#!/usr/bin/python3
"""
    This module contains the class_to_json method which
    translates a python class to a dict. 
"""


def class_to_json(obj):
    """
        Parameters:
            obj: a Python object to be translated
        Returns:
            dictionary representation of obj attributes
    """
    return obj.__dict__
