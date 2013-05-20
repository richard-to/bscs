import unittest

from random import randint, choice

from algorithms.binary_search import binary_search
from algorithms.sort import *


def randomSequence(num=20, min=0, max=500):
    return [randint(min, max) for i in xrange(num)]


class TestInsertionSort(unittest.TestCase):
    def testInsertionSort(self):
        numlist = randomSequence()
        numfind = choice(numlist)
        result = insertionSort(numlist)
        self.assertTrue(binary_search(result, numfind))

    def testSelectionSort(self):
        numlist = randomSequence()
        numfind = choice(numlist)
        result = selectionSort(numlist)
        self.assertTrue(binary_search(result, numfind))

    def testMergeSort(self):
        numlist = randomSequence()
        numfind = choice(numlist)
        result = mergeSort(numlist)
        self.assertTrue(binary_search(result, numfind))


if __name__ == '__main__':
    unittest.main()