# M2: Build a Python tool that automates file organization.
# takes a folder as input, scans the files inside it, identifies files by extension,
# creates appropriate folders automatically, and moves files into their corresponding folders.

import sys
from pathlib import Path

def convert_path_object(folder_path):
    return Path(folder_path)

def check_valid_folder(folder):
    if not folder.exists() or not folder.is_dir():
        print("Invalid folder name.")
        return 0
    return 1

def organize(folder):
    if not check_valid_folder(folder):
        return
    for file in folder.iterdir():
        if file.is_file():
            extension = get_extension(file)
            if not extension:
                extension = "No extension"
            sub_folder_path = make_folder(folder, extension)
            move_to_folder(file, sub_folder_path)

def get_extension(file_path):
    return file_path.suffix[1:]

def make_folder(parent_path, file_extension):
    new_folder_path = parent_path / file_extension
    new_folder_path.mkdir(parents = True, exist_ok = True)
    return new_folder_path

def move_to_folder(file_path, folder_path):
    new_path = folder_path / file_path.name
    # print(new_path)
    file_path.rename(new_path)

def main():
    argc = len(sys.argv)
    if argc == 1:
        print("No parameters provided.")
        return
    for folder_path in sys.argv[1:]:
        organize(convert_path_object(folder_path))

if __name__ == "__main__":
    main()