#!/usr/bin/python3
""" filter states that start with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    """here is main"""
    connection_string = {
            'host': 'localhost',
            'user': sys.argv[1],
            'passwd': sys.argv[2],
            'db': sys.argv[3],
            'port': 3306,
            'charset': 'utf8'
            }
    conn = MySQLdb.connect(**connection_string)
    cur = conn.cursor()
    name = sys.argv[4]
    cur.execute(f"SELECT * FROM states WHERE name='{name}' ORDER BY id ASC")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()
