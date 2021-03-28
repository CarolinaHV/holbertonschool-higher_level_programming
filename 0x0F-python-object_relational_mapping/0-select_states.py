#!/usr/bin/python3
'''
This script lists all states from the database hbtn_0e_0_usa

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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
