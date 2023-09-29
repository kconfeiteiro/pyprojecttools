"""
Library for application monitoring.

Current supporting monitoring types
------------------------------------
- Line profiling
- Linting
- Logging
- Memory profiling
- Method profiling

Functions
---------
- function `get_traceback`

Module Symbols
--------------
__init__.py
---
- function `get_traceback`

memoryprofiling.py
---
- class `MemoryProfiler`

logging.py
---
- variable `today`
- variable `formatted_date`
- class `LoggerBackend`
	- method `generate_unique_name`
- class Logger
	- method `log`
		- function `decorator`
			- function `wrapper`
	- method `manual_log`
- class LogDictConfig
    - variable `filename`
    - variable `filemode`
    - variable `format`
    - variable `level`

linting.py
---
- class `Lint`

lineprofiling.py
---
- class `LineProfiler`


methodprofiling.py
---
- class `Counter`
- class `Timer`
"""

import traceback


def get_traceback():
    """Returns the traceback of the last exception as a string."""
    return traceback.format_exc()
