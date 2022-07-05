#!/usr/bin/python3
"""Module that convert JSON string to python object"""
import json


def from_json_string(my_str):
    """Compute the python object of a JSON string

    Args:
        my_str (str): JSON string
    Returns:
        an object (Python data structure) represented by a JSON string
    """

    str_format = json.loads(my_str)
    return str_format
