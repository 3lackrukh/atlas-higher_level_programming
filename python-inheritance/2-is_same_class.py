#!/usr/bin/python3
"""
    Module checks object class against a user specified class.
"""


def is_same_class(obj, a_class):
    """
        Compares types with equality operator

        Returns:
            True (bool): if the object is a specified class.
            False (bool): if not.
    """
    return (type(obj) is a_class)