#!/usr/bin/python3
"""Read from a file"""


def read_file(filename=""):
    """Reads a text file UTF-8 and print to stdout

    Args:
        filename (str): name of file
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
