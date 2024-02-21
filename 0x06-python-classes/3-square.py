#!/usr/bin/python3
"""more hard work in the private attribute"""


class Square:
    """class square with private attribute"""

    def __init__(self, size=0):
        """call the setter method no init form here"""

        self.size = size

    @property
    def size(self):
        """define size as property and return it"""

        return self.__size

    @size.setter
    def size(self, size):
        """set the size with setter for the first time and every time"""

        if int(size) < 0:
            raise ValueError('size must be >= 0')

        elif not isinstance(size, int):
            raise ValueError('size must be an integer')

        else:
            self.__size = size

    def area(self):
        """the area from te gettere"""

        return(self.size ** 2)
