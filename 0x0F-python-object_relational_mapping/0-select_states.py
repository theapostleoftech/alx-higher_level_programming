#!/usr/bin/python3
"""
This script lists all the states from the database hbtn_0e_0_usa
"""
import MySQLdb as mysqldb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    db = mysqldb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
