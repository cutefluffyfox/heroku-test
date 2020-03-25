from flask import Flask
import sqlite3


app = Flask(__name__)


@app.route('/')
def main_page():
    return 'hello'


@app.route('/data')
def data_page():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    return str(cur.execute('SELECT * FROM test').fetchall())


@app.route('/<username>/<animal>')
def add(username: str, animal: str):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO test(username, animal) VALUES('{username}', '{animal}')")
    con.commit()
    return 'added'


app.run()
