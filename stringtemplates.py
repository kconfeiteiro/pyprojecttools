from datetime import datetime

today = datetime.now()

""" Houses useful pre-formatted strings commonly used """

# For file names
OSdate = today.strftime("%Y_%B_%d")  # e.g., 2023_August_06
OSdateTime = today.strftime("%Y_%B_%d_%H%M%S%f")  # e.g., 2023_August_06_123456789012
Longdateformat = today.strftime("%B %d, %Y")  # e.g., August 06, 2023
UnixTimestamp = str(int(today.timestamp()))  # e.g., 1678253696>
ISO8601date = today.strftime("%Y-%m-%d")  # e.g., 2023-08-06


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
