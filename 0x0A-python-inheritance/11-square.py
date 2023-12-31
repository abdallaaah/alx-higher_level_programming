#!/usr/bin/python3
"""how to inherit"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ square inherit from rectagel"""
    def __init__(self, size):
        """ init function"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str function"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
