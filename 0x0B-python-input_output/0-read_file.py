#!/usr/bin/python3
""" this tutorail is how to read file and print to stdout"""


def read_file(filename=""):
    """ function to read from file and print"""
    with open("my_file_0.txt", 'r', encoding="utf-8") as f:
        file = f.read()
        print(file, end='')
