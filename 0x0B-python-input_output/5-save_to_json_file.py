#!/usr/bin/python3
""" wirte the oject file into file"""
import json


def save_to_json_file(my_obj, filename):
    """ save object to text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
