import argparse
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'severino'))
from severino import severino
from mock import patch
from mock import Mock

class testSeverino(unittest.TestCase):
    
    def test_default_values(self):
        sev = severino.Severino()
        self.assertEqual(True, sev.is_ok)
        self.assertEqual(None, sev.base)
        self.assertEqual(None, sev.current)

# TODO: too tired to patch it now
#    def test_compare_must_be_able_to_override_default_values(self):
        

    def test_severino_should_receive_revision_and_check_differences(self):
        sev = severino.Severino(base="test/resources/good_rev/*", current="test/resources/bad_rev/*")
        sev.compare()
        self.assertTrue(sev.is_ok)

    def test_alternative_sad_path(self):
        sev = severino.Severino(current="./test/resources/bad_rev/*")
        #sev.take_screenshots()
        diffs = sev.compare(base="./test/resources/good_rev/*")
        self.assertEqual(['./test/resources/bad_rev/chrome-yahoo.png'], diffs)


    def test_severino_should_create_database_if_doesnt_exist(self):
        sev = severino.Severino(db="./test.db")
        self.assertTrue(sev.storage.is_valid())
        sev.remove_db()


    def test_severino_should_add_a_new_revision_to_history(self):
        sev = severino.Severino(rev="test_revision", db="./test.db")
        sev._flag_as_good() # this should be called by compare()
        
        self.assertTrue(sev.check("test_revision"))

    def test_storage_should_find_last_good_revision(self):
        sev = severino.Severino(rev="some_revision", db="./test.db")
        sev._flag_as_good() 
        sev.rev = 'good_rev'
        sev._flag_as_good()
        sev.rev = 'bad_rev'
        sev._flag_as_bad()
        
        row = sev.last_good()
        self.assertEquals('good_rev',row[1])

    def test_severino_should_be_able_to_check_against_good_and_bad_revisions(self):
        """
        This test explains the expected behavior if the user adds two revisions with the same name. (It should compare against the latest one) and also guarantees that severino checks for good and bad revisions.
        """
        sev = severino.Severino(base="test/resources/good_rev/*", current="test/resources/good_rev/*", db="./test.db", rev="rev_1")
        sev.compare()
#        self.assertTrue(sev.check(revision="rev_1"))

        sev.compare(current="test/resources/bad_rev/*")
        self.assertFalse(sev.check(revision="rev_1"))

    # mocking Severino
    def test_start_severino_should_interpret_arguments_properly(self):
        with patch('severino.severino.Severino', spec=True) as MockClass:
            MockInstance = Mock()
            MockClass.return_value = MockInstance

            args = Mock()
            args.base=  'foo'
            args.current = 'new_version'
            args.db = None
            args.rev = None
            args.no_compare = False
            args.last_good = False
            args.flag = None
            severino.start_severino(args)

            MockInstance.compare.assert_called_once_with()


    def test_last_good_will_retrieve_last_revision_flagged_as_good(self):
        with patch('severino.severino.Severino', spec=True) as MockClass:
            MockInstance = Mock()
            MockClass.return_value = MockInstance

            args = Mock()
            args.base=  'foo'
            args.current = 'new_version'
            args.db = './test.db'
            args.rev = 'rev_name'
            args.no_compare = True
            args.last_good = True
            args.flag = False
            severino.start_severino(args)

            MockInstance.last_good.assert_called_once_with()
        
