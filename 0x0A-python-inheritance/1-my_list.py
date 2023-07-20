#!/usr/bin/python3
""" Module for MyList class inheriting from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        sortedlist = sorted(self)
        print(sortedlist)

