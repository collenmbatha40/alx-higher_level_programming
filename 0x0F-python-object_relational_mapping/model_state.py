#!/usr/bin/python3

"""Write a python file that contains the class definition 
of a State and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """defines a class state that links to the states table
    with class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
