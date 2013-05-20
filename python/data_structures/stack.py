class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack(object):
    def __init__(self):
        self.clear()

    def isEmpty(self):
        return True if self.head is None else False

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def top(self):
        if self.head is None:
            return None
        else:
            return self.head.value

    def pop(self):
        if self.head is None:
            raise ValueError("Cannot pop from empty list")
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def clear(self):
        self.head = None


def main():
    pass


if __name__ == '__main__':
    main()