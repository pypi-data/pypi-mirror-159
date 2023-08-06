from typing import Dict, Union

import requests

from bifu.classes.pre import PreCommit, PrePush
from bifu.classes.config import PackageConfiguration


class Application:
    pre: Dict[str, Union[PreCommit, PrePush]] = {
        'pre-commit': PreCommit(),
        'pre-push': PrePush(),
    }

    def __init__(self, arguments):
        if arguments.install:
            self.pre[arguments.install].install()
        elif arguments.uninstall:
            self.pre[arguments.uninstall].uninstall()
        else:
            if arguments.run:
                self.pre[arguments.run].run(arguments.number)
            elif arguments.init:
                self.init_configuration()

    @staticmethod
    def init_configuration():
        package = PackageConfiguration
        url = f'https://raw.githubusercontent.com/8tm/{package.name}/master/.{package.name}.yml'
        r = requests.get(url, allow_redirects=True)

        with open(f'.{package.name}.yml', 'w') as config_file:
            config_file.write(r.content.decode())
