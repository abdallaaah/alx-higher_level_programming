#!/usr/bin/python3
""" here is the implemantiation of add unitest"""


def add_integer(a, b=98):
    """ add integar to add two numbers
    Args:
        a(int): the first number
        b(int): the secind number
        """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    z = int(a) + int(b)
    return z
