#!/usr/bin/python3

def no_c(my_string):
    result = ""
    to_be_removed = {"c": "",
                     "C": ""}
    for elem in my_string:
        if elem in to_be_removed:
            result += to_be_removed[elem]
        else:
            result += elem
    return result
