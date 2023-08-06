import io
import threading
from typing import Generator, NamedTuple, Tuple
from pathlib import Path
from subprocess import PIPE, Popen

from _io import BufferedReader  # type: ignore

from bifu.classes.errors import ShellProcessTimeoutError


class ThreadReader(threading.Thread):
    """ Thread that reads from a io_object """
    io_object: BufferedReader
    daemon: bool = False
    finish: bool = False
    output = io.StringIO()

    def __init__(self, io_object: BufferedReader) -> None:
        super().__init__()
        self.io_object = io_object

    # Generator[yield_type, send_type, return_type]
    def reader(self) -> Generator[str, None, None]:
        """ Thread reader - returns live output """
        while True:
            line = self.io_object.readline()

            if not line:
                if self.finish:
                    break
                continue

            yield line
            self.output.write(line)

    def run(self) -> None:
        try:
            for line in self.reader():
                print(line, end='')
        except ValueError:
            pass  # Parent process can close file which is fine

    def stop(self) -> str:
        """ Stop the thread and return output """
        self.finish = True
        return self.output.read()


class Results(NamedTuple):
    stdout: str
    exit_code: int
    stderr: str


class Shell:
    __slots__ = ('_process', '_timeout')
    _process: Popen
    _timeout: int

    def execute(self, command: str, show_live_output: bool = False, timeout: int = 1000) -> Results:
        self._timeout = timeout

        self._process = Popen(
            command, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True,
        )

        try:

            if show_live_output:
                stdout, stderr = self._execute_with_threads()
            else:
                stdout, stderr = self._process.communicate(timeout=self._timeout)

        except TimeoutError as TimeoutErrorAlias:
            self._process.kill()
            raise ShellProcessTimeoutError(self._process.returncode, command) from TimeoutErrorAlias

        return Results(stdout=stdout, exit_code=self._process.returncode, stderr=stderr)

    def _execute_with_threads(self) -> Tuple[str, str]:
        thread_readers = (ThreadReader(self._process.stdout), ThreadReader(self._process.stderr))

        for thread in thread_readers:
            thread.start()

        self._process.wait()
        stdout, stderr = (thread.stop() for thread in thread_readers)

        for thread in thread_readers:
            thread.join()

        return stdout, stderr

    @staticmethod
    def save(path: Path, content: str, chmod: int):
        path.write_text(content)

        if chmod:
            path.chmod(0o755)

        error_code = 1
        if path.read_text() == content:
            error_code = 0

        return error_code

    @staticmethod
    def remove(path: Path):

        if not path.is_file():
            return 0

        path.unlink()

        if not path.is_file():
            return 0

        return 1
