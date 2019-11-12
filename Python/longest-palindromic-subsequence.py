# Time:  O(n^2)
# Space: O(n)

# 516
# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
#
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
#
# "cbbd"
# Output:
# 2

class Solution(object):
    def longestPalindromeSubseq(self, s): # USE THIS
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:  # optional, to optimize special case
            return len(s)

        n = len(s)
        dp = [[0] * n for _ in range(2)]
        for i in reversed(range(n)):
            dp[i%2][i] = 1
            for j in range(i + 1, n):
                dp[i%2][j] = max(dp[(i+1)%2][j], dp[i%2][j-1])
                if s[i] == s[j]:
                    dp[i%2][j] = max(dp[i%2][j], dp[(i+1)%2][j-1] + 2)
        return dp[0][n-1]


    # 2D space. If use size to iterate, cannot optimize space.
    def longestPalindromeSubseq2(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[int(i==j) for j in range(n)] for i in range(n)]
        for size in range(2, n+1):
            for i in range(n - size + 1):
                j = i + size - 1
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 2)
        return dp[0][n-1]