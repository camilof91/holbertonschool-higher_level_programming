#!/usr/bin/python3
"""Lists only states from 4 argument"""


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
    
    find=sys.argv[4]
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE '{find}%' ORDER BY id"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        # if row[1] == find:
            print(row)
    
    cursor.close()
    db.close()
