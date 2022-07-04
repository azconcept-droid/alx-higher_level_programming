#!/usr/bin/python3
"""Defines object instance checker"""


def is_kind_of_class(obj, a_class):
    """Check if the object an instance of a class

    Args:
        obj (object): object to confirm
        a_class (class): class to check
    Returns:
        True if the object is an instance of, or
        if the object is an instance of a class
        that inherited from,the specified class
        False if otherwise
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
