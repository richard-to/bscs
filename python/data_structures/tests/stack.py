import unittest

from data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def testStack(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())

        stack.push(5)
        self.assertFalse(stack.isEmpty())

        stack.clear()
        self.assertTrue(stack.isEmpty())

        stack.push(6)
        self.assertEqual(6, stack.top())
        self.assertEqual(6, stack.pop())
        self.assertTrue(stack.isEmpty())

        stack.push(7)
        stack.push(6)
        stack.push(5)
        self.assertEqual(5, stack.pop())
        self.assertEqual(6, stack.pop())
        self.assertEqual(7, stack.top())

if __name__ == '__main__':
    unittest.main()