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
        """return the json str represntaion"""

        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save dict to file"""
        json_string = []
        filename = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []
        for obj in list_objs:
            json_string.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(json_string))

    @staticmethod
    def from_json_string(json_string):
        json_list = []
        if json_string is None:
            return []
        else:
            return json.loads(json_string)