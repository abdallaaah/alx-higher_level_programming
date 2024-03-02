#!/usr/bin/python3
"""square inherit from rectangle"""
from . import rectangle


class Square(rectangle.Rectangle):
    """square class that inherit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """return the human redabile"""
        return f"[Square] {self.id} {self.x}/{self.y} - {self.size}"
