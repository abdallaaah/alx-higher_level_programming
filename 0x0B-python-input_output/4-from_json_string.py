#!/usr/bin/python3
""" the inverse of the json from json to object """
import json


def from_json_string(my_str):
    """ using load to reverse the json"""
    return json.loads(my_str)
