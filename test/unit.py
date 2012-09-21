import unittest
from .. import compare

class testCompare(unittest.TestCase):

    def test_compare_equal_images(self):
        img_a = 'resources/equal_a.png'
        img_b = 'resources/equal_b.png'

        result = compare.are_equal(img_a, img_b)

        self.assertTrue(result)

    def test_compare_different_images(self):
        img_a = 'resources/equal_a.png'
        img_b = 'resources/different.png'

        result = compare.are_equal(img_a, img_b)

        self.assertFalse(result)

    def test_compare_slightly_different_images(self):
        img_a = 'resources/equal_a.png'
        img_b = 'resources/almost_equal.png'

        result = compare.are_equal(img_a, img_b)

        self.assertFalse(result)


    def test_compare_not_so_slightly_different_images(self):
        img_a = 'resources/equal_a.png'
        img_b = 'resources/almost_equal_b.png'

        result = compare.are_equal(img_a, img_b)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
