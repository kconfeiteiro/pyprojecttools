import glob as g
import os

""" for things like sorting, deleting, copying files, and dealing with directories """

class FileSorting:

    def __init__(self, directory: str = ..., filetype: str = ...):
        self.directory = directory
        self.directory_list = os.listdir(self.directory)
        self.filetype = filetype

    def delete_filetype(folder: str = ..., *filetypes):
        # deletes files of specific extension
        directory = os.listdir(folder)
        removed = []
        for file in directory:
            file = os.path.join(folder, file)
            if file.split(".")[-1] in filetypes:
                removed.append(file)
                os.remove(file)

    @classmethod
    def filter(cls, directory: str = None, filetype: str = ..., **kwargs):
        # take in a directory and filter out based on file extensions or dir names
        # used statically or with class instance
        if directory is None: 
            directory = cls.directory
            
        return g.glob(os.path.join(directory, filetype), **kwargs)


class Directories:

    def mkdir(*paths, display: bool = False):
        # creates directories if they don't exist
        for path in paths:
            if not os.path.exists(path):
                os.mkdir(path)
                if display:
                    print(f'Directory created {path}')

    def generate_unique_name(
        filename: str = ..., 
        path: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), # CWD
        copy_pattern: str = 'Run '
        ):

        # FIXME - fix rest argument for path
        # takes a set name (filename) then if that file exists already it will
        # create another with a counter appended to its name
        base_name, ext = os.path.splitext(filename)
        unique_name, counter = filename, 1
        while os.path.exists(os.path.join(path, unique_name)):
            counter += 1
            unique_name = f'{base_name} ({copy_pattern}{counter}){ext}'

        return unique_name, counter


class FileFetching:

    def fetch_all_files(parent_folder: str):
        # returns a list of all files that are part of directory
        target_files = []
        for path, subdirs, files in os.walk(parent_folder):
            for name in files:
                target_files.append(os.path.join(path, name))
        return target_files 
