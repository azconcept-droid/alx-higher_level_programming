#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    # validate input arguments
    if len(argv) != 3:
        print("Usage: ./4-cities_by_state.py user passwd database")
        exit(1)
    # Connecting to database and getting database object
    mydb = mysql.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # Creating a cursor object for multiple connections
    cur = mydb.cursor()
    # Pass command to mysql
    cur.execute("SELECT * FROM cities \
                ORDER BY cities.id ASC;")
    # Fetch all results of executed queries
    rows = cur.fetchall()
    # Print out each rows line by line
    for row in rows:
        print(row)

    # Disconnect cursor and close database
    cur.close()
    mydb.close()
