#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb as mysql
from sys import argv

name = argv[4]

if __name__ == "__main__":
    # Connecting to database and getting database object
    mydb = mysql.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # Creating a cursor object for multiple connections
    cur = mydb.cursor()
    # Pass command to mysql
    cur.execute("SELECT * FROM states \
                WHERE CONVERT(`name` USING Latin1) \
                COLLATE Latin1_General_CS = '{}';".format(name))
    # Fetch all results of executed queries
    rows = cur.fetchall()
    # Print out each rows line by line
    for row in rows:
        print(row)

    # Disconnect cursor and close database
    cur.close()
    mydb.close()
