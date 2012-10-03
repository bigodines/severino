import sqlite3 
from datetime import datetime

class Lite(object):
    
    def __init__(self, db=None):
        self.db = db


    def is_valid(self):
        self.conn = sqlite3.connect(self.db)
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

