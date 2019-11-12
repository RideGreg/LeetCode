# Time:  O(n)
# Space: O(1)

# 639
# A message containing letters from A-Z is being encoded to numbers using the following mapping way:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Beyond that, now the encoded string can also contain the character '*',
# which can be treated as one of the numbers from 1 to 9.
#
# Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
#
# Also, since the answer may be very large, you should return the output mod 109 + 7.
#
# Example 1:
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
# Example 2:
# Input: "1*"
# Output: 9 + 9 = 18
# Note:
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.

# DP: 令dp[x]表示 s[0 .. x] 对应的原串的可能个数
#
# 状态转移方程如下：
# dp[x] = (dp[x - 2] * dmap[s[x - 1, x]] + dp[x - 1] * dmap[s[x]]) % MOD
# 上式中，dmap[s]表示子串s对应的原串的可能个数，分别令s = '0', '1', ..., '9', '*'，
# 以及'00', '01', ... '*9', '**'对dmap进行初始化

class Solution(object):
    def numDecodings(self, s): # USE THIS: bookshadow
        """
        :type s: str
        :rtype: int
        """
        import collections
        MOD = 10**9 + 7
        dmap = collections.defaultdict(int)
        ch = '0123456789*'
        for m in ch:
            if m == '*': dmap[m] = 9
            elif '1' <= m <= '9': dmap[m] = 1
            for n in ch:
                r = m + n
                if m == '*':
                    if n == '*': dmap[r] = 15      # 11->19, 21->26
                    elif '0' <= n <= '6': dmap[r] = 2   # 1n, 2n
                    elif '7' <= n <= '9': dmap[r] = 1   # 1n
                elif m == '1':
                    if n == '*': dmap[r] = 9       # 11->19
                    else: dmap[r] = 1
                elif m == '2':
                    if n == '*': dmap[r] = 6       # 21->26
                    elif '0' <= n <= '6': dmap[r] = 1

        cur = 0
        prev = pprev = 1
        lc = '-'   # using lastchar, so don't need to consider s[i-1] and i > 0
        for c in s:
            cur = (prev * dmap[c] + pprev * dmap[lc + c]) % MOD
            lc = c
            prev, pprev = cur, prev
        return cur

    def numDecodings_kamyu(self, s): # scrolling array, messier than using 3 variables
        M, W = 1000000007, 3
        dp = [0] * W
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else dp[0] if s[0] != '0' else 0
        for i in xrange(1, len(s)):
            if s[i] == '*':
                dp[(i + 1) % W] = 9 * dp[i % W]
                if s[i - 1] == '1':
                    dp[(i + 1) % W] = (dp[(i + 1) % W] + 9 * dp[(i - 1) % W]) % M
                elif s[i - 1] == '2':
                    dp[(i + 1) % W] = (dp[(i + 1) % W] + 6 * dp[(i - 1) % W]) % M
                elif s[i - 1] == '*':
                    dp[(i + 1) % W] = (dp[(i + 1) % W] + 15 * dp[(i - 1) % W]) % M
            else:
                dp[(i + 1) % W] = dp[i % W] if s[i] != '0' else 0
                if s[i - 1] == '1':
                    dp[(i + 1) % W] = (dp[(i + 1) % W] + dp[(i - 1) % W]) % M
                elif s[i - 1] == '2' and s[i] <= '6':
                    dp[(i + 1) % W] = (dp[(i + 1) % W] + dp[(i - 1) % W]) % M
                elif s[i - 1] == '*':
                    dp[(i + 1) % W] = (dp[(i + 1) % W] + (2 if s[i] <= '6' else 1) * dp[(i - 1) % W]) % M
        return dp[len(s) % W]

print(Solution().numDecodings('*')) # 9
print(Solution().numDecodings('**')) # 96:
# AA, AB, ... AI, ..., IA, IB, .. II; K, L..S, U..Z
# (1)(1), (1)(2) .. (9)(9); 11->19, 21->26