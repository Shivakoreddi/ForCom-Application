import forum_db_connection as fd
import sqlite3

conn = fd.create_connetion("forum.db")
print(conn)
c = conn.cursor()

#c.execute("create table fc_test_user(id integer,name text,userid text,address text)")
c.execute("insert into fc_test_user values(10001,'test_user','testuser@01','ca')")
c.execute("select * from fc_test_user")
print(c.fetchall())
conn.commit()
conn.close()