def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        n1 = 1
        n2 = 1
        start = 3
        while start <= n:
            temp = n1 + n2
            n2 = n1
            n1 = temp
            start += 1
        return n1

def main():
    print fib(100)

if __name__ == '__main__':
    main()