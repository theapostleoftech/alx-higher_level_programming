#!/usr/bin/python3
"""
This script lists all the states from the database hbtn_0e_0_usa
"""
import MySQLdb as mysqldb

# Step 1: Setup database connection
db = mysqldb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="hbtn_0e_0_usa"
    )

# Step 2: Create a cursor using the cursor class
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
