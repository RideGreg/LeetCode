# Time:  O(k * n^2)
# Space: O(n^2)

# 1278 weekly contest 165 11/30/2019

# You are given a string s containing lowercase letters and an integer k. You need to :
#
#     First, change some characters of s to other lowercase English letters.
#     Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
# Return the minimal number of characters that you need to change to divide the string.

# 1 <= k <= s.length <= 100

try:
    xrange
except NameError:
    xrange = range

class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # minChange[i][j]: minimum number of changes to make s[i, j] palindrome
        n = len(s)
        minChange = [[0]*n for _ in range(n)]
        for sz in range(2, n+1):
            for l in range(n+1-sz):
                r = l + sz -1
                if sz == 2:
                    minChange[l][r] = int(s[l] != s[r])
                else:
                    minChange[l][r] = minChange[l+1][r-1] + int(s[l] != s[r])

        # dp[d][i]: minimum number of changes to divide s[0, i] into d palindromes
        dp = minChange[0][:]
        for d in range(2, k+1):
            ndp = [0] * n
            for j in range(d, n):
                ndp[j] = min(dp[k]+minChange[k+1][j] for k in range(d-2, j))
            dp = ndp
        return dp[-1]


    def palindromePartition_wrong_mingContest(self, s: str, k: int) -> int:
        if k == len(s): return 0
        n = len(s)
        lookup = [[False] * n for _ in range(n)]  # lookup[i][j] if s[i][j] is palindrome
        dp = [[float('inf')]*n for _ in range(k+1)] # dp[i][j] is ans for partition s[j:n] into i groups
        for i in range(n):
            dp[1][i] = 0
            b, e = i, n-1
            while b<e:
                if s[b] != s[e]:
                    dp[1][i] += 1
                b+=1
                e-=1
        for kk in range(2, k+1):
            for i in reversed(range(n)):
                if n-i <= kk:
                    dp[kk][i] = 0
                    continue
                for j in range(i, n):
                    if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                        lookup[i][j] = True
                        dp[kk][i] = min(dp[kk][i], dp[kk-1][j + 1] if j<n-1 else 0)
        return dp[k-1][0]

print(Solution().palindromePartition('abc', 2)) # 1
print(Solution().palindromePartition('aabbc', 3)) # 0
print(Solution().palindromePartition('aabbc', 2)) # 1
print(Solution().palindromePartition('leetcode', 7)) # 0
