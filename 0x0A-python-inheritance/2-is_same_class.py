#!/usr/bin/python3
"""
Module for is_same_class method
"""


def is_same_class(obj, a_class):
    """Checks if an object is an exact instance of a class
    """

    if type(obj) == a_class:
        return True
    return False

