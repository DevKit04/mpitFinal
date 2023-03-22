'''

import sqlite3 as sqlt 

con = sqlt.connect('Users.db')
cur = con.cursor()

cur.execute("""
	CREATE TABLE users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		email VARCHAR(255),
		login VARCHAR(255),
		password VARCHAR(255)
	)
""")

con.commit()
cur.close()
con.close()
'''
k = 0

for a in range(0,10):
	for b in range(0,10):
		for c in range(0,10):
			for d in range(0,10):

				if (a+b) == (c+d):
					k+=1

print(k)