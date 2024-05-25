#!/usr/bin/python3
"""
    This module defines class Base.
"""
import json


class Base:
    """
        Attributes:
            __nb_objects: instance counter
        Methods:
            __init__: initializes instance with
            user supplied id or id from Base instance counter
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            This method returns the JSON string
            representation of list_dictionaries.
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
