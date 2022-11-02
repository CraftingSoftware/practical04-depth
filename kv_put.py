import json
import os


def put(key, value, filepath):
    """
    Store the key-value pair at the file specified by the filepath.

    Args:
        key: Key to store
        value: Value to store
        filepath: Path to file to store key-value pair
    """
    if not os.path.exists(filepath):
        # Must create file before reading from it
        with open(filepath, "w", encoding="utf8") as file:
            json.dump({}, file)

    # Read data from file as dictionary and set the value of the key in dictionary
    with open(filepath, "r", encoding="utf8") as file:
        data = json.load(file)
        data[key] = value
    # Write the modified dictionary to the file
    with open(filepath, "w", encoding="utf8") as file:
        json.dump(data, file)
