#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 7)

Write a script that lists all State objects from the database hbtn_0e_6_usa

 * Your script should take 3 arguments:
    mysql username, mysql password and database name

 * You must use the module SQLAlchemy

 * You must import State and Base from model_state
   from model_state import Base, State

 * Your script should connect to a MySQL server
    running on localhost at port 3306

 * Results must be sorted in ascending order by states.id

 * Your code should not be executed when imported
 """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, dbname):
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
        states = session.query(State).order_by(State.id.asc()).all()

        # Print each state
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    # Get command-line arguments
    username, password, dbname = sys.argv[1:]

    # Call the main function with the arguments
    list_states(username, password, dbname)
