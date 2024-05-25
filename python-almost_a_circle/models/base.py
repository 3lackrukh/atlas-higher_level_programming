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

    @classmethod
    def save_to_file(cls, list_objs):
        """
            This method writes the JSON string
            representation of list_objs to a file.
        """
        b_list = []
        if list_objs:
            for i in list_objs:
                b_list.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(b_list))

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string == "":
            return []
        else:
            return json.loads(json_string)
