#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    city_sql = "SELECT cities.name FROM cities\
        INNER JOIN states ON\
            states.id=cities.state_id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"
    state_name = argv[4]
    cur.execute(city_sql, (state_name,))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()