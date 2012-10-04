import os
from app.compare import compare
from app.storage import database

class Severino(object): 

    def __init__(self, base=None, current=None, db="app/storage/severino.db", rev=None):
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
        name = self.rev if self.rev != None else self.current

        if result == True:
            self._flag_as_good()
        else:
            self._flag_as_bad()

        return result

    # legibility matters
    def _flag_as_good(self):
        self.flag(self.rev, True)

    def _flag_as_bad(self):
        self.flag(self.rev, False)

    def flag(self, revision, status=False):
        status = 1 if status == True else 0
        if self.storage.is_valid():
            self.storage.create_log(name=revision, status=status)


    def check(self, revision=None):
        if self.storage.is_valid() == False or revision == None:
            return False

        all = self.storage.get(revision)
        print all
        return all[2] == 1


    def remove_db(self):
        os.remove(self.db_path)
