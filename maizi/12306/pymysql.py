# -*- coding: utf-8 -*-

import MySQLdb

conn=MySQLdb.connect(host='127.0.0.1',
			port=3306,
			user='root',
			passwd='6junechow9',
			db='test',
			charset='utf8mb4')
cur = conn.cursor()
cur.execute('show tables;')
for i in cur.fetchall():
	print(i)
cur.close()
conn.close()
