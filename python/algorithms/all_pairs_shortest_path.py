def all_pairs_shortest_path(graph):
    numNodes = len(graph)
    matrix = [[None for x in xrange(numNodes)] for y in xrange(numNodes)]
    path = [[None for x in xrange(numNodes)] for y in xrange(numNodes)]

    for node in graph:
        for edge in graph[node]:
            matrix[node - 1][edge - 1] = graph[node][edge]
            path[node - 1][edge - 1] = node

    k = 1
    while k <= numNodes:
        for node in graph:
            for edge in graph:
                current = matrix[node - 1][edge - 1]
                n_to_k = matrix[node - 1][k - 1]
                k_to_e = matrix[k - 1][edge - 1]
                if n_to_k is not None and k_to_e is not None:
                    if current is None or current > n_to_k + k_to_e:
                        matrix[node - 1][edge - 1] = n_to_k + k_to_e
                        path[node - 1][edge - 1] = k
        k += 1

    return matrix, path


def main():
    graph = {
        1: {
            1: 0,
            2: 3,
            3: 8,
            5: -4
        },
        2: {
            2: 0,
            4: 1,
            5: 7
        },
        3: {
            2: 4,
            3: 0
        },
        4: {
            1: 2,
            3: -5,
            4: 0
        },
        5: {
            4: 6,
            5: 0
        }
    }
    matrix, path = all_pairs_shortest_path(graph)

    for row in matrix:
        print row
    print ""
    for row in path:
        print row

if __name__ == '__main__':
    main()