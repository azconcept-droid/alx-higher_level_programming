#!/usr/bin/python3
"""Verify object inheritance direct or indirect"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj (object): object to confirm
        a_class (class): class to check
    Returns:
        True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class
        ; otherwise False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
