import unittest
from ..core import compare

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


if __name__ == "__main__":
    print "Please run with 'make tests' from Severino root directory"
