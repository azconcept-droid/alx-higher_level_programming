#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states table
and write out the safe form
that is safe from MySQL injections!
"""

import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    # Connecting to database and getting database object
    mydb = mysql.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # Creating a cursor object for multiple connections
    cur = mydb.cursor()
    # Pass command to mysql
    cur.execute("SELECT * FROM states \
                WHERE states.name=%(name_state)s\
                ORDER BY states.id ASC", {"name_state": argv[4]})
    # Fetch all results of executed queries
    rows = cur.fetchall()
    # Print out each rows line by line
    for row in rows:
        print(row)

    # Disconnect cursor and close database
    cur.close()
    mydb.close()
