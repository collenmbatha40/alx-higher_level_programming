#!/usr/bin/python3
"""
    Module for class Student.
"""


class Student:
    """
        Class Student that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialize Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Gets dictionary representation of Student class
        """
        return self.__dict__

