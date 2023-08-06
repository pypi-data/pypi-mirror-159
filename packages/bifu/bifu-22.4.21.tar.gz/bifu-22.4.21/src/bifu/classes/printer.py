import os
from typing import List


class NoColor:
    end: str = ''

    tasks_bar: str = ''
    commands_bar: str = ''

    output: str = ''
    output_ok: str = ''
    output_failed: str = ''

    status_ok: str = ''
    status_wait: str = ''
    status_failed: str = ''

    grey_bar: str = ''
    light_grey_bar: str = ''


class Printer:
    color = NoColor()
    terminal_width: int = 78

    def __init__(self):
        self.terminal_width, _ = self._get_terminal_size()

    @staticmethod
    def _get_terminal_size() -> List[int]:
        try:
            return list(os.get_terminal_size())
        except OSError:
            return [78, 10]

    def status(self, command: str, error_code: int) -> None:
        print(self.terminal_width * f'{self.color.commands_bar} {self.color.end}', end='\r')

        if error_code == -1:
            text = '  ......  '
            color = self.color.status_wait
            end = '\r'
        elif error_code == 0:
            text = '    OK    '
            color = self.color.status_ok
            end = '\n'
        elif error_code == 1000:
            text = '   INFO   '
            color = self.color.status_wait
            end = '\n'
        else:
            text = '  FAILED  '
            color = self.color.status_failed
            end = '\n'

        print(f'{color}{text}{self.color.end}{self.color.commands_bar} {command}{self.color.end}', end=end)

    def title(self, task_number, task_name):
        print(self.terminal_width * f'{self.color.tasks_bar} {self.color.end}', end='\r')
        print(f'{self.color.tasks_bar}  Task {task_number:^3} {task_name}{self.color.end}')

    def stage(self, stage_name):
        print(self.terminal_width * f'{self.color.light_grey_bar} {self.color.end}', end='\r')
        print(
            f'{self.color.grey_bar}   Stage  {self.color.end}{self.color.light_grey_bar} {stage_name}{self.color.end}',
        )
