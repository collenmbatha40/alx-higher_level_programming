#!/usr/bin/python3

"""
a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
# import 
import MySQLdb
from sys import argv

# check if script is run in the main program and not imported as a module
if __name__ == "__main__":
    # create database connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
