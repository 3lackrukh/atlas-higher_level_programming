#!/usr/bin/python3
"""
Model for the Cities table in a MySQL database.

This module defines a SQLAlchemy model for the 'cities' table
includes a City class
that inherits from a declarative base.

The City class represents a row in the 'cities'
table, with attributes corresponding to columns in the table.

Classes:
    State(Base): Represents a city in the 'cities' table.
    Base: The declarative base class for all models in this application.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city in the 'cities' table.

    Attributes:
        id (int): Auto-incremented primary key.
        name (str): Non-null string maximum length of 128 characters.
        state_id (int): Non-null foreign key to states.id
    """

    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                ForeignKey("states.id"),
                nullable=False)
