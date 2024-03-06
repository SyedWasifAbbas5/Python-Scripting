#!/usr/bin/python

import shutil
import os
import sched
import time
import multiprocessing

def backup_files(source_dir, destination_dir):
    try:
        # Create the destination directory if it doesn't exist
        os.makedirs(destination_dir, exist_ok=True)
        
        # Copy files from source to destination
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, os.path.relpath(source_path, source_dir))
                shutil.copy2(source_path, destination_path)  # Copy file with metadata

        print("Backup completed successfully.")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

def perform_backup(source_dir, destination_dir, interval):
    while True:
        backup_files(source_dir, destination_dir)
        time.sleep(interval)

if __name__ == "__main__":
    source_dir = input("Enter the source directory path: ")
    destination_dir = input("Enter the destination directory path for backup: ")
    interval = int(input("Enter the time interval between backups (in seconds): "))

    backup_process = multiprocessing.Process(target=perform_backup, args=(source_dir, destination_dir, interval))
    backup_process.start()
    print("Backup process started in the background.")
