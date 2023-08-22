#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionaryy = a_dictionary.copy()
    for key, value in a_dictionary.items():
        a_dictionaryy[key] = value * 2
    return a_dictionaryy
