#!/usr/bin/python3
"""learn how ton inerit"""
from . import base


class Rectangle(base.Base):
    """rectangle which inherit from the base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the innit method"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property return width"""

        return self.__width

    @width.setter
    def width(self, width):
        """setter set x"""

        self.__width = width

    @property
    def height(self):
        """proerty return height"""

        return self.__height

    @height.setter
    def height(self, height):
        """setter to hegiht"""

        self.__height = height

    @property
    def x(self):
        """return the x"""

        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""

        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""

        self.__y = y
