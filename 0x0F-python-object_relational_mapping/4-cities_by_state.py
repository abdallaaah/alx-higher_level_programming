#!/usr/bin/python3
""" execute with join statemt"""
import MySQLdb
import sys


if __name__ == "__main__":
    """ the main"""
    connection_string = {
            'host': 'localhost',
            'user': sys.argv[1],
            'passwd': sys.argv[2],
            'port': 3306,
            'db': sys.argv[3],
            'charset': 'utf8'
            }
    con = MySQLdb.connect(**connection_string)
    cur = con.cursor()
    command = (
            "SELECT c.id,c.name,s.name FROM states AS s "
            "JOIN cities AS c ON c.state_id = s.id "
            "ORDER BY c.id ASC "
            )
    cur.execute(command)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    con.close()
