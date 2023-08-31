#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Class represnt the square attibutes and methods"""

    def __init__(self, size=0):
        """ create new square.
        Args:
        size(int): the size of the sqaure.
        """
        self.__size = size
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

