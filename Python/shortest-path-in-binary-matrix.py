# Time:  O(n^2)
# Space: O(n)

# 1091 weekly contest 141 6/15/19
#
# In an N by N square grid, each cell is either empty (0) or blocked (1).
#
# A clear path from top-left to bottom-right has length k if and only if it is composed of cells
# C_1, C_2, ..., C_k such that:
# . Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# . C_1 is at location (0, 0) (ie. has value grid[0][0])
# . C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# . If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
#
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

# BFS


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1),(1, -1)]
        N = len(grid)
        q = [(0, 0)]
        ans = 1
        grid[0][0] = 1
        while q:
            newq = []
            for x, y in q:
                if (x, y) == (N - 1, N - 1):
                    return ans
                for dx, dy in dirs:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < N and 0 <= y2 < N and grid[x2][y2] == 0:
                        newq.append((x2, y2))
                        grid[x2][y2] = 1
            q = newq
            ans += 1
        return -1

print(Solution().shortestPathBinaryMatrix([[0,1],[1,0]])) # 2
print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])) # 4