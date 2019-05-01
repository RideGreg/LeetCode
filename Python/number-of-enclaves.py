# Time:  O(m * n)
# Space: O(m * n)

# 1020
# Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)
#
# A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.
#
# Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.
#
#
# Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3

class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def dfs(x, y):
            if A[x][y] == 1:
                A[x][y] = 0
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < m and 0 <= ny < n:
                        dfs(nx, ny)

        m, n = len(A), len(A[0])
        for y in range(n):
            dfs(0, y)
            dfs(m - 1, y)
        for x in range(m):
            dfs(x, 0)
            dfs(x, n - 1)

        return sum(A[x][y] == 1 for x in range(m) for y in range(n))
