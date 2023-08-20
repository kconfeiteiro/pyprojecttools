from datetime import datetime
from enum import Enum
from typing import Any, Literal, NamedTuple, TypeVar

from sympy import Union

""" Custom data type that fits the 'tabular data' structure """

## STANDALONE TYPES
# coding related standalone types
codinglanguage = Literal[
    "python", "javascript", "html", "css", "java", "c", "c++", "c#", "matlab"
]
scriptinglangauge = Literal["Batch", "PowerShell", "Git Bash", "CMD", "Ubuntu"]

# math/physics related standalone types
coord = int | float

# date|file|directory standalone types
today = datetime.now()
months = Literal[
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"
]

# math/physics related standalone types
coord = int | float
cart_coords = Literal["x", "y", "z"]
sph_coords = Literal["r", "phi", "theta"]

# date|file|directory standalone types
today = datetime.now()
months = Literal[
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"
]

# Miscellaneous standalone types
std_inputs = str | float | int
std_numtypes = int | float


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
    """Range object.

    Properties:
    - start (int|float, optional): range start value.
    - end (int|float, optional): range end value.
    - step (int|float, optional): step of range. Defaults to None.
    """

    start: std_numtypes
    end: std_numtypes
    step: std_numtypes = None


class OrderedPair(NamedTuple):
    """Ordered pair object (of two).

    Properties:
    - first (int|float|str): first property.
    - second (int|float|str): second property.
    """

    first: std_inputs
    second: std_inputs


class OrderedTriple(NamedTuple):
    """Ordered pair object (of three).

    Properties:
    - first (int|float|str): first property.
    - second (int|float|str): second property.
    - third (int|float|str): third (last) property.
    """

    first: std_inputs
    second: std_inputs
    third: std_inputs


class CartCoords(NamedTuple):
    """Ordered triple object for cartesian coordinates. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`.

    Properties:
    - x (int|float): x-coordinate.
    - y (int|float): y-coordinate.
    - z (int|float): z-coordinate.
    """

    x: coord
    y: coord
    z: coord


class SphCoords(NamedTuple):
    """Ordered triple object for spherical coordinates. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`.

    Properties:
    - r_mag (int|float): distance from origin (magnitude of position vector)
    - phi (int|float): angle made from cartesian x-axis.
    - theta (int|float): angle made from cartesian z-axis
    """

    r_mag: coord
    phi: coord
    theta: coord


class PolarCoords(NamedTuple):
    """Ordered triple object for spherical coordinates. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`.

    Properties:
    - r_mag (int|float): distance from origin (magnitude of position vector)
    - phi (int|float): angle made from cartesian x-axis.
    """

    r_mag: coord
    phi: coord


class Location(NamedTuple):
    """Object for locations using longitude/latitude pairs. If you want a more general object for tuples, see `OrderedPair` and `OrderedTriple`.

    Properties:
    - latitude (int|float): lattitude coordinate.
    - longitude (int|float): longitude coordinate.
    """

    latitude: coord
    longitude: coord
