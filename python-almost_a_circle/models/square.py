#!/usr/bin/python3
"""
    This module defines object class Square:
        - inherits from object class Rectangle.
            -- inherits from object class Base.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Initializes instance of Square as instance of Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        self.__width = size
        self.__height = size


    def __str__(self):
        """
            Method overrides inherited __str__ method
            returns the string representation of instance.
        """
        string = f"[Square] ({self.id})"
        string += f" {self.x}/{self.y} - {self.width}"
        return string
