
def insertionSort(numlist):
    for i in xrange(1, len(numlist)):
        val = numlist[i]
        pos = i - 1
        while pos >= 0 and numlist[pos] > val:
            numlist[pos + 1] = numlist[pos]
            pos -= 1
        numlist[pos + 1] = val
    return numlist


def selectionSort(numlist):
    size = len(numlist)
    for i in xrange(size - 1):
        pos = i
        val = numlist[i]
        for j in xrange(i + 1, size):
            if numlist[j] < numlist[pos]:
                val = numlist[j]
                pos = j
        if i != pos:
            numlist[pos] = numlist[i]
            numlist[i] = val
    return numlist


def mergeSort(numlist):

    def merge(numlist, startL, startRight, lenRight):
        indexL = startL
        indexR = startRight
        endIndexR = startRight + lenRight
        temp = []
        while indexL < startRight and indexR < endIndexR:
            if numlist[indexL] <= numlist[indexR]:
                temp.append(numlist[indexL])
                indexL += 1
            else:
                temp.append(numlist[indexR])
                indexR += 1

        while indexL < startRight:
            temp.append(numlist[indexL])
            indexL += 1

        while indexR < endIndexR:
            temp.append(numlist[indexR])
            indexR += 1

        startIndex = startL
        for val in temp:
            numlist[startIndex] = val
            startIndex += 1

    def split(numlist, start, len):
        if len > 1:
            midLen = len / 2

            split(numlist, start, midLen)
            split(numlist, start + midLen, len - midLen)

            merge(numlist, start, start + midLen, len - midLen)

    split(numlist, 0, len(numlist))

    return numlist


def main():
    pass


if __name__ == '__main__':
    main()