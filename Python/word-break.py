# Time:  O(n * l^2), n is length of string s, l is maxLen of words in dict; 
#                    slice to get substring s[i-l:i] takes l time
# Space: O(n)

# 139
# Given a string s and a dictionary of words dict,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):  # USE THIS: only need to check all s[0:i], no need to
                                       # check every s[i:j]
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not wordDict: return False
        n, dset = len(s), set(wordDict)
        maxLen = max(len(w) for w in dset)

        dp = [False] * (n+1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = any(dp[j-l] and s[j-l:j] in dset \
                        for l in range(1, max(maxLen, j)+1))
        return dp[n]


    def wordBreak_ming(self, s, wordDict): # 2D space
        dset, n = set(wordDict), len(s)
        dp = [[False] * n for _ in range(n)]

        for i in reversed(range(n)):
            for j in range(i, n):
                dp[i][j] = s[i:j + 1] in dset
                if not dp[i][j]:
                    dp[i][j] = any(dp[i][k] and dp[k + 1][j] for k in range(i, j))
        return dp[0][-1]

print(Solution().wordBreak("leetcode", ["leet", "code"])) # True
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) # False
