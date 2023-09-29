"""
Houses useful pre-formatted strings commonly used

Script Information
------------------
- Creator: Krysitan D. Confeiteiro
   - confeitk@outlook.com
- Workspace: pyprojecttools
- FIlename: strfmts.py
- Date: September, 29 2023

Script Symbols
--------------
- variable `ISO8601date`
- variable `longdateformat`
- variable `osdate_time`
- variable `osdate`
- variable `today`
- variable `unixtimestamp`
- function `calculate_age`
	- variable `age`
	- variable `birthdate`
	- variable `day`
	- variable `month`
	- variable `today`
	- variable `year`
"""
from datetime import datetime

today = datetime.now()


# For file names
osdate = today.strftime("%Y_%m_%d")
"""Currnet date (without time) for dir/file names, i.e., 2023_August_06"""

osdate_time = today.strftime("%Y_%B_%d_%H%M%S%f")
"""Currnet date including timestamp for dir/file names, i.e., 2023_August_06_123456789012"""


longdateformat = today.strftime("%B %d, %Y")
"""Currnet date in standard long-date formate for reports, plots, etc., (e.g., August 06, 2023)"""


unixtimestamp = str(int(today.timestamp()))
"""Currnet date Unix timestamp i.e., 1678253696>"""


ISO8601date = today.strftime("%Y-%m-%d")
"""Currnet date in ISO8601date formate, i.e., 2023-08-06"""


# birthday calculator
def calculate_age(year: int = None, month: int = None, day: int = None) -> int:
    """Calculates your current age

    Args:
        year (int, optional): Year you were born. Defaults to None.
        month (int, optional): Month you were born. Defaults to None.
        day (int, optional): Day you were born. Defaults to None.

    Returns:
        int: your age in years
    """
    assert all(
        isinstance(var, int) for var in [year, month, day]
    ), "All arguments must be of type 'int'"
    birthdate = datetime.date(year, month, day)
    today = datetime.date.today()
    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    return age
