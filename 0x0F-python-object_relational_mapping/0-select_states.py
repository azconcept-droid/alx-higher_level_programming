#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    # Connecting to database
    mydb = mysql.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # Creating a cursor object for multiple connections
    cur = mydb.cursor()
    # Executing mysql queries
    cur.execute("SELECT * FROM states \
                ORDER BY states.id ASC;")
    # Fetch all results of executed queries
    rows = cur.fetchall()
    # Print out each rows line by line
    for row in rows:
        print(row)

    # Disconnect cursor and close database
    cur.close()
    mydb.close()
