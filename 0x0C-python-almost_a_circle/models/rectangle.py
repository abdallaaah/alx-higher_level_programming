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

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0 or width == 0:
            raise ValueError('width must be > 0')

        self.__width = width

    @property
    def height(self):
        """proerty return height"""

        return self.__height

    @height.setter
    def height(self, height):
        """setter to hegiht"""

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0 or height == 0:
            raise ValueError('height must be > 0')

        self.__height = height

    @property
    def x(self):
        """return the x"""

        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif int(x) < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """return the display function of rectangle"""

        for x in range(0, self.__height):
            for y in range(0, self.__width):
                print('#', end='')
            print('')
