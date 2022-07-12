#!/usr/bin/python3
"""Docs"""
import json

class Base:
    """Docs"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return json.loads(json_string)
