def binary_search(sortedList, value):
    length = len(sortedList)

    if length == 1:
        return value == sortedList[0]

    mid = length / 2
    midValue = sortedList[mid]
    if value == midValue:
        return True
    elif value < midValue:
        return binary_search(sortedList[:mid], value)
    elif value > midValue:
        return binary_search(sortedList[mid:], value)


def main():
    pass


if __name__ == '__main__':
    main()