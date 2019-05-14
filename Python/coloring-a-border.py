# Time:  O(m * n)
# Space: O(m + n)

# 1034
# Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.
#
# Two squares belong to the same connected component if and only if they have the same color and are next to
# each other in any of the 4 directions.
#
# The border of a connected component is all the squares in the connected component that are either 4-directionally
# adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).
#
# Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of
# that square with the given color, and return the final grid.
#
# Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
# Output: [[3, 3], [3, 2]]
#
# Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
# Output: [[1, 3, 3], [2, 3, 3]]
#
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
# Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

import collections


class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        if color == grid[r0][c0]:
            return grid

        lookup, q, borders = {(r0, c0)}, collections.deque([(r0, c0)]), set()
        while q:
            r, c = q.popleft()
            for nr, nc in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                if ((0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and
                        grid[nr][nc] == grid[r][c]):
                    if (nr, nc) not in lookup:
                        lookup.add((nr, nc))
                        q.append((nr, nc))
                else:
                    borders.add((r, c))

        for r, c in borders:
            grid[r][c] = color
        return grid


    # DFS: duplicate code for boarder check which needs to be done before recursion.
    def colorBorder_dfs(self, grid, r0, c0, color):
        def needDye(x, y):
            return not all(0 <= nx < m and 0 <= ny < n and grid[x][y] == grid[nx][ny]
                           for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

        def dfs(x, y):
            if needDye(x, y):
                borders.append((x, y))
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and grid[nx][ny] == grid[x][y]:
                    seen.add((nx, ny))
                    dfs(nx, ny)

        if color == grid[r0][c0]:
            return grid
        m, n = len(grid), len(grid[0])
        seen, borders = {(r0, c0)}, []
        dfs(r0, c0)

        for i, j in borders:
            grid[i][j] = color
        return grid
