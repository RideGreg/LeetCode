# Time:  O(n)
# Space: O(1)

# 552
# Given a positive integer n, return the number of all possible attendance records with length n,
# which will be regarded as rewardable. The answer may be very large, return it after mod 10^9 + 7.
#
# A student attendance record is a string that only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A record is regarded as rewardable if it doesn't
# contain more than one 'A' (absent) or more than two continuous 'L' (late).
#
# Example 1:
# Input: n = 2
# Output: 8
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.
# Note: The value of n won't exceed 100,000.


# DP: 利用dp[n][A][L]表示长度为n，包含A个字符'A'，以L个连续的'L'结尾的字符串的个数。
#
# 状态转移方程：
# dp[n][0][0] = sum(dp[n - 1][0])
# dp[n][0][1] = dp[n - 1][0][0]
# dp[n][0][2] = dp[n - 1][0][1]
# dp[n][1][0] = sum(dp[n - 1][0]) + sum(dp[n - 1][1])
# dp[n][1][1] = dp[n - 1][1][0]
# dp[n][1][2] = dp[n - 1][1][1]
#
# 初始令dp[1] = [[1, 1, 0], [1, 0, 0]]

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        dp = [[1,1,0], [1,0,0]]
        for i in range(2, n+1):
            ndp = [
                [sum(dp[0])%mod, dp[0][0], dp[0][1]],
                [(sum(dp[0])+sum(dp[1]))%mod, dp[1][0], dp[1][1]]
            ]
            dp = ndp
        return sum(map(sum, dp)) % mod