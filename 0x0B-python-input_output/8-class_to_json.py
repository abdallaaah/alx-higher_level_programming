#!/usr/bin/python3
""" from class to json """
import json


def class_to_json(obj):
    """ to json"""
    return obj.__dict__
    
