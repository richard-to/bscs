import unittest

from data_structures.hash import *


class TestHash(unittest.TestCase):
    def testHashSC(self):
        hash = HashSC(11)
        self.assertFalse(hash.find(20))
        hash.insert(22)
        self.assertTrue(hash.find(22))
        hash.insert(11)
        self.assertTrue(hash.find(11))
        self.assertFalse(hash.delete(5))
        self.assertTrue(hash.delete(11))
        hash.insert(9)
        self.assertTrue(hash.find(9))

    def testHashLP(self):
        hash = HashLP(11)
        self.assertFalse(hash.find(20))
        hash.insert(22)
        self.assertTrue(hash.find(22))
        hash.insert(11)
        self.assertTrue(hash.find(11))
        self.assertFalse(hash.delete(5))
        self.assertTrue(hash.delete(22))
        hash.insert(9)
        self.assertTrue(hash.find(9))
        hash.insert(0)

if __name__ == '__main__':
    unittest.main()
