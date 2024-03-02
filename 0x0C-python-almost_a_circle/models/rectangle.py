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
        """Print the Rectangle instance with the character '#'."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """return the string represntaion"""

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """update the rectangle from arguments"""

        if args:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'x' in kwargs:
                self.__x = kwargs.get('x')
            if 'y' in kwargs:
                self.__y = kwargs.get('y')
            if 'width' in kwargs:
                self.__width = kwargs.get('width')
            if 'height' in kwargs:
                self.__height = kwargs.get('height')
