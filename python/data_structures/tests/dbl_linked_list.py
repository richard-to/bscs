import unittest

from data_structures.dbl_linked_list import DblLinkedList


class TestDblLinkedList(unittest.TestCase):

    def testIsEmpty(self):
        linkedList = DblLinkedList()
        self.assertTrue(linkedList.isEmpty())

    def testIsEmptyNot(self):
        linkedList = DblLinkedList()
        linkedList.addFirst(2)
        self.assertFalse(linkedList.isEmpty())

    def testClear(self):
        linkedList = DblLinkedList()
        linkedList.addLast(2)
        self.assertFalse(linkedList.isEmpty())
        linkedList.clear()
        self.assertTrue(linkedList.isEmpty())

    def testAddFirst(self):
        linkedList = DblLinkedList()
        linkedList.addFirst(2)
        linkedList.addFirst(3)
        self.assertEqual(2, linkedList.size)
        self.assertEqual(linkedList.getFirst(), 3)
        self.assertEqual(linkedList.getLast(), 2)

    def testAddLast(self):
        linkedList = DblLinkedList()
        linkedList.addLast(2)
        linkedList.addLast(3)
        self.assertEqual(2, linkedList.size)
        self.assertEqual(linkedList.getFirst(), 2)
        self.assertEqual(linkedList.getLast(), 3)

    def testAdd(self):
        linkedList = DblLinkedList()
        linkedList.addLast(2)
        linkedList.addLast(3)
        linkedList.add(1, 5)
        self.assertEqual(3, linkedList.size)
        self.assertEqual(linkedList.getAtIndex(1), 5)

    def testContains(self):
        linkedList = DblLinkedList()
        self.assertFalse(linkedList.contains(2))
        linkedList.addLast(2)
        linkedList.addLast(3)
        linkedList.add(1, 5)
        self.assertFalse(linkedList.contains(1))
        self.assertTrue(linkedList.contains(2))
        self.assertTrue(linkedList.contains(3))
        self.assertTrue(linkedList.contains(5))

    def testRemoveFirst(self):
        linkedList = DblLinkedList()
        linkedList.addLast(2)
        linkedList.addLast(3)
        self.assertEqual(2, linkedList.removeFirst())
        self.assertEqual(1, linkedList.getSize())

    def testRemoveLast(self):
        linkedList = DblLinkedList()
        linkedList.addLast(2)
        linkedList.addLast(3)
        self.assertEqual(3, linkedList.removeLast())
        self.assertEqual(1, linkedList.getSize())

    def testRemove(self):
        linkedList = DblLinkedList()
        linkedList.addLast(2)
        linkedList.addLast(3)
        linkedList.addLast(5)
        self.assertEqual(5, linkedList.remove(5))
        self.assertEqual(2, linkedList.getSize())

    def testRemoveAtIndex(self):
        linkedList = DblLinkedList()
        linkedList.addLast(2)
        linkedList.addLast(3)
        linkedList.addLast(5)
        self.assertEqual(3, linkedList.removeAtIndex(1))
        self.assertEqual(2, linkedList.getSize())


if __name__ == '__main__':
    unittest.main()
