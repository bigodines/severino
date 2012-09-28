import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'severino'))
from severino.app.compare import compare

class testCompare(unittest.TestCase):

    def setUp(self):
        self.compare = compare.Compare()

    def test_compare_equal_images(self):
        img_a = 'test/resources/equal_a.png'
        img_b = 'test/resources/equal_b.png'

        result = self.compare.are_equal(img_a, img_b)

        self.assertTrue(result)

    def test_compare_different_images(self):
        img_a = 'test/resources/equal_a.png'
        img_b = 'test/resources/different.png'

        result = self.compare.are_equal(img_a, img_b)

        self.assertFalse(result)

    def test_compare_slightly_different_images(self):
        img_a = 'test/resources/equal_a.png'
        img_b = 'test/resources/almost_equal.png'

        result = self.compare.are_equal(img_a, img_b)

        self.assertFalse(result)


    def test_compare_not_so_slightly_different_images(self):
        img_a = 'test/resources/equal_a.png'
        img_b = 'test/resources/almost_equal_b.png'

        result = self.compare.are_equal(img_a, img_b)

        self.assertFalse(result)

    def test_compare_should_be_able_to_compare_identical_directories(self):
        dir_a = 'test/resources/'
        dir_b = 'test/resources/'

        result = self.compare.directories(dir_a, dir_b)

        self.assertEqual([], result)

    def test_compare_should_accept_wildcards_in_dir_comparison(self):
        dir_a = 'test/resources/equal*.png'
        dir_b = 'test/resources/*.png'

        result = self.compare.directories(dir_a, dir_b)

        self.assertEqual(['almost_equal.png', 'almost_equal_b.png', 'different.png'], result)


if __name__ == "__main__":
    print "Please run with 'make tests' from Severino root directory"
