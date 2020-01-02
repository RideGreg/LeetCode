# Time:  O(m * n)
# Space: O(m * n)

# 1162 weekly contest 150 8/17/2019
# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell
# such that its distance to the nearest land cell is maximized and return the distance.
#
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1)
# is |x0 - x1| + |y0 - y1|. If no land or water exists in the grid, return -1.

# Note:
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] is 0 or 1

import collections


class Solution(object):
    # USE THIS: modify original matrix, maintain a counter, save space for a new matrix storing distances
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = collections.deque([(i, j) for i in range(len(grid))
                                      for j in range(len(grid[0])) if grid[i][j] == 1])
        if len(q) == len(grid)*len(grid[0]):
            return -1
        level = -1
        while q:
            next_q = collections.deque()
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and \
                        grid[nx][ny] == 0:
                        next_q.append((nx, ny))
                        grid[nx][ny] = 1
            q = next_q
            level += 1
        return level

    def maxDistance_ming(self, grid):
        n = len(grid)
        d = [[float('inf')] * n for _ in range(n)]  # allocate a new matrix to store all distances
        nodes, cur = [], 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    nodes.append((i,j))
                    d[i][j] = cur
        if len(nodes) == n*n: return -1

        ans = 0
        while nodes:
            new, cur = [], cur+1
            for x,y in nodes:
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<n and d[nx][ny]>cur:
                        d[nx][ny] = cur
                        new.append((nx,ny))
                        ans = cur
            nodes = new
        return ans

print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])) # 2
print(Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]])) # 4