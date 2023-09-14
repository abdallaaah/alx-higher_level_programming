#!/usr/bin/python3
""" write empoty class """


class BaseGeometry():
    """hat raises an Exception with the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
