import unittest

class testSeverino(unittest.TestCase):
    
    def test_severino_should_receive_revision_and_check_differences(self):
        sev = Severino(base="correct")
        self.assertTrue(True)

    def test_happy_path(self):
        sev = Severino(current="wrong")
        sev.take_screenshots()
        diffs = sev.compare(base="correct")
        self.assertNotEqual([], diffs)

