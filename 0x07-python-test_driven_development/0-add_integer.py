#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """Function that adds two integer and/or float numbers"""

    if not a or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
