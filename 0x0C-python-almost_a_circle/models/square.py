#!/usr/bin/python3
"""square inherit from rectangle"""
from . import rectangle


class Square(rectangle.Rectangle):
    """square class that inherit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(size, size, x, y, id=id)

    def __str__(self):
        """return the human redabile"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"


    @property
    def size(self):
        """return size"""

        return self.__size

    @size.setter
    def size(self, size):
        """sit the size"""

        self.width = size
        self.height = size