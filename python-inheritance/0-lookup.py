#!/usr/bin/python3
"""
    Module providing utility method: lookup
"""


def lookup(obj):

    """
        Create a list of object's attributes and methods.

        Parameters:
            obj (object): the object to be examined.

        Returns:
            list: a list of the object's attributes and methods.
    """
    return list(dir(obj))
