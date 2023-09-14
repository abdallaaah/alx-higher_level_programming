#!/usr/bin/python3
""" learning more about inhearting """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class inherit from base"""

    def __init__(self, width, height):
        """ the inishtalization funtion"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ return the area """
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
