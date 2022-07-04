#!/usr/bin/python3
"""lookup Module"""


def lookup(obj):
    """Finds the list of available attributes and methods of an object

    Args:
        obj (object): object class

    Returns:
        A list of attributes and methods of an object
    """

    return (dir(obj))
