# Time:  O(m * n)
# Space: O(n)

# 583
# Given two words word1 and word2,
# find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.
#
# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.

class Solution(object):
    # DP: 状态转移方程：
    #
    # dp[x][y] = x + y     if x == 0 or y == 0
    # dp[x][y] = dp[x - 1][y - 1]     if word1[x] == word2[y]
    # dp[x][y] = min(dp[x - 1][y], dp[x][y - 1]) + 1     otherwise
    #
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n+1))
        for i in range(m):
            ndp = [i+1] + [0]*n
            for j in range(n):
                if word1[i] == word2[j]:
                    ndp[j+1] = dp[j]
                else:
                    ndp[j+1] = min(ndp[j], dp[j+1]) + 1
            dp = ndp
        return dp[-1]

    # 最长公共子序列（Longest Common Subsequence）
    #
    # 求word1和word2的LCS
    # ans = len(word1) + len(word2) - 2 * len(LCS)
    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def lcs(word1, word2):
            len1, len2 = len(word1), len(word2)
            dp = [[0] * (len2 + 1) for x in range(len1 + 1)]
            for x in range(len1):
                for y in range(len2):
                    if word1[x] == word2[y]:
                        dp[x + 1][y + 1] = dp[x][y] + 1
                    else:
                        dp[x + 1][y + 1] = max(dp[x][y + 1], dp[x + 1][y])
            return dp[len1][len2]

        return len(word1) + len(word2) - 2 * lcs(word1, word2)

