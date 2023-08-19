from typing import Any, List, Literal, MutableSequence, Tuple

import sympy


"""Anything related to transformatiosn of any kind"""


def cart_to_polar(
    data: Tuple[List] = None, units: Literal["deg", "rad"] = "deg"
) -> Tuple[MutableSequence[float]]:
    """Function that converts cartesian coordinates to polar coordinate

    Args:
        data (tuple, optional): tuple of immutable sequences (your data). Defaults to None.
        units (literal, optional): what you want to convert. Defaults to "deg".

    Returns:
        Tuple: New lists with converted values
    """
    x_vals, z_vals, y_vals = data
    r_vals = list(map(r_, x_vals, y_vals, z_vals))
    theta_vals = list(map(theta_, z_vals, r_vals))
    phi_vals = list(map(phi_, y_vals, x_vals))

    conversion_func = rad2deg if units == "rad" else deg2rad
    theta_vals = list(map(conversion_func, theta_vals))
    phi_vals = list(map(conversion_func, phi_vals))

    return (r_vals, theta_vals, phi_vals)


def convert(units: Literal["rad to deg", "deg to rad"] = "rad to deg"):
    """Wrapper to convert a tuple (or list) of three or more columns into degrees or radius

    Args:
        units (literal, optional): The conversion direction (degrees to radius and vice versa). Defaults to "rad to deg".
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            conversion_func = rad2deg if units == "rad to deg" else deg2rad
            to_convert = func(*args, **kwargs)
            assert isinstance(
                to_convert, MutableSequence
            ), "Returns must be a list or tuple of your columns"
            converted = [conversion_func(angle) for col in to_convert for angle in col]
            return converted

        return wrapper

    return decorator


def r_(x: float = ..., y: float = ..., z: float = ...) -> float:
    """converts an 'x' coordiante to 'r' in polar or spherical coordiantes.

    Args:
        x (MutableSequence[float], optional): x coordinate. Defaults to ....
        y (MutableSequence[float], optional): y coordinate. Defaults to ....
        z (MutableSequence[float], optional): z coordinate. Defaults to ....

    Returns:
        float: converted coordinate
    """
    return sympy.sqrt(x**2 + y**2 + z**2)


def theta_(z: float = ..., r: float = ...) -> float:
    """Finds theta value from 'z' and 'r'

    Args:
        z (float, optional): z coordinate. Defaults to ....
        r (float, optional): r coordinate. Defaults to ....

    Returns:
        float: converted coordinate
    """
    return sympy.acos(z / r)


def phi_(y: float = ..., x: float = ...) -> float:
    """Finds phi value from 'y' and 'x'

    Args:
        y (float, optional): y coordinate. Defaults to ....
        x (float, optional): x coordinate. Defaults to ....

    Returns:
        float: Converted coordinate
    """
    return sympy.atan2(y, x)


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
