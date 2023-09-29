"""
`pyprojecttools` - A Versatile Python project toolset package that offers commonly used and miscellaneous functions for most types of Python projects.

`pyprojecttools` is a powerful open-source toolkit for Python project development. It offers essential utilities and efficient workflows for projects of all sizes, simplifying creation, organization, and management. From virtual environments and package management to testing and documentation. `pyprojecttools` offers helper functions, helper libraries, a collection of custom datatypes for type hinting, and more!

Additional info:
- Maintainer: Krystian Ojeda Confeitiro
- Contact: confeitk@outlook.com

### Project tree
```
pyprojecttools
- `baseclasses`
    - `datareaders.py`
    - `pipelines.py`
    - `plotters.py`
    - `__init__.py`
- `batch_scripts`
    - `clonepyprojecttools.bat`
    - `tarExtraction.bat`
    - `update.bat`
- `datahelpers.py`
- `dirhelpers.py`
- `dtypes.py`
- `errors_exceptions.py`
- `iterators.py`
- `monitoring`
    - `lineprofiling.py`
    - `linting.py`
    - `logging.py`
    - `memoryprofiling.py`
    - `methodprofiling.py`
    - `__init__.py`
- `multimmedia`
    - `photomanipulation.py`
    - `__init__.py`
- `reports`
    - `reportelements.py`
    - `reports.py`
    - `__init__.py`
- `strfmts.py`
- `transformations`
    - `coordinates.py`
    - `units.py`
    - `__init__.py`
- `userwarnings.py`
- `utilities`
    - `datatools.py`
    - `listtools.py`
    - `strtools.py`
    - `__init__.py`
- `__init__.py`
```
"""

from .baseclasses import datareaders, pipelines, plotters
from .datahelpers import *
from .dirhelpers import file_filter, mkdirectory
from .multimmedia.photomanipulation import GIF

__version__ = "1.2.2"
__all__ = [
    "datareaders",
    "DirectoryFileIterator",
    "file_filter",
    "GIF",
    "mkdirectory",
    "pipelines",
    "plotters",
]
__license__ = "MIT"
__url__ = "https://github.com/kconfeiteiro/pyprojecttools"
__email__ = "confeitk@outlook.com"
__title__ = "pyprojecttools"

