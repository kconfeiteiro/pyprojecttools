"""
Abstract classes for child classes for general data-reading usage.

Classes
-------
class Reader
	method __init__
	method load
	method prepare
	method read
	method save
"""

from abc import ABC, abstractmethod

from ..dtypes import binaryfiles, tabularfiles


class Reader(ABC):
    """
    Abstract base class for general data-reading objects.

    Attributes:
        input_pth (type): Path to input data (or diectory).
        save_as (type): File extension to save your data as (read from file or directory).

    Inheritance:
        ABC: Abstract base class.

    Args:
        input_pth (str=None): Path to input data (or diectory).
        save_as (tabularfiles|binaryfiles=None): File extension to save your data as (read from file or directory).

    """

    def __init__(
        self,
        input_pth: str = None,
        save_as: tabularfiles | binaryfiles = None,
    ) -> None:
        self.input_pth = input_pth
        self.save_as = save_as

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def save(self):
        pass
