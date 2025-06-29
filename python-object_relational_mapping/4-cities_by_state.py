#!/usr/bin/python3

""" The module """

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    query = db.cursor()

    query.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id ASC
    """)
    rows = query.fetchall()

    for row in rows:
        print(row)
