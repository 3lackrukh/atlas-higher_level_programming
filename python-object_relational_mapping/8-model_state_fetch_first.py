#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 8)

Write a script that prints the first State object
from the database hbtn_0e_6_usa

 * Your script should take 3 arguments: 
    mysql username, mysql password and database name

 * You must use the module SQLAlchemy

 * You must import State and Base from model_state
   
 * Your script should connect to a MySQL server
    running on localhost at port 3306

 * The state you display must be the first in states.id

 * You are not allowed to fetch all states from the database
    before displaying the result

 * If the table states is empty,
    print Nothing followed by a new line

 * Your code should not be executed when imported
 """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_first_state(username, password, dbname):
    # Database connection
    cnx = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    
    # Create the engine
    engine = create_engine(cnx, echo=False)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    try:
        # Query the first State object, ordered by id
        first_state = session.query(State).order_by(State.id.asc()).first()
        
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    # Get command-line arguments
    username, password, dbname = sys.argv[1:]
    
    # Call the main function with the arguments
    list_first_state(username, password, dbname)
