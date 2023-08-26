from typing import (
    Any,
    Literal,
)

import pylint.lint

from ..datahelpers import write_to_txt


""" For directly linting Python files (currently untested) """


class Lint:
    def __init__(self, filepath: str = ...) -> None:
        """For linting a Python script file.

        Args:
                filepath (str, optional): path to file you want to lint. Defaults to ....
        """
        self.filepath = filepath
        self.linting_results = None

    def process(
        self,
        filename: str = None,
        mode: Literal["r", "rb"] = "r",
        exitl: bool = False,
        do_exitl: bool = False,
        reporter: Any = None,
        stdin: Any = ...,
        write_to_text: str = ...,
        *args,
        **kwargs
    ):
        """Processes linting for desired script

        Args:
                filename (str, optional): name of file you want to lint. Defaults to None.
                mode (literal, optional): file reading mode. Defaults to 'r'.
                exitl (bool, optional): see pylint documentation. Defaults to False.
                do_exitl (bool, optional): see pylint documentation. Defaults to False.
                reporter (Any, optional): see pylint documentation. Defaults to None.
                stdin (Any, optional): see pylint documentation. Defaults to ....
                write_to_text (str, optional): option to write results to text. Defaults to ....
        """
        code = Lint.parse_code(filename, mode)
        self.linting_results = pylint.lint.Run(
            ["-"],
            exit=exitl,
            do_exit=do_exitl,
            reporter=reporter,
            stdin=stdin,
            *args,
            **kwargs
        )

        if write_to_text:
            write_to_txt(write_to_text, content=self.linting_results)

    @staticmethod
    def parse_code(filename: str = ..., mode: Literal["r", "rb"] = "r") -> Any:
        """Static function for parsing a Python script

        Args:
                filename (str, optional): name of file to parse. Defaults to ....
                mode (literal, optional): reading mode. Defaults to 'r'.

        Returns:
                Any: parsed file
        """
        with open(filename, mode) as file:
            return file.read(file)
