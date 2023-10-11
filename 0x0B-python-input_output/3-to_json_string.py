#!/usr/bin/python3
""" from object ot json"""
import json


def to_json_string(my_obj):
    """ seralzation means encoding """
    print('type of this object',type(my_obj))
    return json.dumps(my_obj)
