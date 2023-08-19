from enum import Enum
from typing import Literal, Type, NamedTuple

from pandas import DataFrame, Series
from numpy import array

""" Custom data type that fits the 'tabular data' structure """

# pandas dataframe
pdDataFrame = Type[DataFrame]
pdSeries = Type[Series]
npArray = Type[array]

# coding related
codinglanguage = Literal[
    "python", "javascript", "html", "css", "java", "c", "c++", "c#", "matlab"
]
scriptinglangauge = Literal["batch", "powershell", "git bash", "CMD", "ubuntu"]


class Date(NamedTuple):
    """Named tuple for Date objects

    Properties:
    - day (int):
    - month (int):
    - year (int):
    """

    day: int
    month: int
    year: int


class Person(NamedTuple):
    """Named tuple for Person objects

    Properties:
    - name (str):
    - age (int):
    - dob (str):
    """

    name: str
    age: int
    dob: str


class Measurement(NamedTuple):
    """Named tuple for Measurement objects

    Properties:
    - value (float):
    - unit (str):
    """

    value: float
    unit: str


class Day(Enum):
    """For Day objects

    Properties:
    - Monday (1)
    - Tuesday (2)
    - Wednesday (3)
    - Thursday (4)
    - Friday (5)
    - Saturday (6)
    - Sunday (7)
    """

    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


class TaskStatus(Enum):
    """Statuses for Task object

    Properties:
    - TODO (1)
    - IN_PROGRESS (2)
    - DONE (3)
    """

    TODO = 1
    IN_PROGRESS = 2
    DONE = 3


class Task(NamedTuple):
    """Named tuple for Task objects

    Properties:
    - description (str):
    - status (TaskStatus):
    """

    description: str
    status: TaskStatus


class Range(NamedTuple):
    """Named tuple for Range objects

    Properties:
    - start (float): Range start value
    - end (float): Range end value
    """

    start: float
    end: float
