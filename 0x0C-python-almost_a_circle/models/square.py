#!/usr/bin/python3
"""square inherit from rectangle"""
from . import rectangle


class Square(rectangle.Rectangle):
    """square class that inherit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the human redabile"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """return size"""

        return self.height

    @size.setter
    def size(self, size):
        """sit the size"""

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update the square from args and if not from kwargs"""

        if args:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.width = kwargs.get('size')
                self.height = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """dicitionry represntaion"""

        dict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y,
        }
        return dict