from fastapi import FastAPI
import os
import sqlite3

DB_PATH=os.path.join(os.path.dirname(__file__),'expense.db')


app=FastAPI()
def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""
                CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                note TEXT DEFAULT ''
                )
                """)
init_db()
@app.post('/add-expense')
def add_expense(date,amount,category,subcategory="",note=""):
    """ Adds expenses to the database"""
    with sqlite3.connect(DB_PATH) as c:
        cur=c.execute("INSERT INTO expenses (date, amount, category, subcategory, note) VALUES(?,?,?,?,?)",
        (date, amount, category, subcategory, note))
        return{"status": "ok","id":cur.lastrowid}


@app.get('/list-expense')
def list_expense():
    """ List all expenses from the database"""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute ("SELECT id, date, amount, category, subcategory, note FROM expenses ORDER BY id ASC")
        cols=[d[0] for d in cur.description]
        return[dict(zip(cols,r)) for r in cur.fetchall()]
