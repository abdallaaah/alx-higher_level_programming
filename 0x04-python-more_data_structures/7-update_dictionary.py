#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    x = a_dictionary.get(key, 5)
    if x == 5:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
