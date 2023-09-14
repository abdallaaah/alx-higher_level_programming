#!/usr/bin/python3
""" inheritence tasks"""


def inherits_from(obj, a_class):
    """is sub class or not"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
