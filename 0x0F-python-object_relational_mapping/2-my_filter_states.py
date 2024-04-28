#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # MySQL connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    tobesearched = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name = '%s' ORDER BY id ASC"

    # Execute SQL query to select all states
    cursor.execute(sql % tobesearched)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
