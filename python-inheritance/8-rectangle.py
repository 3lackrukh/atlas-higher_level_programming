#!/usr/bin/python3
"""
    This  module defines a BaseGeometry sub-class, Rectangle.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):

    """
        Class represents a Rectangle.

        Attributes:
            width (int): length of the x-axis. Default 0
            height (int): length of the y-axis. Default 0

        Methods:
            area: inherited from BaseGeometry (not implemented)

            integer_validator from BaseGeometry
                - validates input is integer
    """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height