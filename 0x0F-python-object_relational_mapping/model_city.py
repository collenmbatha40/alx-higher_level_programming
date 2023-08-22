#!/usr/bin/python3

"""
Write a python file that contains the class definition of 
a city and an instance Base = declarative_base()
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """defines a class city that links to the states table
    with class attribute id that represents a column of an auto-generated, 
    unique integer, can’t be null and is a primary key
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
