import json
import os


def check_file_exists(filepath):
    """
    Check if a file at the specified filepath exists.

    Args:
        filepath: Path to check

    Returns:
        True if file exists, False otherwise
    """
    return os.path.exists(filepath)


def create_empty_file(filepath):
    """
    Create a file with empty JSON.

    Args:
        filepath: Path of file to create
    """
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump({}, file)


def open_file(filepath):
    """
    Open the file specified by the filepath.

    Args:
        filepath: Path of file to open

    Returns:
        File object that represents file at filepath
    """
    return open(filepath, "r", encoding="utf-8")


def get_json(file):
    """
    Get the JSON in a file as a dictionary.

    Args:
        file: File object that contains the JSON

    Returns:
        JSON in the file as a dictionary.
    """
    return json.load(file)


def get(key, data):
    """
    Get the value of the given key in a data dictionary.

    Args:
        key: Key of value to get
        data: Dictionary that holds data

    Returns:
        Value of given key or None if key does not exist
    """
    return data.get(key, None)
