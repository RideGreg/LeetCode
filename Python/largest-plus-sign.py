# Time:  O(n^2)
# Space: O(n^2)

# 764
# In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the
# given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained
# in the grid? Return the order of the plus sign. If there is none, return 0.
#
# An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms
# of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the
# diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the
# relevant area of the plus sign is checked for 1s.
#
# Order 2:
# 00000
# 00100
# 01110
# 00100
# 00000


# DP: 用O(N^2)的代价求出每一行l2r and r2l的“一字型全1区域”的长度
# 用O(N^2)的代价求出每一列t2b and b2t的“一字型全1区域”的长度
# 遍历取最小值即为“十字形全1区域”的长度

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        lookup = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0
        for i in range(N):
            l = 0
            for j in range(N):
                l = 0 if (i, j) in lookup else l+1
                dp[i][j] = l
            l = 0
            for j in reversed(range(N)):
                l = 0 if (i, j) in lookup else l+1
                dp[i][j] = min(dp[i][j], l)

        for j in range(N):
            l = 0
            for i in range(N):
                l = 0 if (i, j) in lookup else l+1
                dp[i][j] = min(dp[i][j], l)
            l = 0
            for i in reversed(range(N)):
                l = 0 if (i, j) in lookup else l+1
                dp[i][j] = min(dp[i][j], l)
                ans = max(ans, dp[i][j])
        return ans

print(Solution().orderOfLargestPlusSign(5, [[4, 2]])) # 2