class Node(object):

    def __init__(self, value, prevNode=None, nextNode=None):
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode


class DblLinkedList(object):

    def __init__(self):
        self.clear()

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return True if self.head is None else False

    def addFirst(self, value):
        node = Node(value)
        if self.isEmpty():
            self.tail = self.head = node
        else:
            node.nextNode = self.head
            self.head.prevNode = node
            self.head = node
        self.size += 1

    def addLast(self, value):
        node = Node(value)
        if self.isEmpty():
            self.tail = self.head = node
        else:
            node.prevNode = self.tail
            self.tail.nextNode = node
            self.tail = node
        self.size += 1

    def add(self, index, value):
        node = Node(value)

        if index < 0 or index > self.size:
            raise ValueError("Index out of bounds")

        if self.isEmpty() and index == 0:
            self.addFirst(value)
        elif index == self.size:
            self.addLast(value)
        else:
            curIndex = 0
            for iterNode in self:
                if curIndex == index:
                    node.prevNode = iterNode.prevNode
                    node.prevNode.nextNode = node
                    node.nextNode = iterNode
                    iterNode.prevNode = node
                    self.size += 1
                    break
                else:
                    curIndex += 1

    def getFirst(self):
        return self.getAtIndex(0)

    def getLast(self):
        index = self.size - 1 if self.size > 0 else 0
        return self.getAtIndex(index)

    def getAtIndex(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of bounds")

        if index == 0:
            return self.head.value
        elif index + 1 == self.size:
            return self.tail.value
        else:
            curIndex = 0
            for iterNode in self:
                if curIndex == index:
                    return iterNode.value
                else:
                    curIndex += 1

    def contains(self, value):
        for iterNode in self:
            if iterNode.value == value:
                return True
        return False

    def getSize(self):
        return self.size

    def removeFirst(self):
        if self.isEmpty():
            raise ValueError("Cannot remove first element from an empty list")

        if self.size == 1:
            value = self.head.value
            self.clear()
            return value
        else:
            value = self.head.value
            newHead = self.head.nextNode
            newHead.prevNode = None
            self.head = newHead
            self.size -= 1
            return value

    def removeLast(self):
        if self.isEmpty():
            raise ValueError("Cannot remove last element from an empty list")

        if self.size == 1:
            value = self.tail.value
            self.clear()
            return value
        else:
            value = self.tail.value
            newTail = self.tail.prevNode
            newTail.nextNode = None
            self.tail = newTail
            self.size -= 1
            return value

    def remove(self, value):
        for iterNode in self:
            if iterNode.value == value:
                prevNode = iterNode.prevNode
                nextNode = iterNode.nextNode

                if prevNode is not None:
                    prevNode.nextNode = nextNode

                if nextNode is not None:
                    nextNode.prevNode = prevNode

                self.size -= 1
                return iterNode.value

    def removeAtIndex(self, index):
        if 0 > index or index >= self.size:
            raise ValueError("Index out of bounds")

        if index == 0:
            return removeFirst()
        elif index + 1 == self.size:
            return removeLast()
        else:
            curIndex = 0
            for iterNode in self:
                if index == curIndex:
                    value = iterNode.value
                    iterNode.prevNode.nextNode = iterNode.nextNode
                    iterNode.nextNode.prevNode = iterNode.prevNode
                    self.size -= 1
                    return value
                else:
                    curIndex += 1

    def __iter__(self):
        self.iterNode = self.head
        return self

    def next(self):
        if self.iterNode == None:
            raise StopIteration
        else:
            curNode = self.iterNode
            self.iterNode = self.iterNode.nextNode
            return curNode


def main():
    pass


if __name__ == '__main__':
    main()