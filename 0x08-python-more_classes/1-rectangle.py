#!/usr/bin/python3
"""real rectangle class """


class Rectangle:
    """ class represent the rectange"""

    def __init__(self, width=0, height=0):
        """ Create a new rectangel
        Args:
        width(int): width of rec
        height(int): height of rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
