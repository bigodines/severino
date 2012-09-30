import sqlite3 

class Db(object):
    
    def __init__(self, db=None):
        self.db = db


    def is_valid(self):
        try:
            self.conn = sqlite3.connect(self.db)
            self.setup()
            return self.conn.execute("select count(*) from sqlite_master where name=?",
                        ("tablename" ,)).fetchone() > 0

        except Exception as e:
            print e
            return False


    def setup(self):
        try: 
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("CREATE TABLE history (id INTEGER PRIMARY KEY, name TEXT, status INTEGER, generated DATETIME);")
        except:
            pass

        
