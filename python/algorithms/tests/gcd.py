import unittest

from algorithms.gcd import gcd


class TestGcd(unittest.TestCase):

    def testGcd(self):
        self.assertEquals(gcd(8, 4), 4)

    def testGcdCase0(self):
        self.assertEquals(gcd(8, 0), 8)

    def testGcdCase1(self):
        self.assertEquals(gcd(8, 3), 1)


if __name__ == '__main__':
    unittest.main()