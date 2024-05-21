#!/usr/bin/python3
"""
    This module contains the save_to_json_file which
    writes a python object to a text file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Parameters:
            my_obj: the python object to be serialized.
            filename (str): the file to write JSON outut to.
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
