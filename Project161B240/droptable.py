import sqlite3
con=sqlite3.Connection("DataBase")
cur=con.cursor()

cur.execute('drop table sumex')
con.commit()
