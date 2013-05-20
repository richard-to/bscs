class Node(object):
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class Queue(object):

    def __init__(self):
        self.clear()

    def isEmpty(self):
        return True if self.tail is None else False

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.tail = node
            self.head = node
        else:
            self.head.prev = node
            self.head = node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Cannot dequeue on empty stack")
        else:
            if self.head == self.tail:
                self.head = None
            value = self.tail.value
            self.tail = self.tail.prev
            self.size -= 1
            return value

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


def main():
    pass


if __name__ == '__main__':
    main()