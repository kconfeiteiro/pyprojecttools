# 1. Contents
- [1. Contents](#1-contents)
- [2. Introduction](#2-introduction)
- [3. Disclaimer](#3-disclaimer)
- [4. Usage](#4-usage)
  - [4.1. Pip Packages](#41-pip-packages)
  - [4.2. Calling Functions](#42-calling-functions)
    - [4.2.1. Working Example](#421-working-example)
  - [4.3. Cloning \& Updating](#43-cloning--updating)
    - [4.3.1. Pull requests](#431-pull-requests)
    - [4.3.2. Additional Tools](#432-additional-tools)
- [5. Issues and Collaboration](#5-issues-and-collaboration)


# 2. Introduction

`pyprojecttools` is a powerful open-source toolkit for Python projects. This toolkit offers essential utilities and efficient workflows for projects of all sizes, simplifying creation, organization, and management. From virtual environments and package management to testing and documentation. `pyprojecttools` offers helper functions, helper libraries, a collection of custom datatypes for type hinting, and more. Collaboration and additional contributions are welcome and encouraged! While trivial in nature this toolkit can offer ease-of-access for simple functions, formatted strings, and more, used in many types of Python projects.

This repository will be continuously maintained by its owner. If there are any issues, please contact [confeitk@outlook.com](mailto:confeitk@outlook.com).


# 3. Disclaimer
The code in this repository was written using version `Python 3.11.4`, meaning, there might be compatibility issues with older Python versions. You can download version 3.11.4 [here](https://www.python.org/downloads/windows/).

# 4. Usage

All you need to do to use the functions is clone the repository locally by typing

```cmd
git clone https://github.com/kconfeiteiro/pyprojecttools
```
in your `cmd` (opened in your working directory). Then, you can call functions from the `pyprojecttools` directory.

For future use, `clonePyProjectTools.bat` has been added to ease the cloning process for multiple projects. The URL does not change, so this can be used as long as need. To run the batch file, simply type

```cmd
clonePyProjectTools.bat
```
in your terminal. Or, click the icon for the `.bat` file from your computer's native file explorer. You can also easily use a *[doskey](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/doskey)* to easily download this package; I would recommend making **[global doskeys](https://superuser.com/questions/1134368/create-permanent-doskey-in-windows-cmd)** to allow for its use across all projects.


## 4.1. Pip Packages

 If you are missing `pip` packages, do not forget to install the `requirements.txt` using the terminal command

```cmd
py -m pip install -r requirements.txt
```

Make sure to be in the directory of the cloned repository, `pyprojecttools`, while `pip` installing the requirements. You can also use a similar command as [Pull Requests](https://github.com/kconfeiteiro/PyProjectTools#pull-requests):

```
pushd pyprojecttools & py -m pip install -r requirements.txt & popd
```

which will change your directory to that of the registry, then `cd ..` will automatically return you to your working directory.

## 4.2. Calling Functions

Project tree:
```
pyprojecttools
├─ baseclasses
│  ├─ datareaders.py
│  ├─ pipelines.py
│  ├─ plotters.py
│  └─ __init__.py
├─ batch_scripts
│  ├─ clonePyProjectTools.bat
│  ├─ tarExtraction.bat
│  └─ update.bat
├─ datahelpers.py
├─ dirhelpers.py
├─ dtypes.py
├─ errors_exceptions.py
├─ iterators.py
├─ monitoring
│  ├─ lineprofiling.py
│  ├─ linting.py
│  ├─ logging.py
│  ├─ memoryprofiling.py
│  ├─ methodprofiling.py
│  └─ __init__.py
├─ multimmedia
│  ├─ photomanipulation.py
│  └─ __init__.py
├─ reports
│  ├─ reportelements.py
│  ├─ reports.py
│  └─ __init__.py
├─ strfmts.py
├─ transform
│  ├─ coordinates.py
│  ├─ units.py
│  └─ __init__.py
├─ userwarnings.py
├─ utilities
│  ├─ datatools.py
│  ├─ listtools.py
│  ├─ strtools.py
│  └─ __init__.py
└─ __init__.py
```

which means to call functions in your main script (`main.py`, in this example), use

```py
from pyprojecttools.dirhelpers import mkdirectory
```

(for example) to import an entire script. If you would like to call a specific class only, use

```py
import pyprojecttools.dirhelpers as helpers
```

*Note*: If you make changes to the cloned repository, they will not be reflected on GitHub unless you [fork the remote repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

### 4.2.1. Working Example

```py
# import the function 'mkdirectory' from the `dirhelpers` script
from pyprojecttools.dirhelpers import mkdirectory

# call function from imported script
filepath = 'example/path/to/dir'
mkdirectory(filepath)
```

where the function, `mkdirectory()`, creates a directory if it does not exist. Calling static functions and classes require the same import syntax.

## 4.3. Cloning & Updating
### 4.3.1. Pull requests

Pull requests are automatically completed. To pull new changes, use the command

```
pushd pyprojecttools & git pull & popd
```

in your terminal (opened in your working directory).


If you do not have git downloaded and configured, the commands above will not work in your terminal. If this is the case, you can simply download the repository as a `.zip` file by clicking *Download Zip* in the green `<> Code` dropdown menu:

![.zip file download window](allMDcontent/image/README/1689627172676.png)

### 4.3.2. Additional Tools

In `useful_batch_scrips` ([link](https://github.com/kconfeiteiro/PyProjectTools/tree/main/useful_batch_scripts)), you can find two scrips:

1. `clonePyProjectTools.bat`
   - Clones the latest version of the repository. Particularly useful if you are working on multiple projects.
2. `update.bat`
   - Pulls from remote repository automatically. No `git` commands neeed.

# 5. Issues and Collaboration

If there are any issues, bugs, or broken functions feel free to contact confeitk@outlook.com. Or, if you would like to contribute, feel free to fork the repository!
