#!/usr/bin/python3
"""Defines a txt file reading function"""


def read_file(filename=""):
    """Prints the contents of UTF8 txt file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
