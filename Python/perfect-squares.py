# Time:  O(n * sqrt(n))
# Space: O(n)

# 279
# Given a positive integer n, find the least number of perfect
# square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
# given n = 13, return 2 because 13 = 4 + 9.
#

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        for i in range(1, n+1):
            dp.append(1 + min(dp[-k*k] for k in range(1, int(i**0.5)+1)))
        return dp[n]

print(Solution().numSquares(12)) # 3, 12 = 4+4+4
print(Solution().numSquares(13)) # 2, 13 = 4 + 9