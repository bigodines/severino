import argparse
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

    def last_good(self):
        if self.storage.is_valid():
            return self.storage.last_good()

    def check(self, revision=None):
        if self.storage.is_valid() == False or revision == None:
            return False

        all = self.storage.get(revision)
        return all[2] == 1

    def remove_db(self):
        os.remove(self.db_path)



## creates a new  severino instance based on CL parameters ##
def start_severino(args={}):
    base = current = None
    if args.base != None:
        base = args.base

    if args.current != None:
        current = args.current

    sev = Severino(base, current)

    if args.no_compare == False:
        sev.compare()

    if args.last_good == True:
        print sev.last_good()
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Severino compares screenshots to detect differences')
    parser.add_argument('-b', '--base', 
                        metavar='revision',
                        help="Sets a new base version to be used as comparison parameter (latest 'good' as default)")
    parser.add_argument('-c', '--current', 
                        metavar='revision',
                        help="Defines a directory (revision name) to be compared against --base (default will take new screenshots)")
    parser.add_argument('-no-cmp', '--no_compare', 
                        action='store_false',
                        help="Do not compare, just take screenshots")
    parser.add_argument('-last','--last_good', 
                        action='store_false',
                        help="Returns the latest 'good' revision")
    parser.add_argument('-flag','--flag', 
                        help='Flag revision R as good/bad')


    args = parser.parse_args()

    start_severino(args)


