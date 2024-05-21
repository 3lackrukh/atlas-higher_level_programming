#!/usr/bin/python3
"""
This module contains the from_json_string method which
returns an object represented by a json string.
"""
import json


def from_json_string(my_str):
    """
        Parameters:
            my_str: the json format string to be converted
            to a python object.
        
        Returns: a python object
    """
    return json.loads(my_str)
