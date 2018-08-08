# Given two strings, find the longest common subsequence (LCS).
# Your code should return the length of LCS.
#
# Example: For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1
# For "ABCD" and "EACB", the LCS is "AC", return 2.

class Solution(object):
    def LCS(self, a, b):
        m, n = len(a), len(b)
        dp = [[0]*(n+1) for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # SEEMS NOT CORRECT
                if a[i-1] == b[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        return dp[m][n]

print Solution().LCS("ABCD", "EACBXXXX") #2
