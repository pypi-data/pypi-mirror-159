import sys

from munch import DefaultMunch  # type: ignore

from bifu.classes.printer import Printer
from bifu.classes.config import GitConfiguration, PackageConfiguration, YamlConfiguration
from bifu.classes.process import Shell


class Pre:
    git = GitConfiguration()
    package = PackageConfiguration()
    printer = Printer()
    shell = Shell()
    yaml = YamlConfiguration()
    hook_name: str = ''

    def _select_branch_configuration(self):
        self.yaml.load_configuration()

        if self.yaml.configuration[self.hook_name] is None:
            print(f'Error 3: Section {self.hook_name} not fund')
            sys.exit(3)

        if self.git.branch_name in self.yaml.configuration[self.hook_name]:
            self.git.branch_configuration = self.git.branch_name
        elif self.git.all_branches in self.yaml.configuration[self.hook_name]:
            self.git.branch_configuration = self.git.all_branches
        else:
            print(
                f'\nCannot find configuration for branch "{self.git.branch_name}".\n'
                f'{self.package.name} will exit with an exit code 255.\n'
                f'Create configuration for this branch or for all branches.\n',
            )
            sys.exit(255)

        if self.yaml.configuration[self.hook_name][self.git.branch_configuration].tasks is None:
            print(
                f'\nCannot find tasks for branch "{self.git.branch_name}".\n'
                f'{self.package.name} will exit with an exit code 200.\n'
                f'Add tasks for this branch or for all branches.\n',
            )
            sys.exit(200)

    def _load_theme(self) -> None:
        if self.yaml.configuration.theme and self.yaml.configuration.theme.themed:

            for key in self.yaml.configuration.theme:
                self.yaml.configuration.theme[key] = f'\033[{self.yaml.configuration.theme[key]}'

            self.yaml.configuration.theme['end'] = '\033[0m'
            self.printer.color = DefaultMunch.fromDict(self.yaml.configuration.theme)

    def _run_commands(self, stage_name, stage_data, show_output: bool = False) -> int:
        error_code = 0

        if stage_data[stage_name] is None:
            error_code = 1
            return error_code

        show_live_output = stage_data[f'{stage_name} output']

        if show_output and show_live_output:
            self.printer.stage(stage_name)

        for command in stage_data[stage_name]:
            process_error_code = self.shell.execute(command, show_live_output=show_live_output)[1]

            if show_output and show_live_output:
                self.printer.status(command, process_error_code)

            error_code = error_code + process_error_code

        return error_code

    def _run_task(self, task_number: int, task_name: str) -> int:
        show_output = self.yaml.configuration[self.hook_name][self.git.branch_configuration].output

        if show_output:
            self.printer.title(task_number, task_name)

        error_code = 0
        if self.yaml.configuration.tasks[task_name] is None:
            print(f" - Task {task_name} doesn't exists!")
            error_code = 1

        if self.yaml.configuration.tasks[task_name]['before script']:
            error_code = error_code + self._run_commands(
                'before script', self.yaml.configuration.tasks[task_name], show_output,
            )
        error_code = error_code + self._run_commands('script', self.yaml.configuration.tasks[task_name], show_output)
        if self.yaml.configuration.tasks[task_name]['after script']:
            error_code = error_code + self._run_commands(
                'after script', self.yaml.configuration.tasks[task_name], show_output,
            )
        return error_code

    def _run_all_tasks(self, task_number: int = 0):
        error_code = 0
        number_of_tasks = len(self.yaml.configuration[self.hook_name][self.git.branch_configuration].tasks)

        if 0 < task_number <= number_of_tasks:
            error_code = self._run_task(
                task_number,
                self.yaml.configuration[self.hook_name][self.git.branch_configuration].tasks[task_number - 1],
            )
        elif task_number > number_of_tasks:
            print(f'There is no task number {task_number}.\nThis branch has only {number_of_tasks} task(s)')
            sys.exit(6)
        else:
            tasks = self.yaml.configuration[self.hook_name][self.git.branch_configuration].tasks
            for task_id, task_name in enumerate(tasks, start=1):
                error_code = error_code + self._run_task(task_id, task_name)

        sys.exit(error_code)

    def install(self) -> None:
        status_title = f'Installing "{self.package.name}" {self.hook_name} hook'
        self.printer.status(status_title, -1)
        error_code = self.shell.save(
            path=self.git.repository_dot_git_path / 'hooks' / self.hook_name,
            content=f'{self.package.name} --run {self.hook_name}',
            chmod=0o755,
        )
        self.printer.status(status_title, error_code)
        sys.exit(error_code)

    def uninstall(self):
        status_title = f'Uninstalling {self.hook_name} hook'
        self.printer.status(status_title, -1)
        error_code = self.shell.remove(self.git.repository_dot_git_path / 'hooks' / self.hook_name)
        self.printer.status(status_title, error_code)
        sys.exit(error_code)


class PreCommit(Pre):
    hook_name: str = 'pre-commit'

    def _check_guardian(self) -> None:
        if self.yaml.configuration[self.hook_name][self.git.branch_configuration].block_commits:
            error_code = 5
            self.printer.status('commit changes', error_code)
            print(
                f"\n{11*' '}Branch {self.git.branch_name} has a commit blocker enabled!\n"
                f"{11*' '}You can't commit to this branch \n"
                f"{11*' '}because you can't push into it!\n",
            )
            sys.exit(error_code)

    def run(self, task_number: int = 0) -> None:
        self._select_branch_configuration()
        self._load_theme()
        self._check_guardian()
        self._run_all_tasks(task_number)


class PrePush(Pre):
    hook_name: str = 'pre-push'

    def run(self, task_number: int = 0) -> None:
        self._select_branch_configuration()
        self._load_theme()
        self._run_all_tasks(task_number)
