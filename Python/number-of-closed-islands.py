# Time:  O(m * n)
# Space: O(1)

# 1254 weekly contest 162 11/9/2019
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally
# connected group of 0s and a closed island is an island totally (all left, top, right, bottom)
# surrounded by 1s.
#
# Return the number of closed islands.


class Solution(object):
    def closedIsland(self, grid):  # USE THIS
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(stack):
            while stack:
                i, j = stack.pop()
                grid[i][j] = 1
                for di, dj in dirs:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0:
                        stack.append((i2, j2))

        stack, m, n, ans = [], len(grid), len(grid[0]), 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # clean land cells connecting to border
        for r in (0, m - 1):  # top and bottom row
            for c in range(n):
                if grid[r][c] == 0:
                    stack.append((r, c))
        for c in (0, n - 1):  # left and right column
            for r in range(1, m - 1):
                if grid[r][c] == 0:
                    stack.append((r, c))
        dfs(stack)

        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    dfs([(r, c)])
                    ans += 1
        return ans


    def closedIsland_kamyu(self, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def fill(grid, i, j):
            if not (0 <= i < len(grid) and 
                    0 <= j < len(grid[0]) and 
                    grid[i][j] == 0):
                return False
            grid[i][j] = 1
            for dx, dy in directions:
                fill(grid, i+dx, j+dy)
            return True

        for j in xrange(len(grid[0])):
            fill(grid, 0, j)
            fill(grid, len(grid)-1, j)
        for i in xrange(1, len(grid)):
            fill(grid, i, 0)
            fill(grid, i, len(grid[0])-1)
        result = 0
        for i in xrange(1, len(grid)-1):
            for j in xrange(1, len(grid[0])-1):
                if fill(grid, i, j):
                    result += 1
        return result

print(Solution().closedIsland([
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]]
)) # 2

print(Solution().closedIsland([
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]])) # 1

print(Solution().closedIsland([
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,0,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]])) # 2
