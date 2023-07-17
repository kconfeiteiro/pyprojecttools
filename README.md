# Introduction

The purpose of this repository is just to include all of the small functions I use for multiple projects. Having them here allows me to simply clone the repository rather than copying the code for each project. This repository is a work in progress and I will be adding whichever functions I find are useful. As this repository grows, I will improve on its organization, as it was thrown together relatively quickly, so its organization is questionable, at best. Explore all the functions in the `Utils` directory.

# Usage

All you need to do to use the functions is clone the repository locally by typing 

```
git clone https://github.com/kconfeiteiro/PyProjectTools
```

 in your `cmd` (opened in your working directory). Then, you can call functions from the `PyProjectUtils` directory. 

 ## Pip Packages
 If you are missing `pip` packages, do not forget to install the `requirements.txt` using the terminal command
 ```
py -m pip install -r requirements.txt
```

## Calling Functions
The layout of the directory is (after its cloned)
```
└───PyProjectUtils
     |
     └───Utils
         │   DataSaving.py
         │   FileReading.py
         │   FileSorting.py
         │   Tools.py
         │   __init__.py
```
To call functions in your main script, use
```py
from PyProjectUtils import Tools
``` 
(for example) to import an entire script. If you would like to call a specific class only, use 
```py
from PyProjectUtils.Utils.Tools import Tools
``` 
to import a single class. Note that if you make changes to the cloned repository, they will not be reflected on GitHub.

### Working Example
```py
# import the class 'Directories' from the FileSorting script
from PyProjectUtils.Utils.FileSorting import Directories as dr

# call function from the imported class
filepath = 'example/path/to/dir'
dr.mkdir(filepath)
```
where the function `dr.mkdir()` creates a directory if it does not exist.

## Pull requests

Pull requests are automatically completed. To pull new changes, use the command

```
cd PyProjectTools & git pull https://github.com/kconfeiteiro/PyProjectTools & cd ..
```

in your terminal (opened in your working directory).

# Issues and Collaboration

If there are any issues, bugs, or broken functions feel free to contact confeitk@outlook.com. Or, if you would like to add functions of your own, feel free to fork the repository!
