# Time:  O(n^2)
# Space: O(1)

# 892
# On a N * N grid, we place some 1 * 1 * 1 cubes.
#
# Each value v = grid[i][j] represents a tower of v cubes
# placed on top of grid cell (i, j).
#
# Return the total surface area of the resulting shapes.
#
# Example 1:
#
# Input: [[2]]
# Output: 10
# Example 2:
#
# Input: [[1,2],[3,4]]
# Output: 34
# Example 3:
#
# Input: [[1,0],[0,2]]
# Output: 16
# Example 4:
#
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
# Example 5:
#
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
#
# Note:
# - 1 <= N <= 50
# - 0 <= grid[i][j] <= 50

class Solution(object):
    def surfaceArea(self, grid): # USE THIS: minus joint surface, 36 ms
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid)):
                if grid[i][j]:
                    result += 2 + grid[i][j]*4
                if i:
                    result -= min(grid[i][j], grid[i-1][j])*2
                if j:
                    result -= min(grid[i][j], grid[i][j-1])*2
        return result

    # look at 4 neighbors of each cell, add contribution if higher than neighbor. Avoid double count
    # 56 ms
    def surfaceArea2(self, grid):
        n, ans = len(grid), 0
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j]:
                    ans += 2
                    for nx, ny in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                        if 0<=nx<n and 0<=ny<n:
                            nei_val = grid[nx][ny]
                        else:
                            nei_val = 0
                        ans += max(0, grid[i][j]-nei_val)
        return ans

    # add difference between neighboring cells: iterate more times
    def surfaceArea3(self, grid):
        ans = 0
        for row in grid:
            ans += 2*sum(c>0 for c in row)
            rrow = [0]+row+[0]
            ans += sum(abs(rrow[i]-rrow[i+1]) for i in xrange(len(rrow)-1))
        for col in zip(*grid):
            col = (0,)+col+(0,) # KENG: zip's result is tuple which cannot concatenate to list
            ans += sum(abs(col[i]-col[i+1]) for i in xrange(len(col)-1))
        return ans
