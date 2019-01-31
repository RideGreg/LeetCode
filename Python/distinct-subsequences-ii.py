# Time:  O(n)
# Space: O(1)

# 940
# Given a string S, count the number of distinct, non-empty subsequences of S .
# Since the result may be large, return the answer modulo 10^9 + 7.

# S contains only lowercase letters.
# 1 <= S.length <= 2000

# Dynamic Programming
# It is not intuitive to find the answer. In the solution below, we find all subsequences (including empty ones),
# and subtract the empty subsequence at the end.
#
# For a dynamic programming solution, in order to not repeat work, our goal is to phrase the current problem in terms of
# the answer to previous problems. A typical idea will be to try to count the number of states dp[k] (distinct subsequences)
# that use letters S[0], S[1], ..., S[k].
#
# Naively, S = "abcx", we have dp[k] = dp[k-1] * 2. This is because for dp[2] which counts ("", "a", "b", "c", "ab", "ac",
# "bc", "abc"), dp[3] counts all of those, plus all of those with the x ending, like ("x", "ax", "bx", "cx", "abx", "acx", "bcx", "abcx").
#
# However, for something like S = "abab", let's play around with it. We have:
#
# dp[0] = 2, as it counts ("", "a")
# dp[1] = 4, as it counts ("", "a", "b", "ab");
# dp[2] = 7 as it counts ("", "a", "b", "aa", "ab", "ba", "aba");
# dp[3] = 12, as it counts ("", "a", "b", "aa", "ab", "ba", "bb", "aab", "aba", "abb", "bab", "abab").
# We have that dp[3]countsdp[2], plus("b", "aa", "ab", "ba", "aba")with"b"added to it. Notice that("", "a")are duplicate
# in this list. In general, the sequences that resulted from putting "b" the last time (ie."b", "ab"`) will get double counted.
#
# This insight leads to the recurrence:
# dp[k] = 2 * dp[k-1] - dp[last[S[k]] - 1]
#
# The # of distinct subsequences ending at S[k], is twice the distinct subsequences counted by dp[k-1] (all of them, plus
# all of them with S[k] appended), minus the amount we double counted, which is dp[last[S[k]] - 1].

import collections


class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        import collections
        M = 10**9 + 7
        result = 1 # empty string ''
        dupCount = collections.defaultdict(int)
        for c in S:
            result, dupCount[ord(c)-ord('a')] = 2*result-dupCount[ord(c)-ord('a')], result
        return (result-1) % M

    # Time O(n), Space O(n)
    def distinctSubseqII_LeetCodeOfficial(self, S):
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            if x in last:
                value = dp[-1]*2 - dp[last[x] - 1]
            else:
                value = dp[-1]*2
            dp.append(value % (10**9+7))
            last[x] = i+1
        return dp[-1] - 1

print(Solution().distinctSubseqII("abc")) # 7
print(Solution().distinctSubseqII("aba")) # 6, duplicate 'a'
print(Solution().distinctSubseqII("aaa")) # 3, duplicate 'a', 'aa'
