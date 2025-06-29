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

    query.execute("SELECT * FROM states ORDER BY id ASC")
    rows = query.fetchall()

    for row in rows:
        print(row)
