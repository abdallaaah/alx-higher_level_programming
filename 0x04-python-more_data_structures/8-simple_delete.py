#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    x = a_dictionary.get(key, 5)
    if x != 5:
        del a_dictionary[key]
    return a_dictionary
