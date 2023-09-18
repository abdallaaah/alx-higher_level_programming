#!/usr/bin/python3
""" 0x0C. Python - Almost a circle"""


class Base:
    """ base class of all coming"""
    __nb__objects = 0

    def __init__(self, id=None):
        """ the init file assign id if not none"""
        if id is None:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
        else:
            self.id = id
