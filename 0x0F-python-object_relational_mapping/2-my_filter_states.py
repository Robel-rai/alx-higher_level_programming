#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    # Create the SQL query with the user input
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute the query and fetch all results
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()

    # Print each row of results
    for row in rows:
        print(row)

    # Close cursor and connection to database
    cur.close()
    db.close()
