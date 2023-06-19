#!/usr/bin/python3
""" Rectangle class module"""


import Base from models.base


class Rectangle(Base):
    """class Rectangle(inherits from Base class)"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing of child class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the value of width instance"""
        return self.__width

    @property
    def height(self):
        """Gets the value of height instance"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets new values for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets new values for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets the value of x instance"""
        return self.__x

    @property
    def y(self):
        """Gets the value of y instance"""
        return self.__y

    @x.setter
    def x(self, value):
        """Sets the new value of x instance"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Sets the new value of y instance"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Method that returns the area of the rectangle object
        Return:
           Area of the rectangle object
        """
        return self.width * self.height

    def display(self):
        """Method that prints to stdout the
           Rectangle object with the character '#'
           """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """Method that overrides the str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Method that changed the order of arguments for rectangle object
        Args:
           *args: list of arguments
           **kwargs: Dictionary with arguments
        Return:
           Nothing
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method that returns a dictionary with
           attributes of the object.
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
