"""Abstract base classes for plotting objects."""

from abc import ABC, abstractmethod, abstractproperty
from typing import Any

from baseclasses import RANGE
from pandas import DataFrame
from utilities.datatools import reduce_df


class Plot(ABC):
    """
    Standard abastract base class for generic plots.

    Method:
        prepdata: Prepare data.
        plot: Executes plotting code.
        savefig: Saves figure(s).

    Properties:
        figure: Returns figure object.
        reduce_data (RANGE values): setting to reduce data; either `.low` (25%), `.med` (50%), and `.high` (75%) of original dataaset size.

    Inheritance:
        ABC: Abstract Base Class.

    Raises:
        ValueError: If inputted (int or float) value is not between `(0, 1]`
    """

    __reduction_range = RANGE | int | float | None

    def __init__(
        self,
        dataset: DataFrame | Any = None,
        reduce_data: __reduction_range = None,
    ) -> None:
        self.dataset = dataset
        self.reduce_data = reduce_data

        if self.reduce_data:
            if isinstance(self.reduce_data, int | float) and (
                self.reduce_data > 1 or self.reduce_data <= 0
            ):
                _msg = f"As an numerical value, 'reduce_data' must be between range [0, 1]. Recieved {self.reduce_data}"
                raise ValueError(_msg)

    @abstractmethod
    def prepdata(self):
        pass

    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def savefig(self):
        pass

    @abstractproperty
    def figure(self):
        pass

    @property
    def dataset(self):
        return self.dataset

    @dataset.setter
    def dataset(self, value):
        self.dataset = value

    def _reduce_data(self, amt: __reduction_range = None):
        """
        Reduces data by `RANGE` setting or by custom size (int or float, between `0` and `1`). Private Method.

        Value range:
        - low = 0.25
        - med = 0.5
        - high = 0.75

        Args:
            amt (int, optional): New decimal percentage-based size of original dataset. Defaults to None.
        """
        self.dataset = reduce_df(self.dataset, amt)
