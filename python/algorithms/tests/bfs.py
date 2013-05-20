import unittest

from algorithms.bfs import bfs, bfsPath


class TestBFS(unittest.TestCase):
    def testBFS(self):
        adjList = {
            0: [8],
            1: [3, 7, 9, 2],
            2: [8, 1, 4],
            3: [4, 5, 1],
            4: [2, 3],
            5: [3, 6],
            6: [7, 5],
            7: [1, 6],
            8: [2, 0, 9],
            9: [1, 8],
        }
        pred = bfs(adjList, 2)
        self.assertEqual({0: 8, 1: 2, 2: None, 3: 1, 4: 2, 5: 3, 6: 7, 7: 1, 8: 2, 9: 8}, pred)

        self.assertEqual([], bfsPath(pred, 2))
        self.assertEqual([2, 8], bfsPath(pred, 0))
        self.assertEqual([2, 1, 7], bfsPath(pred, 6))
        self.assertEqual([2], bfsPath(pred, 4))

if __name__ == '__main__':
    unittest.main()