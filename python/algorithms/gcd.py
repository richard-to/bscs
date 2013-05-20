def gcd(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return gcd(n, r)


def main():
    pass


if __name__ == '__main__':
    main()
