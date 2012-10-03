import os
from app.compare import compare
from app.storage import database

class Severino(object): 

    def __init__(self, base=None, current=None, db="storage/severino.db", rev=None):
        self.base = base
        self.current = current
        self.rev = rev
        self.is_ok = True
        self.db_path = db
        self.storage = database.Lite(db)


    def compare(self, base=None, current=None):
        if base != None: 
            self.base = base
        if current != None:
            self.current = current
        comp = compare.Compare()
        result = comp.directories(self.current, self.base)
        return result

    def _flag_as_good(self):
        if self.storage.is_valid():
            self.storage.create_log(name=self.rev, status=1)


    def check(self, revision=None):
        return True


    def remove_db(self):
        os.remove(self.db_path)
