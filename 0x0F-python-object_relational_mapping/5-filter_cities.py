#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    # validate input arguments
    if len(argv) != 5:
        print("Usage: ./5-filter_cities.py user passwd database statename")
        exit(1)
    # Connecting to database and getting database object
    mydb = mysql.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # Creating a cursor object for multiple connections
    cur = mydb.cursor()
    # Pass command to mysql
    cur.execute("SELECT cities.name \
                FROM cities \
                JOIN states ON cities.state_id=states.id \
                WHERE states.name=%(states_name)s \
                ORDER BY cities.id ASC;", {"states_name": argv[4]})
    # Fetch all results of executed queries
    cities = cur.fetchall()
    # Print cities on a line that matches the state argument
    show_cities = [city_name for city in cities for city_name in city]
    print(", ".join(show_cities))

    # Disconnect cursor and close database
    cur.close()
    mydb.close()
