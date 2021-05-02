#!/usr/bin/python3
'''
This script takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa

'''

from sys import argv
import MySQLdb

if __name__ == "__main__":

    ''' Connect to database '''
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    ''' Create a cursor '''
    cur = conn.cursor()

    ''' Query the database '''
    cur.execute("""SELECT `cities.name`
    FROM `cities`
    JOIN `states` ON cities.state_id=states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC""", (argv[4], ))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
