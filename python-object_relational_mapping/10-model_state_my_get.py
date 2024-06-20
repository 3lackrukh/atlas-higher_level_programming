#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 10)

Write a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa

* Your script should take 4 arguments:
    mysql username, mysql password, database name and state name to search
    (SQL injection free)

* You must use the module SQLAlchemy

* You must import State and Base from model_state

* Your script should connect to a MySQL server
    running on localhost at port 3306

* You can assume you have one record with the state name to search

* Results must display the states.id

* If no state has the name you searched for,
display Not found

* Your code should not be executed when imported
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def state_id_by_name(username, password, dbname, state_name):
    # Database connection
    cnx = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'

    # Create the engine
    engine = create_engine(cnx, echo=False)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Safely query the State object by name
        state = (
            session.query(State)
            .filter(State.name == state_name)
            .one_or_none())

        if state:
            print(state.id)
        else:
            print("Not found")
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    # Get command-line arguments
    username, password, dbname, state_name = sys.argv[1:]

    # Call the main function with the arguments
    state_id_by_name(username, password, dbname, state_name)
