# Time:  O(m * n)
# Space: O(min(m, n))

# 1143
# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none)
# deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
# while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
# If there is no common subsequence, return 0.

# LCS. Similar problems here:
# 1092. Shortest Common Supersequence
# 1062. Longest Repeating Substring
# 516. Longest Palindromic Subsequence

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        dp = [0] * (n+1)
        for i in range(1, m+1):
            ndp = [0]
            for j in range(1, n+1):
                ndp.append(max(ndp[-1], dp[j]))
                if text1[i-1] == text2[j-1]:
                    ndp[j] = max(ndp[j], dp[j-1]+1)
            dp = ndp
        return dp[-1]

    def longestCommonSubsequence_kamyu(self, text1, text2):
        if len(text1) > len(text2):
            return self.longestCommonSubsequence(text2, text1)

        m, n = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(2)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i%2][j] = max(dp[(i+1)%2][j], dp[i%2][j-1])
                if text1[j-1] == text2[i-1]:
                    dp[i%2][j] = max(dp[i%2][j], dp[(i+1)%2][j-1]+1)
        return dp[n%2][-1]

print(Solution().longestCommonSubsequence("abcde", "ace")) # 3
print(Solution().longestCommonSubsequence("abc", "def")) # 0