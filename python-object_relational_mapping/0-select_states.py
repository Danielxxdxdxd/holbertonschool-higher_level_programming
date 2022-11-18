#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    """
    Create a connection to the database
    arguments:
        1. server name
        2. database user name
        3. database password
        4. database name
    """
    data_base = MySQLdb.connect(host='localhost', user=argv[1],
                                password=argv[2], database=argv[3])

    """
    Creates a cursor that is capable of
    executing SQL queries on the database
    """
    cursor = data_base.cursor()

    """
    Executing SQL queries on the database
    Takes a SQL query as a string, as an argument
    """
    cursor.execute('SELECT * FROM states')

    """
    Fetch (extraer) the rows of the table and store them in a variable
    The data is store as a Tuple of tuples
    """
    data_rows = cursor.fetchall()

    for data in data_rows:
        print(data)
