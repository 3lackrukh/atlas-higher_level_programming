#!/usr/bin/python3
"""
    Module compares object class with a user specified class.
"""


def is_same_class(obj, a_class):
    """
        Compares types with equality operator

        Returns:
            True (bool): if the object is of specified class.
            False (bool): if not.
    """
    return (type(obj) == a_class)
