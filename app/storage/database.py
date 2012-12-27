import sqlite3 
from datetime import datetime

class Lite(object):
    
    def __init__(self, db=None):
        self.db = db


    def is_valid(self):
        self.conn = sqlite3.connect(self.db)
        self.conn.row_factory = sqlite3.Row
        try:
            self.setup()
            return self.conn.execute("select count(*) from sqlite_master where name=?",
                        ("tablename" ,)).fetchone() > 0

        except Exception as e:
            return False


    def setup(self):
        try: 
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("CREATE TABLE history (id INTEGER PRIMARY KEY, name TEXT, status INTEGER, generated DATETIME);")
        except:
            pass

    def create_log(self, name, status):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO history(name, status, generated) VALUES (?, ?, ?)", (name, status, datetime.now()))

    def get(self, revision):
        with self.conn:
            cur = self.conn.cursor()
            return cur.execute("SELECT id, name, status, generated FROM history WHERE name=:revision ORDER BY generated DESC LIMIT 1",{"revision": revision}).fetchone()

    def last_good(self):
        with self.conn:
            cur = self.conn.cursor()
            return cur.execute("SELECT id, name, status, generated FROM history WHERE status = 1 ORDER BY generated DESC LIMIT 1").fetchone()
