# utils.py

import os
import logging
from typing import Dict, List

def get_absolute_path(relative_path: str) -> str:
    """Returns the absolute path of a file or directory."""
    return os.path.abspath(relative_path)

def get_current_dir() -> str:
    """Returns the current working directory."""
    return os.getcwd()

def get_logger(name: str) -> logging.Logger:
    """Returns a logger instance with the given name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

def load_json_data(file_path: str) -> Dict:
    """Loads JSON data from a file."""
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_data(file_path: str, data: Dict) -> None:
    """Saves JSON data to a file."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def list_files(directory: str) -> List[str]:
    """Returns a list of files in a directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def list_directories(directory: str) -> List[str]:
    """Returns a list of directories in a directory."""
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]