# Time:  O(m * n), 深度优先搜索的时间复杂度是 O(V+E)，其中 V是节点数，E是边数。在矩阵中，O(V)=O(mn)，
# O(E) ~= O(4mn) = O(mn)
# Space: O(m * n), 空间复杂度主要取决于缓存和递归调用深度，缓存的空间复杂度是 O(mn)，递归调用深度不会超过 mn。

# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up
# or down. You may NOT move diagonally or move outside of the boundary
# (i.e. wrap-around is not allowed).
#
# Example 1:
#
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
#
# Example 2:
#
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# 1. DFS + Memorization solution. Bottom up.
# 记忆化深度优先搜索
# 将矩阵看成一个有向图，每个单元格对应图的一个*节点*，相邻两个单元格之间存在一条从较小值指向较大值的*有向边*。
# 问题转化成在有向图中寻找最长路径。
# 朴素深度优先搜索，时间复杂度是指数级，必须使用记忆化的方法进行优化。
import collections, itertools
from functools import lru_cache
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        @lru_cache(None)
        def dfs(row, column):
            best = 1
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        if not matrix:
            return 0
        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans

    def longestIncreasingPath_ownMemo(self, matrix):
        def dfs(i, j):
            if not max_lengths[i][j]:
                best = 0
                directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                for d in directions:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        best = max(best, dfs(x, y))
                max_lengths[i][j] = best + 1
            return max_lengths[i][j]

        if not matrix:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        max_lengths = [[0] * n for _ in range(m)]
        for i, j in itertools.product(range(m), range(n)):
                res = max(res, dfs(i, j))

        return res

# 2. 拓扑排序
# 从所有出度为 0的单元格开始广度优先搜索，每一轮搜索都会遍历当前层的所有单元格，更新其余单元格的出度，
# 并将出度变为 0 的单元格加入下一层搜索。当搜索结束时，搜索的总层数即为矩阵中的最长递增路径的长度。
#
    def longestIncreasingPath_topo(self, matrix):
        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][
                        column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))
        return ans

print(Solution().longestIncreasingPath([[9,9,4], [6,6,8], [2,1,1]])) # 4