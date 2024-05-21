#!/usr/bin/python3
"""
    Module checks if object class is an instance of user specified class.
"""


def is_kind_of_class(obj, a_class):
    """
        Utilizes the isinstance() built-in method

        Returns:
            True (bool): if the object is an instance of specified class.
            False (bool): if not. 
    """
    return (isinstance(obj, a_class))