# Time:  O(n^2)
# Space: O(n)

# 1312 weekly contest 170 1/4/2020

# Given a string s. In one step you can insert any character at any index of the string.
#
# Return the minimum number of steps to make s palindrome.
#
# A Palindrome String is one that reads the same backward as well as forward.

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        def longestCommonSubsequence(text1, text2):
            if len(text1) < len(text2):
                return self.longestCommonSubsequence(text2, text1)
            dp = [[0 for _ in range(len(text2)+1)] for _ in range(2)]
            for i in range(1, len(text1)+1):
                for j in range(1, len(text2)+1):
                    dp[i%2][j] = dp[(i-1)%2][j-1]+1 if text1[i-1] == text2[j-1] \
                                 else max(dp[(i-1)%2][j], dp[i%2][j-1])
            return dp[len(text1)%2][len(text2)]

        return len(s)-longestCommonSubsequence(s, s[::-1])


    def minInsertions_ming(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for sz in range(2, n+1):
            for l in range(n-sz+1):
                r = l+sz-1
                dp[l][r] = float('inf')
                if s[l]==s[r]:
                    dp[l][r] = min(dp[l][r], dp[l+1][r-1])
                else:
                    dp[l][r] = min(dp[l][r], 1 + min(dp[l + 1][r], dp[l][r-1]))
        return dp[0][-1]

print(Solution().minInsertions('zzazz'))
print(Solution().minInsertions('mbadm'))
print(Solution().minInsertions('leetcode'))
print(Solution().minInsertions('g'))
print(Solution().minInsertions('no'))