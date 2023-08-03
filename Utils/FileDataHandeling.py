import json
import os
from typing import (List, Literal, Union)

''' For anything realated to reading data from file or directory '''

class FileReading:

    def read_txt(filename: str, mode: Literal['r', 'rb'] = 'r', **kwargs):
        '''
        read line(s) from a text file

        Args:
        ---
        :filename (string) - name of file you want to read
        :mode (string) - reading mode; 'r' for normal, 'rb' for reading bytes
        :kwargs (Any) - additional arguments for open()
        '''
        with open(filename, mode=mode, **kwargs) as file:
            return file.readlines()

    def read_json(filename: str = ..., *args, **kwargs):
        '''
        reads a JSON file

        Args:
        ---
        :filename (string) - name of file you want to read
        '''
        assert os.path.exists(filename), "File not found"
        with open(filename, *args, **kwargs) as f:
            return json.load(f)

class FileWriting:

    def write_txt(
        save_as: str = ...,
        content: Union[str, List[str]] = ...,
        mode: Literal["w", "wb"] = "w",
        *args,
        **kwargs
    ):
        '''
        writes string or list of string to a text file

        Args:
        ---
        :save_as (string) - filename for file you are writing to
        :content (list or string) - content that you are writing to the file
        :args & :kwargs (Any) - additional arguments for open() function
        '''

        with open(save_as, mode, *args, **kwargs) as file:
            assert (
                type(content) in [list, List[str]],
                "Content is of wrong format, needs to be string or list of string"
            )

            if type(content) == list:
                for line in content:
                    file.write(line)
                    file.write("\n")
            else:
                file.write(content)

