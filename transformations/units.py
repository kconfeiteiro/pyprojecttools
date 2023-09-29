"""
Anything related to unit conversions of any kind.

Script Information
------------------
- Creator: Krystian D. Confeiteiro
    - Contact: confeitk@outlook.com
- Workspace: pyprojecttools
- FIlename: units.py
- Path: transformations\units.py
- Date: September, 29 2023

Script Information
------------------
- function `rad2deg`
- function `deg2rad`
"""

import sympy



def rad2deg(angle: float = ...) -> float:
    """Converts angle from radians to degree

    Args:
        angle (float, optional): angle in radians. Defaults to ....

    Returns:
        float: angle in degrees
    """
    return angle * (180 / sympy.pi)


def deg2rad(angle: float = ...) -> float:
    """Converts angle from degrees to radians

    Args:
        angle (float, optional): angle in degrees. Defaults to ....

    Returns:
        float: angle in radians
    """
    return angle * (sympy.pi / 180)
