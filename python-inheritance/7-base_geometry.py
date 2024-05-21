#!/usr/bin/python3
"""
    Module defines a class BaseGeometry
"""


class BaseGeometry:
    """
        Initial prototype for base class geometry
    """

    def area(self):
        """
            Initial prototype of area method.
            not implemented.

            Raises:
                Exception with message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")
