# Time:  O(m * n)
# Space: O(m * n)

# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and
# top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right)
# from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#       ~  1   2   2   3  (5) *
#       ~  3   2   3  (4) (4) *
#       ~  2   4  (5)  3   1  *
#       ~ (6) (7)  1   4   5  *
#       ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

from typing import List
from collections import deque
class Solution(object):
    def pacificAtlantic1(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(board, r, c):
            q = deque([(r, c)])
            used = {(r, c)}
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < m and 0 <= y2 < n and heights[x2][y2] <= heights[x][y] and (x2, y2) not in used:
                        if board[x2][y2] == 1:
                            board[r][c] = 1
                            return
                        elif board[x2][y2] == 0:
                            q.append((x2, y2))
                            used.add((x2, y2))
            board[r][c] = -1

        m, n = len(heights), len(heights[0])
        toPacific = [[0] * n for _ in range(m)]
        toPacific[0] = [1] * n  # first row
        for r in range(1, m):  # first column
            toPacific[r][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                bfs(toPacific, r, c)

        toAtlantic = [[0] * n for _ in range(m)]
        toAtlantic[m - 1] = [1] * n  # last row
        for r in range(0, m - 1):  # last column
            toAtlantic[r][n - 1] = 1

        for r in range(m-1):
            for c in range(n-1):
                bfs(toAtlantic, r, c)

        return [[r, c] for r in range(m) for c in range(n) if toPacific[r][c] == toAtlantic[r][c] == 1]

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        PACIFIC, ATLANTIC = 1, 2

        def pacificAtlanticHelper(matrix, x, y, prev_height, prev_val, visited, res):
            if (not 0 <= x < len(matrix)) or \
               (not 0 <= y < len(matrix[0])) or \
               matrix[x][y] < prev_height or \
               (visited[x][y] | prev_val) == visited[x][y]:
                return

            visited[x][y] |= prev_val
            if visited[x][y] == (PACIFIC | ATLANTIC):
                res.append((x, y))

            for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                pacificAtlanticHelper(matrix, x + d[0], y + d[1], matrix[x][y], visited[x][y], visited, res)

        if not matrix:
            return []

        res = []
        m, n = len(matrix),len(matrix[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            pacificAtlanticHelper(matrix, i, 0, float("-inf"), PACIFIC, visited, res)
            pacificAtlanticHelper(matrix, i, n - 1, float("-inf"), ATLANTIC, visited, res)
        for j in range(n):
            pacificAtlanticHelper(matrix, 0, j, float("-inf"), PACIFIC, visited, res)
            pacificAtlanticHelper(matrix, m - 1, j, float("-inf"), ATLANTIC, visited, res)

        return res

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

print(Solution().pacificAtlantic([[1]]))  # [[0, 0]]