#!/usr/bin/python3

"""
This is a script that takes in the name
of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    state = cur.execute("SELECT id FROM states WHERE name = %s", (argv[4],))
    state = cur.fetchone()
    cur.execute("SELECT name FROM cities WHERE state_id = %s", state)
    cur.execute("SELECT c.name from cities c JOIN states s on \
                 c.state_id = s.id WHERE s.name = %s", (argv[4],))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
