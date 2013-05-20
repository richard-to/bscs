class HashSC(object):
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.n = 0
        self.load = self.n / size

    def hash(self, num):
        index = num % self.size
        if self.table[index] is None:
            self.table[index] = []
        return index

    def insert(self, num):
        index = self.hash(num)
        self.table[index].append(num)
        self.n += 1

    def find(self, num):
        index = self.hash(num)
        for val in self.table[index]:
            if num == val:
                return True
        return False

    def delete(self, num):
        index = self.hash(num)
        for idx, val in enumerate(self.table[index]):
            if num == val:
                self.table[index].pop(idx)
                self.n -= 1
                return True
        return False


class HashLP(object):
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.n = 0
        self.load = self.n / size

    def hash(self, num):
        index = num % self.size
        if self.table[index] is None:
            self.table[index] = [None, False]
        return index

    def insert(self, num):
        index = self.hash(num)
        if self.table[index][0] is None:
            self.table[index] = [num, True]
        else:
            i = (index + 1) % self.size
            while i != index:
                if self.table[i] is None or self.table[i][0] is None:
                    self.table[i] = [num, True]
                    break
                else:
                    i = (i + 1) % self.size
        self.n += 1

    def find(self, num):
        index = self.hash(num)
        for val in self.table[index]:
            if num == val:
                return True
            else:
                i = (index + 1) % self.size
                while i != index:
                    if self.table[i] is not None and self.table[i][0] == num:
                        return True
                    else:
                        i = (i + 1) % self.size
        return False

    def delete(self, num):
        index = self.hash(num)
        if self.table[index][0] == num:
            self.table[index] = [None, True]
            self.n -= 1
            return True
        else:
            i = (index + 1) % self.size
            while i != index and self.table[i] is not None and self.table[i][1] == True:
                if self.table[i][0] == num:
                    self.table[i] = [None, True]
                    self.n -= 1
                    return True
                else:
                    i = (i + 1) % self.size
        return False