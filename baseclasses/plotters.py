"""
Abstract base classes for plotting objects.

Classes
-------
class Plot
	variable reduc_types
	method __init__
	method columns
	method dataset
	method figure
	method plot
	method prepdata
	method savefig
	variable figtitle
	variable output_dir
	variable reduce_data
	variable save_as
	variable size


"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional

from pandas import DataFrame

from ..errors_exceptions import KeyErrorWarning, MissingDataError
from ..utilities.datatools import reduce_df
from . import RANGE


class Plot(ABC):
    """
    Standard abastract base class for generic plots.

    Method:
        plot: Executes plotting code.
        prepdata: Prepare data.
        savefig: Saves figure(s).

    Properties:
        columns (List[str] | None, optional): Columns you want to plot. Defaults to None.
        dataset (DataFrame | Any, optional): Data to plot (use in tandem with `columns` or input plot-ready dataframe). Defaults to None.
        display (bool, optional): Toggle dislpay of plot(s) using `Plotly` methods. Defaults to True.
        figtitle (Tuple[str, bool], optional): Tuple of the figure title and boolean to toggle title centering, i.e., `("Title", True)`. Defaults to None.
        output_dir (str, optional): Directory to output saved plots. Optional, `os.getcwd()` is called when `output_dir` is `None`.
        reduce_data (Plot.reduc_types, optional): Reduces data base on 'levels' (RANGE.low/RANGE.med/RANGE.high) or decimal values between (0, 1). Defaults to None.
        save_as (str, optional): File name to save plot as. Defaults to None.
        size (str, optional): Tuple figure size. Defaults to None.

    Inheritance:
        ABC: Abstract Base Class.

    Raises:
        ValueError: If inputted (int or float) value is not between `(0, 1]`
        ValueError: Missing `data` or `columns` inputs.
        KeyError: Incorrect value for `RANGE` setter. Use either `RANGE.low`, `RANGE.med`, or `RANGE.high`
        ValueError: Configuration values must not be empty (None)
    """

    reduc_types = Optional[RANGE | int | float]

    def __init__(
        self,
        columns: Optional[List[str]] = None,
        dataset: DataFrame | Any = None,
        figtitle: str = None,
        output_dir: Optional[str] = None,
        reduce_data: reduc_types = None,
        save_as: str = None,
        size: str = None,
    ) -> None:
        self.columns = columns
        self.dataset = dataset
        self.figtitle = figtitle
        self.output_dir = output_dir
        self.reduce_data = reduce_data
        self.save_as = save_as
        self.size = size

        self._fig = None
        self._config = {
            "columns": self.columns,
            "dataset": self.dataset,
            "figtitle": self.figtitle,
            "output_dir": self.output_dir,
            "reduce_data": self.reduce_data,
            "save_as": self.save_as,
            "size": self.size,
        }

        if not self.columns and (3 < self.dataset.shape[1] <= 0):
            _msg = f"Invalid data shape: {self.dataset.shape}. Data must have three columns"
            raise MissingDataError(self.dataset)

        if all(value is not None for value in self._config.values()):
            msg = f"Configuration values must not be empty (None). Recieved:\n{self._config}"
            raise ValueError(msg)

        if self.reduce_data:
            if isinstance(self.reduce_data, int | float) and not (
                0 < self.reduce_data <= 1
            ):
                _msg = f"As an numerical value, 'reduce_data' must be between range [0, 1]. Recieved {self.reduce_data}"
                raise ValueError(_msg)
            elif not isinstance(
                self.reduce_data, int | float
            ) and self.reduce_data not in [RANGE.low, RANGE.med, RANGE.high]:
                _msg = "Incorrect value for `RANGE` setter. Use either `RANGE.low`, `RANGE.med`, or `RANGE.high`"
                raise KeyError(_msg)
            self._reduce_data(self.reduce_data)

    def prepdata(self):
        self.dataset = self.dataset[[*self.columns]]

    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def savefig(self):
        pass

    @property
    def figure(self):
        return self._fig

    @property
    def dataset(self):
        return self.dataset

    @dataset.setter
    def dataset(self, value):
        self.dataset = value

    @property
    def columns(self):
        return self.columns

    @columns.setter
    def columns(self, value):
        self.columns = value

    def _reduce_data(self):
        """
        Reduces data by `RANGE` setting or by custom size (int or float, between `0` and `1`). Private Method.

        Value range:
        - low = 0.25
        - med = 0.5
        - high = 0.75

        Args:
            amt (int, optional): New decimal percentage-based size of original dataset. Defaults to None.
        """
        self.dataset = reduce_df(self.dataset, self.reduce_data)
