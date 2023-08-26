import sympy

"""Anything related to unit conversions of any kind"""


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
