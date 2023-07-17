import os


""" for things like sorting, deleting, copying files, and dealing with directories """

class FileSorting:

    def __init__(self, directory: str = ...):
        self.directory = directory
        self.directory_list = os.listdir(self.directory)

    def delete_filetype(folder: str = ..., *filetypes):
        # deletes files of specific extension
        directory = os.listdir(folder)
        removed = []
        for file in directory:
            file = os.path.join(folder, file)
            if file.split(".")[-1] in filetypes:
                removed.append(file)
                os.remove(file)

    def filter(self):
        '''
        take in a directory and filter out based on file extensions or dir
        names
        '''
        pass


class Directories:

    def mkdir(*paths):
        # creates directories if they don't exist
        # takes n amount of dirs
        for path in paths:
            if not os.path.exists(path):
                os.mkdir(path)
                print(f'Directory created {path}')


class FileFetching:

    def fetch_all_files(parent_folder: str):
        # returns a list of all files that are part of directory
        target_files = []
        for path, subdirs, files in os.walk(parent_folder):
            for name in files:
                target_files.append(os.path.join(path, name))
        return target_files 
