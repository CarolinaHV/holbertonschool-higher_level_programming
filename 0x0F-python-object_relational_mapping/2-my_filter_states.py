#!/usr/bin/python3
'''
This Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.

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

    ''' Query the database - list all the rows '''
    cur.execute("""SELECT * FROM states
    WHERE name LIKE '{}'
    ORDER BY id ASC""".format(argv[4]))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
