class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree(object):

    def __init__(self):
        self.clear()

    def isEmpty(self):
        return True if self.root is None else False

    def insert(self, value):
        if self.isEmpty():
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        else:
            raise ValueError("Duplicate values not allowed")

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return None
        elif value == node.value:
            return node.value
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return node
        elif value < node.value:
            node.left = self._remove(node.left, value)
            return node
        elif value > node.value:
            node.right = self._remove(node.right, value)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                replacement = self._findMax(node.left)
                node.value = replacement
                self._remove(node.left, replacement)
                return node

    def findMax(self):
        return self._findMax(self.root)

    def _findMax(self, node):
        if node is None:
            raise ValueError("Cannot find max of empty tree")
        elif node.right is None:
            return node.value
        else:
            return self._findMax(node.right)

    def findMin(self):
        return self._findMin(self.root)

    def _findMin(self, node):
        if node is None:
            raise ValueError("Cannot find min of empty tree")
        elif node.left is None:
            return node.value
        else:
            return self._findMin(node.left)

    def traversePreorder(self):
        numlist = []
        self._traversePreorder(self.root, numlist)
        return numlist

    def _traversePreorder(self, node, numlist):
        if node is not None:
            numlist.append(node.value)
            self._traversePreorder(node.left, numlist)
            self._traversePreorder(node.right, numlist)

    def traverseInorder(self):
        numlist = []
        self._traverseInorder(self.root, numlist)
        return numlist

    def _traverseInorder(self, node, numlist):
        if node is not None:
            self._traverseInorder(node.left, numlist)
            numlist.append(node.value)
            self._traverseInorder(node.right, numlist)

    def traversePostorder(self):
        numlist = []
        self._traversePostorder(self.root, numlist)
        return numlist

    def _traversePostorder(self, node, numlist):
        if node is not None:
            self._traversePostorder(node.left, numlist)
            self._traversePostorder(node.right, numlist)
            numlist.append(node.value)

    def clear(self):
        self.root = None


def main():
    pass


if __name__ == '__main__':
    main()