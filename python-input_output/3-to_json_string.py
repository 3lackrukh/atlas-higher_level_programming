#!/usr/bin/python3
"""
    This module contains the to_json_string method which
    returns the JSON representation of a specified object
"""
import json


def to_json_string(my_obj):
    """
        Parameters:
            my_obj: the object to be serialized into JSON format.

        Returns: Serialized JSON representation of the object.
    """
    return json.dumps(my_obj)
