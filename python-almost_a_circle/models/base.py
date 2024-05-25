#!/usr/bin/python3
"""
    This module defines class Base.
"""
import json
import os


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

    @classmethod
    def create(cls, **dictionary):
        """
            This method initializes an instance
            of the specified sub-class and
            sets instance attributes from dictionary.
        """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        file_name = f"{cls.__name__}.json"
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as f:
            return [cls.create(**i) for i in cls.from_json_string(f.read())]
