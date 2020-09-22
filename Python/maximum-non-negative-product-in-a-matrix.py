# Time:  O(m * n)
# Space: O(n)

# 1594
# You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0),
# and in each step, you can only move right or down in the matrix.
#
# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right
# corner (rows - 1, cols - 1), find the path with the maximum non-negative product. The product of
# a path is the product of all integers in the grid cells visited along the path.
#
# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.
#
# Notice that the modulo is performed after getting the maximum product.

from functools import lru_cache

class Solution(object):
    def maxProductPath(self, grid):
        R, C = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(r, c):
            v = grid[r][c]
            if r == R - 1 and c == C - 1:
                return v, v

            mn, mx = float('inf'), float('-inf')
            # most cells will calculate mn, mx from right and bottom neighbors
            # except last row and last column.
            if r < R - 1:
                mn2, mx2 = dp(r + 1, c)
                mn = min(mn, mn2 * v, mx2 * v)
                mx = max(mx, mn2 * v, mx2 * v)
            if c < C - 1:
                mn2, mx2 = dp(r, c + 1)
                mn = min(mn, mn2 * v, mx2 * v)
                mx = max(mx, mn2 * v, mx2 * v)
            return mn, mx

        ans = dp(0, 0)[1]
        return ans % MOD if ans >= 0 else -1


    # dp with rolling window
    def maxProductPath_kamyu(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        max_dp = [[0]*len(grid[0]) for _ in xrange(2)]
        min_dp = [[0]*len(grid[0]) for _ in xrange(2)]
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if i == 0 and j == 0:
                    max_dp[i%2][j] = min_dp[i%2][j] = grid[i][j]
                    continue
                curr_max = max(max_dp[(i-1)%2][j] if i > 0 else max_dp[i%2][j-1],
                               max_dp[i%2][j-1] if j > 0 else max_dp[(i-1)%2][j])
                curr_min = min(min_dp[(i-1)%2][j] if i > 0 else min_dp[i%2][j-1],
                               min_dp[i%2][j-1] if j > 0 else min_dp[(i-1)%2][j])
                if grid[i][j] < 0:
                    curr_max, curr_min = curr_min, curr_max
                max_dp[i%2][j] = curr_max*grid[i][j]
                min_dp[i%2][j] = curr_min*grid[i][j]
        return max_dp[(len(grid)-1)%2][-1]%MOD if max_dp[(len(grid)-1)%2][-1] >= 0 else -1

print(Solution().maxProductPath([
    [-1,-2,-3],
    [-2,-3,-3],
    [-3,-3,-2]
])) # -1: impossible
print(Solution().maxProductPath([
    [1,-2,1],
    [1,-2,1],
    [3,-4,1]
])) # 8: 1, 1, -2, -4, 1
print(Solution().maxProductPath([
    [1,3],
    [0,-4]
])) # 0: 1, 0, -4
print(Solution().maxProductPath([
    [ 1, 4,4,0],
    [-2, 0,0,1],
    [ 1,-1,1,1]
])) # 2 = 1 * -2 * 1 * -1 * 1 * 1