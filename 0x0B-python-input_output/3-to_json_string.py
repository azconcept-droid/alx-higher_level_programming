#!/usr/bin/python3
"""Module that convert object to JSON format"""


def to_json_string(my_obj):
    """Compute the JSON representation of an object (string)

    Args:
        my_obj (object): to convert
    Returns:
         the JSON representation of an object (string):
    """

    json_format = json.dumps(my_obj)
    return json_format
