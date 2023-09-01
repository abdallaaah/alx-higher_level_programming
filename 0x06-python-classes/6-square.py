#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Class represnt the square attibutes and methods"""

    def __init__(self, size=0, position=(0, 0)):
        """ create new square.
        Args:
        size(int): the size of the sqaure.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Return my print with #"""
        if self.size == 0:
            print("")
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("_", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def position(self):
        return self.__postion
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


