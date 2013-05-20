from data_structures.queue import Queue


def bfs(adjList, start):
    queue = Queue()
    visited = {}
    pred = {}
    for key in adjList:
        visited[key] = False
        pred[key] = None

    visited[start] = True
    queue.enqueue(start)

    while queue.size > 0:
        vertex = queue.dequeue()
        edges = adjList[vertex]
        for edge in edges:
            if visited[edge] is False:
                visited[edge] = True
                queue.enqueue(edge)
                pred[edge] = vertex

    return pred


def bfsPath(pred, dest):
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
