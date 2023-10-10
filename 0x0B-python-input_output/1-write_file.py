#!/usr/bin/python3
""" overwrite function """


def write_file(filename="", text=""):
    """ write with overwrite file"""
    with open(filename, 'w', encoding='utf-8') as f:
        number = f.write(text)
        return number
