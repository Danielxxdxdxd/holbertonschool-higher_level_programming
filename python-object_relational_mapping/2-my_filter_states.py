#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    data_base = MySQLdb.connect(host='localhost', user=argv[1],
                                password=argv[2], database=argv[3])

    state_arg = argv[4]

    cursor = data_base.cursor()

    cursor.execute('SELECT * FROM states \
                    WHERE name LIKE BINARY "{}"'.format(state_arg))

    data_rows = cursor.fetchall()

    for data in data_rows:
        print(data)
