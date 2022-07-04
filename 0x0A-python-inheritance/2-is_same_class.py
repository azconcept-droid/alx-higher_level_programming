#!/usr/bin/python3
"""Defines an instance of same class"""


def is_same_class(obj, a_class):
    """Check an instance of same class

    Args:
        obj (object): object to confirm
        a_class (class): class to check
    Returns:
        True if obj is an instance of a_class
        False if otherwise
    """

    if type(obj) == a_class:
        return True
    else:
        return False
