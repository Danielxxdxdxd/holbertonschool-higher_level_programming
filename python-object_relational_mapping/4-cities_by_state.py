#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    data_base = MySQLdb.connect(host='localhost', user=argv[1],
                                password=argv[2], database=argv[3])

    cursor = data_base.cursor()

    cursor.execute("""
                    SELECT
                        cities.id, cities.name, states.name
                    FROM
                        cities
                    INNER JOIN
                        states
                    ON
                        cities.state_id = states.id
                    ORDER BY
                        cities.id
                    """)

    data_rows = cursor.fetchall()

    for data in data_rows:
        print(data)
