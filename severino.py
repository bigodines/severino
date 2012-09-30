from app.compare import compare
from app.storage import sqlite3

class Severino(object): 

    def __init__(self, base=None, current=None, db="storage/severino.db"):
        self.base = base
        self.current = current
        self.is_ok = True
        self.storage = sqlite3.Db(db)


    def compare(self, base=None, current=None):
        if base != None: 
            self.base = base
        if current != None:
            self.current = current
        comp = compare.Compare()
        result = comp.directories(self.current, self.base)
        return result


