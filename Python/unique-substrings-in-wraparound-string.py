# Time:  O(n)
# Space: O(1)

# 467
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
#
# Now we have another string p. Your job is to find out
# how many unique non-empty substrings of p are present in s.
# In particular, your input is the string p and you need to output
# the number of different non-empty substrings of p in the string s.
#
# Note: p consists of only lowercase English letters and the size of p might be over 10000.
#
# Example 1:
# Input: "a"
# Output: 1
#
# Explanation: Only the substring "a" of string "a" is in the string s.
# Example 2:
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string s.
# Example 3:
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

class Solution(object):
    # 按照子串的结尾字母分类计数
    # 用字典cmap记录以某字母结尾的子串的最大长度（因为只要unique子串，同一字母结尾的非最大长度
    # 子串都会出现在最大长度子串中）
    # 假设连续子串长度为n，符合要求的子串个数为n+(n-1)+...+1，正好等同于
    # 把连续子串中每个字母的长度加在一起
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        import collections
        cmap = collections.defaultdict(int)
        clen = 0
        for i in range(len(p)):
            if i and (ord(p[i])-ord(p[i-1])) % 26 != 1:
                clen = 1
            else:
                clen += 1

            cmap[p[i]] = max(cmap[p[i]], clen)
        return sum(cmap.values())

    # DP: interval O(n^2)
    def findSubstringInWraproundString_LTE(self, p):
        n, ans = len(p), 0
        lookup = {}
        dp = [[False]*n for _ in range(n)]
        for long in range(1, n+1):
            for i in range(n-long+1):
                j = i+long-1
                if p[i:j+1] not in lookup:
                    if i == j:
                        dp[i][j] = True
                        ans += 1
                    else:
                        for k in range(i, j):
                            if dp[i][k] and dp[k+1][j] and (ord(p[k+1])-ord(p[k]))%26 == 1:
                                dp[i][j] = True
                                ans += 1
                                break
                    lookup[p[i:j+1]] = dp[i][j]
                else:
                    dp[i][j] = lookup[p[i:j+1]]

        return ans

print(Solution().findSubstringInWraproundString('cac')) # 2
print(Solution().findSubstringInWraproundString('zabmxyzab')) # 16
