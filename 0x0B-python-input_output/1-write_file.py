#!/usr/bin/python3
"""Module that write to a file"""


def write_file(filename="", text=""):
    """Write to a text file UTF-8

    Args:
        filename (str): name of file to write into
        text (str): string to write
    Returns:
         number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:

        return file.write(text)
