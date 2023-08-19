from typing import (
    List,
    TypedDict,
    Union,
)

from pylatex import (
    Document,
    Section,
    Subsection,
    Subsubsection,
)

from custom_str_templates import LongDateFormat
from reports.reportelements import Section, Subsection, Subsubsection


""" For building PDF reports (in LaTeX) """


class StandardReport(Section, Subsection, Subsubsection):
    def __init__(
        self,
        title: str = None,
        author: str = None,
        date: str = f"Report: {LongDateFormat}",
        save_as: str = None,
    ) -> None:
        """Creates a generic report for configurable sections (only sections, subsection, subsubsections, line(s)/paragraph(s), figures, and tables)

        Args:
                title (str, optional): title of document. Defaults to None.
                author (str, optional): author of document. Defaults to None.
                date (_type_, optional): date of creation. Defaults to f'Report: {LongDateFormat}'.
                save_as (str, optional): name to dave file as (omit '.pdf' at end). Defaults to None.
        """
        super().__init__(Document(title), title, author, date)
        self.save_as = save_as

    def save_as(
        self, render_preview: bool = False, clean_tex: bool = False, **kwargs
    ) -> None:
        """Saves generated report as PDF

        Args:
                render_preview (bool, optional): option to preview render (TeX or MikTex is required). Defaults to False.
                clean_tex (bool, optional): option to generate clean TeX language files. Defaults to False.
        """
        self.doc.generate_pdf("report", clean_tex=clean_tex, **kwargs)
        if render_preview:
            self.doc.view()


class DocumentConfigs(TypedDict):
    """Keyword arguments for Document configuration (from https://jeltef.github.io/PyLaTeX/current/pylatex/pylatex.document.html)"""

    default_filepath: str
    documentclass: str
    document_options: Union[str, List[str]]
    fontenc: str
    inputenc: str
    font_size: str
    lmodern: bool
    textcomp: bool
    page_numbers: bool
    indent: bool
    geometry_options: Union[str, List[str]]
    data: List[str]
