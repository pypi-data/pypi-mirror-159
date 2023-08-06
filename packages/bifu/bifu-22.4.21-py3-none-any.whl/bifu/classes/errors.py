class ShellProcessTimeoutError(BaseException):
    _exception_message: str = 'Shell command failed with exit code: {} \nError message: \nCommand "{}" timed out.'

    def __init__(self, exit_code: int, commandz: str):
        super().__init__(self._exception_message.format(exit_code, commandz))
