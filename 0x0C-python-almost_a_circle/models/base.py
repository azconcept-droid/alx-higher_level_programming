#!/usr/bin/python3
"""Base class module"""
import json


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class
        Args:
            id (int): identity of the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries
        Agrs:
            list_dictionaries (list): list dictionaries of parameter
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        json_string
        Args:
            json_string (str): json string of a list of dictionaries
        """
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)
