# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bifu', 'bifu.classes']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'munch>=2.5.0,<3.0.0',
 'pygit2>=1.7.2,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'types-PyYAML>=6.0.3,<7.0.0',
 'types-requests>=2.27.19,<3.0.0']

entry_points = \
{'console_scripts': ['bifu = bifu.main:main']}

setup_kwargs = {
    'name': 'bifu',
    'version': '22.4.21',
    'description': 'B.I.F.U. - simple command runner and repository guardian',
    'long_description': '# B.I.F.U.\n\n## Description\n\n**B.I.F.U.** was created to help me remember to do some steps before committing to the repository.\n\nYeah... probably there are many others tools which can do it for you instead of this one ( more-less, i.e. [pre-commit](https://pre-commit.com/) ) so maybe it\'s worth to try "pro" solution :)\n\n**B.I.F.U.** will let you (only):\n- automamically/manually run your defined commands  which should be executed before commiting or pushing to git repository (using git hooks)\n- secure selected branches before commiting (master, main or some productions or "closed" once)\n- [TODO] rebase all new commits to one before pushing to remote repository\n- [TODO] use it as a quick-runner (select some of all tasks to run instead of writing long commands with parameters by hand i.e. pytest, flake, mypy etc)\n- [TODO] force installing pre-commits in developer repository by executing command in python test script/library etc.\n\n**B.I.F.U** doesn\'t install libraries or additional software in your enviroment.\n\nInstead of that it is using your existing enviroment, so first you need to source your python virtual enviroment and then this tool will work.\n\nPlus sides: instant execution and space saving.\n\n\n**B.I.F.U** is short of _"**B**efore **I** **F** _ _ k **U**p"._\n\n\n## Versioning\n\n**B.I.F.U** is versioned using [Calendar Versioning](https://calver.org/) system: \n\nCalendar Versioning schemas:\n\n<img src="https://img.shields.io/badge/calver-YY.MM.DD-22bfda.svg"> or <img src="https://img.shields.io/badge/calver-YY.MM.DD.MICRO-22bfda.svg">\n\n\n    YY - Short year - 6, 16, 106\n    MM - Short month - 1, 2 ... 11, 12\n    DD - Short day - 1, 2 ... 30, 31\n    Micro - Patch (in case when more than one package is released in one day)\n\n## Instalation\n\nTo install **B.I.F.U.** go to your repository and run:\n    \n    pip install bifu\n\n\n## Initiation\n\nTo initiate default config file use command:\n\n```shell\n$ bifu --init\n```\n\nThis command will download **B.I.F.U.** configuration file `.bifu.yml` to current directory.\n\nYou can change this file as you like and test tasks from downloaded/changed file using next commands.\n\nRemember: If you wish to test tasks from downloaded file you need to install requirements from test section (flake8, pytest, mypy etc).\n\n### pre-commit, pre-push installation\n```shell\n$ bifu --install pre-commit\n$ bifu --install pre-push\n```\n\n### Running all jobs\n```shell\n$ bifu --run pre-commit\n$ bifu -r pre-push\n$ bifu -r pre-commit -n 0\n```\n\n### Running job number X\n```shell\n$ bifu --run pre-commit --number 1\n$ bifu -r pre-push -n 3\n```\n\n### pre-commit, pre-push uninstallation\n```shell\n$ bifu --uninstall pre-commit\n$ bifu --uninstall pre-push\n```\n\n## Requirements\n\nTo run **B.I.F.U.** you need to install python in version minimum 3.7 and additional libraries:\n\n```python\nPyYAML = "^6.0"\ntypes-PyYAML = \'^6.0.3\'\npygit2 = "^1.7.2"\nmunch = "^2.5.0"\nrequests = "^2.27.1"\n```\n\nPlease check [pyproject.toml](https://github.com/8tm/bifu/blob/master/.bifu.yml) file to see all requirements.\n\n## ToDo section\n- List all tasks\n- Create menu to select which task should be executed\n- Force installing pre-commit or pre-push\n- Rebase all new commits to one (auto rebase?)\n- Refactor - use dataclasses instead of munch\n',
    'author': 'Tadeusz Miszczyk',
    'author_email': '42252259+8tm@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/8tm/bifu',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
