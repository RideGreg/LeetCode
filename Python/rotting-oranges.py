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
    def orangesRotting(self, grid): # USE THIS: a little more spaces to store time on each queue entry, but solid w/o bugs
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(grid), len(grid[0])

        fresh = 0
        q = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    q.append((r, c, 0))
                elif val == 1:
                    fresh += 1

        time = 0
        while q:
            r, c, time = q.popleft()
            for d in directions:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc, time+1))
        return time if fresh == 0 else -1


    def orangesRotting(self, grid): # easy to have a bug
        m, n = len(grid), len(grid[0])
        q, fresh = deque(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    
        time = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                i, j = q.popleft()
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        q.append((ni, nj))
            if q:         # it is a bug if missing this 'if'
                time += 1
        return -1 if fresh > 0 else time

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
