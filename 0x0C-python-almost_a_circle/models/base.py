#!/usr/bin/python3
"""OOP is traning for this module"""
import json


class Base:
    """This is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """thie initalize function"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the str represntaion"""

        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save dict to file"""

        if list_objs is None or not list_objs:
            list_objs = []
        filename = cls.__name__ + '.json'
        for obj in list_objs:
            json_string = cls.to_json_string(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(json_string)
