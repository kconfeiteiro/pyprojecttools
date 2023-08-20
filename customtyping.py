from datetime import datetime
from enum import Enum
from typing import Literal, NamedTuple


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


class Weekday(Enum):
    """For Day object.

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
    weekday: Weekday


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
    - start (float): Range start value.
    - end (float): Range end value.
    """

    start: float
    end: float


class OrderedPair(NamedTuple):
    """Named tuple for ordered pair (of two). Not constricted to cartesian|polar coordinate systems, i.e., (lattitude, longitude).

    Properties:
        x (int|float): x-coordinate.
        y (int|float): y-coordiante.
    """

    x: coord
    y: coord


class OrderedPair(NamedTuple):
    """Named tuple for ordered triplets (of three). Not constricted to cartesian|sphereical coordinate systems.

    Properties:
        x (int|float): x-coordinate.
        y (int|float): y-coordiante.
        z (int|float): z-coordiante.
    """

    x: coord
    y: coord
    z: coord


class Location(NamedTuple):
    """Object for locations using longitude/latitude pairs.

    Properties:
    - latitude (int|float): lattitude coordinate
    - longitude (int|float): longitude coordinate
    """

    latitude: coord
    longitude: coord
