#!/usr/bin/python3
"""Module that write an object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON format

    Args:
        my_obj (object): object to write
    """

    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
