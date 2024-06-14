#!/usr/bin/python3
"""
This script retrieves state information from the `hbtn_0e_0_usa` database based on a provided state name.

**Steps:**

1. **Retrieves Credentials:** Expects four command-line arguments:
   - Username (index 1) to access the database.
   - Password (index 2) for the specified user.
   - Database name (index 3), which should be `hbtn_0e_0_usa`.
   - State name (index 4) to search for (case-sensitive).

2. **Connects to Database:** Establishes a connection to the MySQL database using the provided credentials.

3. **Executes Secure Query:**
   - Prepares a query to select all columns from the `states` table.
   - Filters results where the `name` column matches the provided state name (using a binary comparison for exact matching).
   - Sorts the results by the `id` column in ascending order.
   - Uses parameter binding (`%(name)s`) to prevent SQL injection vulnerabilities.

4. **Fetches and Prints Results:**
   - Retrieves all matching rows from the database.
   - If any rows are found, iterates through them and prints each row's data.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
