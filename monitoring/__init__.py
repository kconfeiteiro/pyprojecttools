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
- function get_traceback
"""

import traceback


def get_traceback():
    """Returns the traceback of the last exception as a string."""
    return traceback.format_exc()
