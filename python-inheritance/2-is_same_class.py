#!/usr/bin/python3
"""
    Module compares object class with a user specified class.
"""


def is_same_class(obj, a_class):
    """
        Utilizes the isinstance() built-in method

        Returns:
            True (bool): if the object is an instance of specified class.
            False (bool): if not. 
    """
    return (type(obj) == a_class)
