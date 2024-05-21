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
        """
            Method validates input value is an int.

            Parameters:
                name: parameter name to check.
                value: value to check

            Raises:
                ValueError: if value is not an int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
