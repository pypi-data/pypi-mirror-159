# B.I.F.U.

## Description

**B.I.F.U.** was created to help me remember to do some steps before committing to the repository.

Yeah... probably there are many others tools which can do it for you instead of this one ( more-less, i.e. [pre-commit](https://pre-commit.com/) ) so maybe it's worth to try "pro" solution :)

**B.I.F.U.** will let you (only):
- automamically/manually run your defined commands  which should be executed before commiting or pushing to git repository (using git hooks)
- secure selected branches before commiting (master, main or some productions or "closed" once)
- [TODO] rebase all new commits to one before pushing to remote repository
- [TODO] use it as a quick-runner (select some of all tasks to run instead of writing long commands with parameters by hand i.e. pytest, flake, mypy etc)
- [TODO] force installing pre-commits in developer repository by executing command in python test script/library etc.

**B.I.F.U** doesn't install libraries or additional software in your enviroment.

Instead of that it is using your existing enviroment, so first you need to source your python virtual enviroment and then this tool will work.

Plus sides: instant execution and space saving.


**B.I.F.U** is short of _"**B**efore **I** **F** _ _ k **U**p"._


## Versioning

**B.I.F.U** is versioned using [Calendar Versioning](https://calver.org/) system: 

Calendar Versioning schemas:

<img src="https://img.shields.io/badge/calver-YY.MM.DD-22bfda.svg"> or <img src="https://img.shields.io/badge/calver-YY.MM.DD.MICRO-22bfda.svg">


    YY - Short year - 6, 16, 106
    MM - Short month - 1, 2 ... 11, 12
    DD - Short day - 1, 2 ... 30, 31
    Micro - Patch (in case when more than one package is released in one day)

## Instalation

To install **B.I.F.U.** go to your repository and run:
    
    pip install bifu


## Initiation

To initiate default config file use command:

```shell
$ bifu --init
```

This command will download **B.I.F.U.** configuration file `.bifu.yml` to current directory.

You can change this file as you like and test tasks from downloaded/changed file using next commands.

Remember: If you wish to test tasks from downloaded file you need to install requirements from test section (flake8, pytest, mypy etc).

### pre-commit, pre-push installation
```shell
$ bifu --install pre-commit
$ bifu --install pre-push
```

### Running all jobs
```shell
$ bifu --run pre-commit
$ bifu -r pre-push
$ bifu -r pre-commit -n 0
```

### Running job number X
```shell
$ bifu --run pre-commit --number 1
$ bifu -r pre-push -n 3
```

### pre-commit, pre-push uninstallation
```shell
$ bifu --uninstall pre-commit
$ bifu --uninstall pre-push
```

## Requirements

To run **B.I.F.U.** you need to install python in version minimum 3.7 and additional libraries:

```python
PyYAML = "^6.0"
types-PyYAML = '^6.0.3'
pygit2 = "^1.7.2"
munch = "^2.5.0"
requests = "^2.27.1"
```

Please check [pyproject.toml](https://github.com/8tm/bifu/blob/master/.bifu.yml) file to see all requirements.

## ToDo section
- List all tasks
- Create menu to select which task should be executed
- Force installing pre-commit or pre-push
- Rebase all new commits to one (auto rebase?)
- Refactor - use dataclasses instead of munch
