# Time:  O(m * n)
# Space: O(m * n)

# 994
# In a given grid, each cell can have one of three values:
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1 instead.

import collections


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(grid), len(grid[0])

        count = 0
        q = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    q.append((r, c, 0))
                elif val == 1:
                    count += 1

        result = 0
        while q:
            r, c, result = q.popleft()
            for d in directions:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    count -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc, result+1))
        return result if count == 0 else -1

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
