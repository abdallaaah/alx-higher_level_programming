#!/usr/bin/python3
import MySQLdb
import sys
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, MetaData
from sqlalchemy.orm import Session

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

if __name__ == "__main__":
    """this main make the code excuted when excute not import"""
    main(sys.argv)
