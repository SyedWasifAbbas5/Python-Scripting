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
    directory_prefix = input("Enter the directory name prefix: ")
    start_range = int(input("Enter the starting number of the range: "))
    end_range = int(input("Enter the ending number of the range: "))

    if start_range > end_range:
        print("Starting range cannot be greater than ending range.")
    else:
        directories = [f"{directory_prefix}{i}" for i in range(start_range, end_range + 1)]
        create_directories(directories)