#!/usr/bin/python3
"""list all states"""
import MySQLdb
import sys


def main(argv):
    """the main to create connection"""
    connection_string = {
            'host': 'localhost',
            'port': 3306,
            'user': argv[1],
            'passwd': argv[2],
            'db': argv[3],
            'charset': 'utf8'
            }
    conn = MySQLdb.connect(**connection_string)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    qury_rows = cur.fetchall()
    for row in qury_rows:
        print(row)
    cur.close
    conn.close


if __name__ == "__main__":
    """this main make the code excuted when excute not import"""
    main(sys.argv)
