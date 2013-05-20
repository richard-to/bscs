def dfs(adjList, start):
    visited = {}
    pred = {}
    for key in adjList:
        visited[key] = False
        pred[key] = None
    visited[start] = True
    rdfs(adjList, start, visited, pred)
    return pred


def rdfs(adjList, vertex, visited, pred):
    edges = adjList[vertex]
    for edge in edges:
        if visited[edge] is False:
            visited[edge] = True
            pred[edge] = vertex
            rdfs(adjList, edge, visited, pred)


def dfsPath(pred, dest):
    prev = pred[dest]
    path = []
    while prev is not None:
        path.append(prev)
        prev = pred[prev]
    path.reverse()
    return path


def main():
    pass


if __name__ == '__main__':
    main()