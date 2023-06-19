#!/usr/bin/python3

"""Define a class called Rectangle"""


class Rectangle:
    """Initializes a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle dimensions"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the value for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
