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
    state = (sys.argv[4],)
    command = (
            "SELECT c.name FROM states AS s "
            "JOIN cities AS c ON c.state_id = s.id "
            "WHERE s.name = %s"
            "ORDER BY c.id ASC "
            )
    cur.execute(command, state)
    result = cur.fetchall()
    city = [row[0] for row in result]
    print(', '.join(city))
    cur.close()
    con.close()
