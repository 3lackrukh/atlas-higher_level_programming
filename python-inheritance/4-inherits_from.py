#!/usr/bin/python3
"""
    Module checks if object class is a sub-class of user specified class.
"""


def inherits_from(obj, a_class):
    """
        Utilizes the issubclas() built-in method

        Returns:
            True (bool): if the object is an instance of specified class.
            False (bool): if not.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
