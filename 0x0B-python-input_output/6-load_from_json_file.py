#!/usr/bin/python3
"""Module that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file

    Args:
        filename (str): JSON file to load
    """

    with open(filename) as file:
        obj_created = json.load(file)
        return obj_created
