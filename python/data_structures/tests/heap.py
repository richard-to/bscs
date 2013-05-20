import unittest

from data_structures.heap import *


class TestHeap(unittest.TestCase):
    def testHeap(self):
        heap = Heap(8)
        self.assertTrue(heap.isEmpty())
        self.assertFalse(heap.isFull())

        heap.insert(10)
        heap.insert(16)
        heap.insert(20)
        self.assertEqual([10, 16, 20, 0, 0, 0, 0, 0], heap.heap)

        heap.insert(2)
        self.assertEqual([2, 10, 20, 16, 0, 0, 0, 0], heap.heap)

        heap.insert(8)
        self.assertEqual([2, 8, 20, 16, 10, 0, 0, 0], heap.heap)

        heap.insert(30)
        self.assertEqual([2, 8, 20, 16, 10, 30, 0, 0], heap.heap)
        self.assertEqual(2, heap.findMin())

        heap.insert(1)
        self.assertEqual([1, 8, 2, 16, 10, 30, 20, 0], heap.heap)

        heap.insert(45)
        self.assertEqual([1, 8, 2, 16, 10, 30, 20, 45], heap.heap)
        self.assertEqual(1, heap.findMin())
        self.assertTrue(heap.isFull())
        self.assertFalse(heap.isEmpty())

        self.assertEqual(1, heap.deleteMin())
        self.assertEqual([2, 8, 20, 16, 10, 30, 45, 0], heap.heap)
        self.assertEqual(2, heap.deleteMin())


if __name__ == '__main__':
    unittest.main()