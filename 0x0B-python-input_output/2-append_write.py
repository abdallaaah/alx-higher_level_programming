#!/usr/bin/python3
""" append in file """


def append_write(filename="", text=""):
    """ append to file """
    
    with open(filename, 'a', encoding='utf-8') as f:
        numbers = f.write(text)
        return numbers
