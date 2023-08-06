import sys
from pathlib import Path

import pygit2 as git  # type: ignore
import yaml
from munch import DefaultMunch  # type: ignore


class GitConfiguration:
    current_path: Path = Path().cwd()
    repository_dot_git_path: Path = Path()
    repository_path: Path = Path()
    repo: git.repository.Repository = None
    branch_name: str = ''
    all_branches: str = '^*'
    branch_configuration: str = ''
    unknown_branch_name: str = 'bifu__UNKNOWN_BRANCH_NAME'

    def __init__(self):
        path = git.discover_repository(self.current_path)

        if path is None:
            print(f'Error 1: Git repository not found in path: {self.current_path}')
            sys.exit(1)

        self.repository_dot_git_path = Path(path)
        self.repository_path = self.repository_dot_git_path.parent
        self.repo = git.repository.Repository(self.repository_path)
        self.branch_name = self.get_branch_name()

    def get_branch_name(self) -> str:
        try:
            branch_name = self.repo.head.name.replace('refs/heads/', '')
        except git.GitError:
            branch_name = self.unknown_branch_name
        return branch_name


class PackageConfiguration:
    name: str = 'bifu'
    configuration_file_name: str = ''
    configuration_file_path: Path = Path()
    repository_url: str = 'https://github.com/8tm/bifu'

    def __init__(self):
        git_configuration = GitConfiguration()
        self.configuration_file_name = f'.{self.name}.yml'
        self.configuration_file_path = git_configuration.repository_path / self.configuration_file_name

        if not self.configuration_file_path.is_file():
            print(f'Error 2: Configuration file not found in path "{git_configuration.repository_path}"')
            # sys.exit(2)


class YamlConfiguration:
    configuration: DefaultMunch = {}

    def load_configuration(self):
        base_configuration = PackageConfiguration()
        with open(base_configuration.configuration_file_path) as file:
            yaml_content = yaml.full_load(file)
        self.configuration = DefaultMunch.fromDict(yaml_content)
