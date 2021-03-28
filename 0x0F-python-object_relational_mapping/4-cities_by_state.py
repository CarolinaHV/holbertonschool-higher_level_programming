#!/usr/bin/python3
'''
This script that lists all states with a name starting
with N (upper N) from the database h.

'''

from sys import argv
import MySQLdb

if __name__ == "__main__":

    ''' Connect to database '''
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf-8")

    ''' Create a cursor '''
    cur = conn.cursor()

    ''' Query the database - list all the rows '''
    cur.execute("""SELECT cities.id, cities.name, states.name FROM states 
    JOIN cities ON  cities.states_id = states.id  
    ORDER BY cities.id ASC""")
    
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
