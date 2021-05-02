#!/usr/bin/python3
'''
 SQL Injection...

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
    cur.execute("""SELECT * FROM `states`
    WHERE `name`=(%s) ORDER BY `id` ASC""", (argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
