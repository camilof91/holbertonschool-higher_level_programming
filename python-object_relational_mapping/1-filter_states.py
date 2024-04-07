#!/usr/bin/python3
"""Lists only states that start with the letter N
from the database hbtn_0e_0_usa"""
# Usage: ./0-select_states.py <mysql username> <mysql password> <database name>


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE '[nN]%' ORDER BY id"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()
