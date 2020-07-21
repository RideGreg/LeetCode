# Time:  O(n * l^2), slice to get substring s[i-l:i] takes l time
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
        n = len(s)
        dset = set(wordDict)
        maxLen = max(map(len, dset)) if dset else 0

        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            dp[i] = any(dp[i-l] and s[i-l:i] in dset \
                        for l in range(1, min(i, maxLen)+1))
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

if __name__ == "__main__":
    print Solution().wordBreak("leetcode", ["leet", "code"])
