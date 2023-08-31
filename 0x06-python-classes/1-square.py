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
