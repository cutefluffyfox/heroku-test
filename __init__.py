import sqlite3
from os import listdir, getcwd


def create_database(database='database.db'):
    if database not in listdir(getcwd()):
        with open(database, 'w'):
            pass
    con = sqlite3.connect(database)
    cur = con.cursor()
    tables = {
        'test': ("""
                CREATE TABLE `@table_name@` (
                  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  `username` TEXT NOT NULL,
                  `animal` TEXT NOT NULL);""")
    }
    # creating tables
    for table_name in tables:
        if not cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'").fetchall():
            cur.execute(tables[table_name].replace('@table_name@', table_name))
            con.commit()


def drop_database(database='database.db'):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('DROP TABLE test')
    con.commit()


if __name__ == '__main__':
    create_database()
