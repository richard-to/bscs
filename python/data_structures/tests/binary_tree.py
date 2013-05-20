import unittest

from data_structures.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def testBinaryTree(self):
        tree = BinaryTree()
        self.assertTrue(tree.isEmpty())

        tree.insert(3)
        self.assertFalse(tree.isEmpty())
        self.assertEqual(3, tree.find(3))

        tree.insert(5)
        tree.insert(9)
        tree.insert(2)
        tree.insert(20)
        self.assertEqual(5, tree.find(5))
        self.assertEqual(2, tree.findMin())
        self.assertEqual(20, tree.findMax())
        self.assertEqual(2, tree.find(2))

        self.assertEqual([3, 2, 5, 9, 20], tree.traversePreorder())
        self.assertEqual([2, 3, 5, 9, 20], tree.traverseInorder())
        self.assertEqual([2, 20, 9, 5, 3], tree.traversePostorder())

        tree.clear()
        self.assertTrue(tree.isEmpty())

    def testBinaryTreeRemove(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(8)
        tree.insert(15)
        tree.insert(6)
        tree.insert(9)
        tree.insert(13)
        tree.insert(25)
        tree.insert(12)
        tree.insert(14)
        tree.insert(20)
        tree.insert(39)

        tree.remove(60)
        tree.remove(0)
        tree.remove(6)
        tree.remove(8)
        self.assertEqual(None, tree.find(6))
        self.assertEqual(None, tree.find(8))
        self.assertEqual([10, 9, 15, 13, 12, 14, 25, 20, 39], tree.traversePreorder())


if __name__ == '__main__':
    unittest.main()