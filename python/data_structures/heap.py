class Heap(object):
    def __init__(self, capacity):
        self.heap = [0] * capacity
        self.size = 0

    def isEmpty(self):
        return True if self.size == 0 else False

    def isFull(self):
        return True if self.size == len(self.heap) else False

    def insert(self, num):
        if self.isFull():
            raise ValueError("Heap full")
        self.heap[self.size] = num
        self.percolateUp(self.size)
        self.size += 1

    def findMin(self):
        return self.heap[0]

    def deleteMin(self):
        min = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap[self.size] = 0
        self.percolateDown(0)
        return min

    def percolateUp(self, hole):
        if hole > 0:
            if hole % 2 == 0:
                parent = (hole - 1) / 2
            else:
                parent = hole / 2
            if self.heap[hole] < self.heap[parent]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[hole]
                self.heap[hole] = temp
                self.percolateUp(parent)

    def percolateDown(self, hole):
        parent = self.heap[hole]
        child1 = 2 * hole + 1
        child2 = child1 + 1

        if child1 < self.size and (child2 >= self.size or self.heap[child1] < self.heap[child2]):
            if parent > self.heap[child1]:
                self.heap[hole] = self.heap[child1]
                self.heap[child1] = parent
                self.percolateDown(child1)
        elif child2 < self.size:
            if parent > self.heap[child2]:
                self.heap[hole] = self.heap[child2]
                self.heap[child2] = parent
                self.percolateDown(child2)

    def buildHeap(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()