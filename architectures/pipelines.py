""" Blueprint for various pipeline algorithms """

from abc import ABC, abstractmethod


class Pipeline(ABC):
    def __new__(cls, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def plot_data(self):
        pass

    @abstractmethod
    def save_results(self):
        pass

    def generate_report(self):
        pass
