#!/usr/bin/python3
"""Module that append a file"""


def append_write(filename="", text=""):
    """Append to a text file UTF-8

    Args:
        filename (str): name of file to append into
        text (str): string to write
    Returns:
         number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        char_added = file.write(text)
        return char_added
