from abc import (ABC, abstractclassmethod, abstractmethod, abstractproperty,
				 abstractstaticmethod)
from datetime import datetime
from typing import (Any, Callable, Dict, List, Literal, NewType, Tuple, Type,
					TypeVar, Union)

from pylatex import (Alignat, Axis, Document, Figure, Foot, Head, LargeText,
					 LineBreak, Math, Matrix, MediumText, MiniPage, NewPage,
					 PageStyle, Plot, Section, Subsection, Subsubsection,
					 Tabular, TikZ, simple_page_number, Tabular, Command)
from pylatex.utils import italic, NoEscape
from pandas import DataFrame

from Helpers.Dates import LongDateFormat


""" Houses abstract classes and class elements for generated reports """

class ReportBase(ABC):

    def __init__(
        self,
        doc: Document = None,
        title: str = None,
        author: str = None,
        date: str = None
    ) -> None:
        """Base class for subsequent report "generator" classes

        Args:
            doc (Document, optional): 'Document' object instance. Defaults to None.
            title (str, optional): document title. Defaults to None.
            author (str, optional): document author. Defaults to None.
            date (str, optional): current data. Defaults to LongDateFormat (i.e., August 6, 2023).
        """
        self.doc = doc
        self.title = title
        self.author = author
        self.date = date if date else LongDateFormat

        self.doc.preamble.append(Command('author', self.author))
        self.doc.preamble.append(Command('date', NoEscape(self.date)))
        self.doc.append(NoEscape(r'\maketitle'))

        self.num_sections = 0
        self.num_ssections = 0
        self.num_sssections = 0

    def __str__(self):
        return f"Sections: {self.num_sections}; Subsections: {self.num_ssections}; Subsubsections: {self.num_sssections}"

    def __len__(self):
        return self.num_sections + self.num_ssections + self.num_sssections

    @abstractmethod
    def add_line(self, content: str = ...) -> None:
        """Abstract base method for adding lines. Additional functionality to be added

        Args:
            content (str or list or st, optional): line(s)/paragraph(s) you want to add. Defaults to ....
        """
        pass

    def add_image(self, image_path: str = ..., caption: str = ..., width: int = None) -> None:
        """Adds image to document report

        Args:
            image_path (str, optional): path to image. Defaults to ....
            caption (str, optional): caption for image. Defaults to ....
            width (int, optional): width of image (in pixels). Defaults to None.
        """
        with self.doc.create(Figure(position='h!')) as fig:
            fig.add_image(image_path, width=f"{width.strip('.pdf')}")
            fig.add_caption(caption)

    def add_dataframe(self, dataframe: DataFrame = None, caption: str = ...) -> None:
        """Adds table to

        Args:
            dataframe (DataFrame, optional): _description_. Defaults to None.
            caption (str, optional): _description_. Defaults to ....
        """
        with self.doc.create(Section('Table')):
            with self.doc.create(Tabular('c' * len(dataframe.columns))) as table:
                table.add_hline()
                table.add_row(dataframe.columns)
                table.add_hline()
                for _, row in dataframe.iterrows():
                    table.add_row(row)
                    table.add_hline()
            self.doc.append(NoEscape(r'\caption{' + caption + '}'))

    @property
    def sections(self):
        """Returns current number of sections"""
        return self.num_sections()

    @property
    def subsections(self):
        """Returns current number of subsections"""
        return self.num_ssections()

    @property
    def subsubsections(self):
        """Returns current number of subsubsections"""
        return self.num_sssections


class Section(ReportBase):

    def __init__(self, doc: Document = None, title: str = ...) -> None:
        super().__init__(doc, title)
        self.section = self.doc.create(Section(title))

    def add_section(self, title: str = ...) -> None:
        """Adds section to document

        Args:
            title (str, optional): title of new section. Defaults to ....
        """
        self.num_sections += 1
        self.doc.append(Section(title))

    def add_line(self, content: str = ...) -> None:
        """Adds line(s)/paragraph(s) to report

        Args:
            content (str, optional): str or list of str to add. Defaults to ....
        """
        self.section.append(content)


class Subsection(ReportBase):

    def __init__(self, doc: Document = None, title: str = ...) -> None:
        super().__init__(doc, title)
        self.subsection = self.doc.create(Subsection(title))

    def add_subsection(self, title: str = ...) -> None:
        """Adds subsection to document

        Args:
            title (str, optional): title of new subsection. Defaults to ....
        """
        self.num_ssections += 1
        self.doc.append(Subsection(title))

    def add_line(self, content: str = ...) -> None:
        """Adds line(s)/paragraph(s) to report

        Args:
            content (str, optional): str or list of str to add. Defaults to ....
        """
        self.subsection.append(content)


class Subsubsection(ReportBase):

    def __init__(self, doc: Document = None, title: str = ...) -> None:
        super().__init__(doc, title)
        self.subsubsection = self.doc.create(Subsubsection(title))

    def add_subsubsection(self, title: str = ...) -> None:
        """Adds subsubsection to document

        Args:
            title (str, optional): title of new subsubsection. Defaults to ....
        """
        self.num_sssections += 1
        self.doc.append(Subsubsection(title))

    def add_line(self, content: str = ...) -> None:
        """Adds line(s)/paragraph(s) to report

        Args:
            content (str, optional): str or list of str to add. Defaults to ....
        """
        self.subsubsection.append(content)
