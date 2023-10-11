#!/usr/bin/python3
""" from json file to object """
import json


def load_from_json_file(filename):
    """ form json to object """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
