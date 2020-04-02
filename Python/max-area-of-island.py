# Time:  O(m * n)
# Space: O(m * n), the max depth of dfs may be m * n

# 695
# Given a non-empty 2D array grid of 0's and 1's,
# an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6. Note the answer is not 11,
# because the island must be connected 4-directionally.
#
# Example 2:
# [[0,0,0,0,0,0,0,0]]
#
# Given the above grid, return 0.
#
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution(object):
    def maxAreaOfIsland(self, grid): # USE THIS: dfs
        ans = 0
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cur = 0
                    stk = [(i,j)]
                    grid[i][j] = 0
                    while stk:
                        x, y = stk.pop()
                        cur += 1  # increment in 1 place, better than multi places
                        for dx, dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]:
                                stk.append((nx, ny))
                                grid[nx][ny] = 0
                    ans = max(ans, cur)
        return ans

    def maxAreaOfIsland_bfs(self, grid):
        import collections
        ans = 0
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cur = 0
                    q = collections.deque([(i,j)])
                    grid[i][j] = 0
                    while q:
                        x, y = q.popleft()
                        cur += 1
                        for dx, dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]:
                                q.append((nx, ny))
                                grid[nx][ny] = 0
                    ans = max(ans, cur)
        return ans

    def maxAreaOfIsland_kamyu(self, grid): # dfs: recursive
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [[-1,  0], [ 1,  0], [ 0,  1], [ 0, -1]]

        def dfs(i, j, grid, area):
            if not (0 <= i < len(grid) and \
                    0 <= j < len(grid[0]) and \
                    grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            area[0] += 1
            for d in directions:
                dfs(i+d[0], j+d[1], grid, area)
            return True

        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                area = [0]
                if dfs(i, j, grid, area):
                    result = max(result, area[0])
        return result

print(Solution().maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
])) # 6