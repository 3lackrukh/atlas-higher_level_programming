#!/usr/bin/python3
"""
Model for the States table in a MySQL database.

This module defines a SQLAlchemy model for the 'states' table
includes a State class
that inherits from a declarative base.

The State class represents a row in the 'states'
table, with attributes corresponding to columns in the table.

Classes:
    State(Base): Represents a state in the 'states' table.
    Base: The declarative base class for all models in this application.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a state in the 'states' table.

    Attributes:
        id (int): Auto-incremented primary key.
        name (str): Non-null string maximum length of 128 characters.
    """

    __tablename__ = 'states'

    id = Column(Integer, 
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
