# Time:  O(n^3)
# Space: O(n^2)

# 1139 weekly contest 147 7/27/2019

# Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid
# that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        top, left = [a[:] for a in grid], [a[:] for a in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i:
                        top[i][j] = top[i-1][j] + 1
                    if j:
                        left[i][j] = left[i][j-1] + 1
        for l in range(min(m, n), 0 -1):
            for i in range(m-l+1):
                for j in range(n-l+1):
                    if min(top[i+l-1][j],
                           top[i+l-1][j+l-1],
                           left[i][j+l-1],
                           left[i+l-1][j+l-1]) >= l:
                        return l*l
        return 0

print(Solution().largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]])) # 9
print(Solution().largest1BorderedSquare([[1,1,0,0]])) # 1