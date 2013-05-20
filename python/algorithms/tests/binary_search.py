import unittest

from algorithms.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def testBaseCaseFound(self):
        self.assertTrue(binary_search([1], 1))

    def testBaseCaseNotFound(self):
        self.assertFalse(binary_search([1], 2))

    def testNormalCase(self):
        self.assertTrue(binary_search([1, 4, 6, 7, 10, 12, 15, 17], 15))

    def testNormalCase2(self):
        self.assertTrue(binary_search([1, 4, 6, 7, 10, 12, 15, 17], 4))

    def testNormalCase3(self):
        self.assertTrue(binary_search([1, 4, 6, 7, 8, 10, 12, 15, 17], 8))


if __name__ == '__main__':
    unittest.main()