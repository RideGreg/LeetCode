# Time:  O(n^2)
# Space: O(n^2)

# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
#
# After, what is the size of the largest island?
# (An island is a 4-directionally connected group of 1s).
#
# Example 1:
#
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s,
# then we get an island with area = 3.
# Example 2:
#
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger,
# only one island with area = 1.
# Example 3:
#
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 1.
#
# Notes:
# - 1 <= grid.length = grid[0].length <= 50.
# - 0 <= grid[i][j] <= 1.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    # union-find
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pj] = pi
                size[pi] += size[pj]

        m, n = len(grid), len(grid[0])
        parent = range(m * n)
        size = [0] * (m * n)
        self.maxSize = 0

        # Set up connected graph.
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    size[i * n + j] = 1
                    if i > 0 and grid[i - 1][j] == 1:
                        union(i * n + j, (i - 1) * n + j)
                    if j > 0 and grid[i][j - 1] == 1:
                        union(i * n + j, i * n + j - 1)
                    self.maxSize = max(self.maxSize, size[i*n+j])

        ans = self.maxSize
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    parentSet = set()
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            parentSet.add(find(x * n + y))
                    ans = max(ans, 1+sum(size[k] for k in parentSet))
        return ans

    # DFS but similar to union-find. For each connected group, fill it with a new value (starting from 2, since 0 and 1 are used)
    # and remember it's size as area[index] = dfs(...).
    def largestIsland2(self, grid):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(r, c, index, grid):
            if not (0 <= r < len(grid) and
                    0 <= c < len(grid[0]) and
                    grid[r][c] == 1):
                return 0
            result = 1
            grid[r][c] = index
            for d in directions:
                result += dfs(r+d[0], c+d[1], index, grid)
            return result

        area = {}
        index = 2
        for r in xrange(len(grid)):
            for c in xrange(len(grid[r])):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index, grid)
                    index += 1

        result = max(area.values() or [0])
        for r in xrange(len(grid)):
            for c in xrange(len(grid[r])):
                if grid[r][c] == 0:
                    seen = set()
                    for d in directions:
                        nr, nc = r+d[0], c+d[1]
                        if not (0 <= nr < len(grid) and
                                0 <= nc < len(grid[0]) and
                                grid[nr][nc] > 1):
                            continue
                        seen.add(grid[nr][nc])
                    result = max(result, 1 + sum(area[i] for i in seen))
        return result


print(Solution().largestIsland([[1,0],[0,1]])) # 3
print(Solution().largestIsland([[1]])) # 1