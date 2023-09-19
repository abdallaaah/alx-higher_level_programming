#!/usr/bin/python3
"""this is will be responsaple to the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ the init function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.size)
