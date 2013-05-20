import unittest

from data_structures.queue import Queue


class TestQueue(unittest.TestCase):

    def testQueue(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())
        self.assertEqual(0, queue.size)

        queue.enqueue(5)
        self.assertFalse(queue.isEmpty())
        self.assertEqual(1, queue.size)

        queue.enqueue(6)
        self.assertEqual(2, queue.size)

        self.assertEqual(5, queue.dequeue())
        self.assertEqual(1, queue.size)

        self.assertEqual(6, queue.dequeue())
        self.assertEqual(0, queue.size)
        self.assertTrue(queue.isEmpty())

        queue.enqueue(8)
        queue.clear()
        self.assertEqual(0, queue.size)
        self.assertTrue(queue.isEmpty())


if __name__ == '__main__':
    unittest.main()