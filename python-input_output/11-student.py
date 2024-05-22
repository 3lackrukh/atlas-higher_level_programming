#!/usr/bin/python3
"""
    This module defines a python class Student
"""


class Student:
    """
        Attributes:
            - first_name (str)
            - last_name (str)
            - age (int)
        Methods:
            - to_json:
                retrieves dictionary representation of attributes
            - reload_from_json:
                replaces all attributes of instance Student
                with values from a user supplied dictionary
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and not attrs:
            return {}
        if attrs:
            return {k: v for k, v in self.__dict__.items()if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
