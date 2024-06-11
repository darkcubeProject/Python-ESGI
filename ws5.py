import os
import shutil
import json
from datetime import datetime

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def fichiers_backup(item, destination_backup):
    try:
        if os.path.isfile(item):
            shutil.copy2(item, destination_backup)
            print(f"File {item} backed up successfully.")
        elif os.path.isdir(item):
            shutil.copytree(item, os.path.join(destination_backup, os.path.basename(item)))
            print(f"Directory {item} backed up successfully.")
        else:
            print(f"{item} does not exist.")
    except PermissionError:
        print(f"Permission denied for {item}.")
    except Exception as e:
        print(f"An error occurred while backing up {item}: {e}")

def main():
    config_file = 'config.json'  # Path to your config.json file
    config = load_config(config_file)

    backup_destination = config['destination_backup']

    # Create backup destination directory if it doesn't exist
    if not os.path.exists(backup_destination):
        os.makedirs(backup_destination)

    for item in config['fichiers_backup']:
        fichiers_backup(item, destination_backup)

if __name__ == "__main__":
    main()
