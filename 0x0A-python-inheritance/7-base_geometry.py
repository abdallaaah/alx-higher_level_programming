#!/usr/bin/python3
""" write empoty class """


class BaseGeometry():
    """hat raises an Exception with the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
