import json
from typing import (Dict, List, Literal, Union)

import pandas as pd

''' for anything related to saving data (in any format)'''

class DataSaving:
    
    def build_xl(filename: str, df, sheetname: Union[str, List] = 'Main', index=False, **kwargs):
        # writes to an excel sheet
        with pd.ExcelWriter(filename) as writer:
            if type(sheetname) == list:
                for data, sheetname in zip(df, sheetname):
                    data.to_excel(writer, sheet_name=sheetname, index=index, **kwargs)
            else:
                df.to_excel(writer, sheet_name=sheetname, index=index, **kwargs)

        print(f'File has been written to {filename}')

    def write_to_txt(
        filename: str = ...,
        lines: Union[str, List[str]] = ...,
        mode: Literal['w', 'wb', 'a'] = 'w',
        **kwargs,
    ):
        # writes data to text file
        with open(filename, mode=mode, **kwargs) as file:
            if type(lines) == str:
                file.write(lines)
            else:
                for line in lines:
                    file.write(line)
            file.close()

        print(f'File has been written to {filename}')
    
    def write_to_json(filename: str = ..., dict_to_save: Dict = None, mode: Literal['w', 'wb'] = 'w', **kwargs):
        # writes dictionary to json file
        with open(filename, mode) as file:
            json.dump(dict_to_save, file, **kwargs)
        
        print(f'File has been written to {filename}')