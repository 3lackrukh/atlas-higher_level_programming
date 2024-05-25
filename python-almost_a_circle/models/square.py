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
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

    def __str__(self):
        """
            Method overrides inherited __str__ method
            returns the string representation of instance.
        """
        string = f"[Square] ({self.id})"
        string += f" {self.x}/{self.y} - {self.size}"
        return string

    def update(self, *args, **kwargs):
        """
            Method updates instance parameters.
        """
        if args and args is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

     def to_dictionary(self):
        """
            Method constructs and returns:
            a dictionary representation of instance attributes
        """
        s_dict = {}
        s_dict.update({"id": self.id})
        s_dict.update({"size": self.size})
        s_dict.update({"x": self.x})
        s_dict.update({"y": self.y})
        return s_dict
