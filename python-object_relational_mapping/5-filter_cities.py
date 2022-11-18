#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    data_base = MySQLdb.connect(host='localhost', user=argv[1],
                                password=argv[2], database=argv[3])

    state_arg = argv[4]

    cursor = data_base.cursor()

    cursor.execute("""
                    SELECT
                        cities.name
                    FROM
                        cities
                    INNER JOIN
                        states
                    ON
                        cities.state_id = states.id
                    WHERE
                        states.name LIKE BINARY %(state)s
                    """, {
                        'state': state_arg
                    })

    data_rows = cursor.fetchall()

    print(', '.join([str(i[0]) for i in data_rows]))
