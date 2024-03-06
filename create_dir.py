#!/usr/bin/python

import os

def create_directories(directory_names):
    for directory_name in directory_names:
        try:
            os.makedirs(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")

if __name__ == "__main__":
    directories = input("Enter directory names (separated by comma): ").split(",")
    directories = [directory.strip() for directory in directories]
    create_directories(directories)