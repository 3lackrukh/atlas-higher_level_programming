#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 12)

Write a script that changes the name of a State object
from the database hbtn_0e_6_usa

* Your script should take 3 arguments:
    mysql username, mysql password and database name

* You must use the module SQLAlchemy

* You must import State and Base from model_state

* Your script should connect to a MySQL server
    running on localhost at port 3306

* Change the name of the State where id = 2 to New Mexico

* Your code should not be executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(username, password, dbname):
    # Database connection
    cnx = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'

    # Create the engine
    engine = create_engine(cnx, echo=False)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Update the name of the State object with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    # Get command-line arguments
    username, password, dbname = sys.argv[1:]

    # Call the main function with the arguments
    update_state_name(username, password, dbname)
