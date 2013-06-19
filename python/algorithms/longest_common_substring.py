def longest_common_substring(word1, word2):
    matrix = [[0 for x in xrange(len(word1) + 1)] for y in xrange(len(word2) + 1)]
    longest_len = 0
    col = 0
    for w2i in xrange(len(word2)):
        for w1i in xrange(len(word1)):
            if word2[w2i] == word1[w1i]:
                current_len = matrix[w2i + 1][w1i + 1] = matrix[w2i][w1i] + 1
                if current_len > longest_len:
                    longest_len = current_len
                    col = w1i
    return word1[col - longest_len + 1:col + 1]


def main():
    print longest_common_substring("tofoodie", "toody")


if __name__ == '__main__':
    main()