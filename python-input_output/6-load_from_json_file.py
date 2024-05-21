#!/usr/bin/python3
"""
    This module contains the load_from_json_file method which
    creates a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
        Parameters:
            filename (str): the name of the file to load from.

        Returns:
            my_obj: a python object created from json file.
    """
    with open(filename, "r") as f:
        return json.loads(f.read())
