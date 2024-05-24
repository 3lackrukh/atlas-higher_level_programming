#!/usr/bin/python3
"""
    This module defines object class Rectangle
        - Inherits from class Base
"""

from models.base import Base

class Rectangle(Base):

        def __init__(self, width, height, x=0, y=0, id=None):
            super().__init__(id)
            self.__width = None
            self.__height = None
            self.__x = None
            self.__y = None
            

        @property
        def height(self, height):
              return self.__height

        @property
        def width(self, width):
              return self.__width

        @property
        def x(self, x):
              return self.__x

        @property
        def y(self, y):
              return self.__y

        @width.setter
        def width(self, width):
            if isinstance(width, int) and width > 0:
                self.__width = width
            else:
                 raise TypeError("width must be an int > 0")

        @height.setter
        def height(self, height):
            if isinstance(height, int) and height > 0:
                self.__height = height
            else:
                 raise TypeError("height must be an int > 0")

        @x.setter
        def x(self, x):
            if isinstance(x, int) and x > 0:
                  self.__x = x
            else:
                 raise TypeError("x must be an int > 0")

        @y.setter
        def y(self, y):
            if isinstance(y, int) and y > 0:
                  self.__y = y
            else:
                 raise TypeError("y must be an int > 0")