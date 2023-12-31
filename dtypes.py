"""
Custom datatypes for general use.

Script Information
------------------
- Creator: Krysitan D. Confeiteiro
   - confeitk@outlook.com
- Workspace: pyprojecttools
- Filename: dtypes.py
- Date: September, 29 2023

Script Symbols
--------------
- Variables
    - variable `binaryfiles`
    - variable `codinglanguage`
    - variable `coord`
    - variable `months`
    - variable `pol2s`
    - variable `rect2d`
    - variable `rect3d`
    - variable `scriptinglangauge`
    - variable `sph3d`
    - variable `std_inputs`
    - variable `std_numtypes`
    - variable `tabularfiles`
- Classes
    - class `Date`
    - class `Location`
    - class `Measurement`
    - class `OrderedPair`
    - class `OrderedTriple`
    - class `Person`
    - class `PolarCoords`
    - class `Range`
    - class `RectCoords`
    - class `SphCoords`
    - class `Task`
    - class `TaskStatus`
    - class `Wkday`
"""

from enum import Enum
from typing import Literal, NamedTuple

## STANDALONE TYPES
# coding related standalone types
codinglanguage = Literal[
    "python", "javascript", "html", "css", "java", "c", "c++", "c#", "matlab"
]
"""Literal type for popular coding langues."""

scriptinglangauge = Literal["Batch", "PowerShell", "Git Bash", "CMD", "Ubuntu"]
"""Literal type for scripting languages."""

# date|file|directory standalone types
months = Literal[
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"
]
"""Literal type for abbreviated months."""

# System IO related standalone custom types
tabularfiles = Literal[".xlsx", ".xls", ".csv", ".txt"]
"""Common file types for tabular data."""

binaryfiles = Literal[".png", ".jpg", ".pdf"]
"""Common file types for images, gifs, etc."""

# math/physics related standalone types
coord = int | float
"""Standard type for number (more specifically, coordinates)."""

rect2d = Literal["x", "y"]
"""Literal type for 2D rectangular coordiantes."""

pol2s = Literal["r", "phi"]
"""Literal type for polar coordiantes."""

rect3d = Literal["x", "y", "z"]
"""Literal type for 3D rectangular coordiantes."""

sph3d = Literal["r", "phi", "theta"]
"""Literal type for 3D spherical coordiantes."""

# Miscellaneous standalone types
std_inputs = str | float | int
"""Standard input types"""

std_numtypes = int | float
"""Standard types for numerical inputs"""


class Date(NamedTuple):
    """Object for current date.

    Properties:
    - day (int):
    - month (int):
    - year (int):
    """

    day: int
    month: int
    year: int


class Date(NamedTuple):
    """Date objects

    Properties:
    - day (int):
    - month (int):
    - year (int):
    """

    day: int
    month: int
    year: int


class Person(NamedTuple):
    """Object for person, includes name, age, and date of birth.

    Properties:
    - name (str): name of person.
    - age (int|str): age of person.
    - dob (str): person's date of birth.
    """

    name: str
    age: int | str
    dob: str


class Measurement(NamedTuple):
    """Measurement object.

    Properties:
    - value (float): measurment value.
    - unit (str): units of measurment.
    """

    value: float
    unit: str


class Wkday(Enum):
    """Enumerated day object for weekdays with corresponding unique values. This class is the type-hint for the `weekday` property of named-tuple `Date`.

    Properties:
    - Sunday (value = 1)
    - Monday (value = 2)
    - Tuesday (value = 3)
    - Wednesday (value = 4)
    - Thursday (value = 5)
    - Friday (value = 6)
    - Saturday (value = 7)
    """

    Sunday = 1
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7


class Date(NamedTuple):
    """Date object with (month, calendar day, year, weekday)

    Properties:
    -
    """

    month: months
    cday: str | int
    year: str | int
    weekday: Wkday


