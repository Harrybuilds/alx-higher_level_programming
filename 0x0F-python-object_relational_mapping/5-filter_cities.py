import MySQLdb
import sys

# Get command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

try:
    # Establish connection
    connection = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor
    cursor = connection.cursor()

    # Define SQL query
    sql = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    # Execute query with parameterized query
    cursor.execute(sql, (state_name,))

    # Fetch results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    connection.close()

except MySQLdb.Error as e:
    print("MySQL Error:", e)