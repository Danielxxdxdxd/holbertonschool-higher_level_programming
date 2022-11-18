#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    data_base = MySQLdb.connect(host='localhost', user=argv[1],
                                password=argv[2], database=argv[3])

    cursor = data_base.cursor()

    cursor.execute('SELECT * FROM states WHERE name LIKE BINARY "N%"')

    data_rows = cursor.fetchall()

    for data in data_rows:
        print(data)
