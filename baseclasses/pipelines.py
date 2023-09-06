"""
Blueprint for various pipeline algorithms

Classes
-------
class PipelineBase
	method __new__
	method __init_subclass__
	method __repr__
	method generate_report
	method preprocess
	method run
	method save
class DataPipeline
	method __init__
	method __len__
	method __getitem__
	method __iter__
	method add_data
	method analyze
	method plots
	method statistics

Abstract Methods From `Pipelinebase`
------------------------------------
- Preprocess: For preprocessing data.
- Run: Executes the entire pipeline (for running all subsequent methods in a single method).
- Save: For saving all the processed data/images/etc.
- Generate_report: For generating report summary of pipeline run.

"""

from abc import ABC, abstractmethod

from pandas import Series, DataFrame

from ..iterators import ObjIterator


class PipelineBase(ABC):
    """
    Base class for different generic pipelines.

    Abstract methods:
        preprocess: Preprocesing for all data.
        run: Runs the entire pipeline.
        save: Saves everything from the pipeline run.
        generate_report: Generates PDF report/summary of the pipeline's run.

    Inheritance:
        ABC: methods for Abstract Base Classes.

    """

    def __new__(cls, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__repr__ = cls.__repr__

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ", ".join(
            f"{attr}={getattr(self, attr)!r}" for attr in self.__dict__
        )
        return f"{class_name}({attributes})"

    @abstractmethod
    def preprocess(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass


class DataPipeline(PipelineBase):
    """
    Base class for data-processing pipelines.

    Abstract methods:
        statistics: Performs statistical analysis
        analyze: Performs analysis from methods from `statistics()` method.
        plots: Generates plots for data.
        add_data: For adding additional data to dataset after original dataset has already been set.

    Inheritance:
        PipelineBase: Base class for all types of pipelines.

    """

    def __init__(self) -> None:
        self.data = None
        self._index = 0

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return ObjIterator(self.data)

    def add_data(self, data: DataFrame | Series = None):
        self.data.append(data)

    @abstractmethod
    def statistics(self):
        pass

    @abstractmethod
    def analyze(self):
        pass

    @abstractmethod
    def plots(self):
        pass
