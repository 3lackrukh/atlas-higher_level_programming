#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 4)

Write a script that lists all cities from the database hbtn_0e_4_usa

* Your script should take 3 arguments:
mysql username, mysql password and database name

* You must use the module MySQLdb (import MySQLdb)

* Your script should connect to a MySQL server
running on localhost at port 3306

* Results must be sorted in ascending order by cities.id

* You can use only execute() once

"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # prepare SQL query to accept the state_name argument
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM states "
        "INNER JOIN cities "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC")

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