class TaskStatus(Enum):
    """Statuses for Task object.

    Properties:
    - PENDING (value = 0)
    - TODO (value = 1)
    - IN_PROGRESS (value = 2)
    - PENDING (value = 3)
    - DONE (value = 4)
    """

    PENDING = 0
    TODO = 1
    IN_PROGRESS = 2
    HOLD = 3
    DONE = 4


class Task(NamedTuple):
    """Task object. Defaults `status` to `TaskStatus.PENDING` (pending, value = 0) from `TaskStatus`.

    Properties:
    - description (str): task description.
    - status (TaskStatus): task status (see TaskStatus).
    """

    description: str
    status: TaskStatus = TaskStatus.PENDING


class Range(NamedTuple):
    """Range object. Step is optional.

    Properties:
    - start (int|float): range start value.
    - end (int|float): range end value.
    - step (int|float, optional): step of range. Defaults to None.
    """

    start: std_numtypes
    end: std_numtypes
    step: std_numtypes = None


class OrderedPair(NamedTuple):
    """Ordered pair object (of two). All default to `None` to allow for any combination.

    Properties:
    - first (int|float|str, optional): first property. Defaults to None.
    - second (int|float|str, optional): second property. Defaults to None.

    Also see:
    - `OrderedTriple`
    - `RectCoords`
    - `SphCoords`
    - `PolarCoords`
    - `Location`
    """

    first: std_inputs = None
    second: std_inputs = None


class OrderedTriple(NamedTuple):
    """Ordered pair object (of three). All default to `None` to allow for any combination.

    Properties`:`
    - first (int|float|str, optional): first property. Defaults to None.
    - second (int|float|str, optional): second property. Defaults to None.
    - third (int|float|str, optional): third (last) property. Defaults to None.

    Also see:
    - `OrderedPair`
    - `RectCoords`
    - `SphCoords`
    - `PolarCoords`
    - `Location`
    """

    first: std_inputs = None
    second: std_inputs = None
    third: std_inputs = None


class RectCoords(NamedTuple):
    """Ordered triple object for cartesian coordinates. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`. All default to None to allow for any combination of coordinates.

    Properties:
    - x (int|float, optional): x-coordinate. Defaults to None.
    - y (int|float, optional): y-coordinate. Defaults to None.
    - z (int|float, optional): z-coordinate. Defaults to None.

    Also see:
    - `OrderedPair`
    - `SphCoords`
    - `PolarCoords`
    - `Location`
    """

    x: coord = None
    y: coord = None
    z: coord = None


class SphCoords(NamedTuple):
    """Ordered triple object for spherical coordinates. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`. All default to `None` to allow for any combination of coordinates.

    Properties:
    - r_mag (int|float, optional): distance from origin (magnitude of position vector). Defaults to None.
    - phi (int|float, optional): angle made from cartesian x-axis. Defaults to None.
    - theta (int|float, optional): angle made from cartesian z-axis. Defaults to None.

    Also see:
    - `RectCoords`
    - `PolarCoords`
    - `Location`
    """

    r_mag: coord = None
    phi: coord = None
    theta: coord = None


class PolarCoords(NamedTuple):
    """Ordered triple object for spherical coordinates. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`. All default to None to allow for any combination.

    Properties:
    - r_mag (int|float, optional): distance from origin (magnitude of position vector). Defaults to None.
    - phi (int|float, optional): angle made from cartesian x-axis. Defaults to None.

    Also see:
    - `RectCoords`
    - `SphCoords`
    - `Location`
    """

    r_mag: coord = None
    phi: coord = None


class Location(NamedTuple):
    """Object for locations using longitude/latitude pairs. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`. All default to None to allow for any combination.

    Properties:
    - latitude (int|float, optional): lattitude coordinate. Defaults to None.
    - longitude (int|float, optional): longitude coordinate. Defaults to None.

    Also see:
    - `RectCoords`
    - `SphCoords`
    - `PolarCoords`
    - `OrderedPair`
    - `OrderedTriple`
    """

    latitude: coord = None
    longitude: coord = None
