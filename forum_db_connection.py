import sqlite3
from sqlite3 import Error

def create_connetion(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)



if __name__=='__main__':
    create_connetion("db/forum.db")

