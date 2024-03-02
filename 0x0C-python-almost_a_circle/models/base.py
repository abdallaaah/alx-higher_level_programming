#!/usr/bin/python3
"""OOP is traning for this module"""


class Base:
    """This is the base class"""

    __nb_objects = 1

    def __init__(self, id=None):
        """thie initalize function"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

