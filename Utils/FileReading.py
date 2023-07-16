import json
from typing import (Literal)

''' For anything realated to reading data from file or directory '''

class FileReading:
    
    def read_txt(filename: str, mode: Literal['r', 'rb'] = 'r', **kwargs):
        # reading a text file
        with open(filename, mode=mode, **kwargs) as file:
            return file.readlines()

    def read_json(filename: str, *args, **kwargs):
        # reading a JSON file
        with open(filename, *args, **kwargs) as f:
            return json.load(f)