#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 14)

Write a script that lists all City objects from the database hbtn_0e_14_usa

 * Your script should take 3 arguments:
    mysql username, mysql password and database name

 * You must use the module SQLAlchemy

 * You must import State and Base from model_state
   from model_state import Base, State

 * Your script should connect to a MySQL server
    running on localhost at port 3306

 * Results must be sorted in ascending order by cities.id

 * Your code should not be executed when imported
 """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def list_cities_by_state(username, password, dbname):
    # Database connection
    cnx = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'

    # Create the engine
    engine = create_engine(cnx, echo=False)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Query all State objects, ordered by id
        cities = (
            session.query(City, State)
            .filter(City.state_id == State.id).all())

        # Print each state
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    # Get command-line arguments
    username, password, dbname = sys.argv[1:]

    # Call the main function with the arguments
    list_cities_by_state(username, password, dbname)
