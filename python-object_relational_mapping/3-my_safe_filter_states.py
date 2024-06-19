#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 3)

Write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.

* should be safe from SQL injections

* Your script should take 4 arguments:
mysql username, mysql password, database name and state name searched
(no argument validation needed)

* You must use the module MySQLdb (import MySQLdb)

* Your script should connect to a MySQL server
running on localhost at port 3306

* You must use format to create the SQL query with the user input

* Results must be sorted in ascending order by states.id

Your code should not be executed when imported
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # prepare SQL query to accept the state_name argument
    query = (
        "SELECT * FROM `states` "
        "WHERE `name` = BINARY '{}' "
        "ORDER BY `id` ASC").format(state_name)

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
