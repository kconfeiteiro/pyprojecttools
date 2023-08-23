"""Abstract base classes for plotting objects."""

from abc import ABC, abstractmethod, abstractproperty


class Plot(ABC):
    """
    Standard abastract base class for generic plots.

    Method:
        prepdata: Prepare data.
        plot: Executes plotting code.
        savefig: Saves figure(s).

    Properties:
        figure: Returns figure object.

    Inheritance:
        ABC: Abstract Base Class.
    """

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