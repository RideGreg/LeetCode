# Time:  O(n^2)
# Space: O(n^2)

# 730
# Given a string S, find the number of different non-empty palindromic subsequences in S,
# and return that number modulo 10^9 + 7.
#
# A subsequence of a string S is obtained by deleting 0 or more characters from S.
#
# A sequence is palindromic if it is equal to the sequence reversed.
#
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.
#
# Example 1:
# Input:
# S = 'bccb'
# Output: 6
# Explanation:
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
#
# Example 2:
# Input:
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
#
# Explanation:
# There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
# Note:
# - The length of S will be in the range [1, 1000].
# - Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.


# Search + Memoization
class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        size = len(S)
        # next: position of char (in 'abcd') in S[i:]
        # prev: position of char (in 'abcd') in S[:i]
        next = [{k : -1 for k in 'abcd'} for _ in range(size)]
        prev = [{k : -1 for k in 'abcd'} for _ in range(size)]

        prev[0][S[0]] = 0
        for x in range(1, size):
            for k in 'abcd':
                prev[x][k] = x if k == S[x] else prev[x-1][k]

        next[size-1][S[size-1]] = size-1
        for x in range(size-2, -1, -1):
            for k in 'abcd':
                next[x][k] = x if k == S[x] else next[x+1][k]

        dmap = [[0] * size for _ in range(size)]

        def solve(i, j):
            if i > j: return 0
            if not dmap[i][j]:
                ans = 0
                for k in 'abcd':
                    ii, jj = next[i][k], prev[j][k]
                    if ii < 0: continue # S[i:] doesn't contain char k
                    if ii <= j: ans += 1 # non-duplicate, so single 'k' is once
                    if ii < jj: ans += solve(ii + 1, jj - 1) + 1 # 1 means 'kk'
                dmap[i][j] = ans % (10 ** 9 + 7)
            return dmap[i][j]

        return solve(0, size - 1)

    def countPalindromicSubsequences_kamyu(self, S):
        def dp(i, j):
            if not lookup[i][j]:
                result = 1
                if i <= j:
                    for x in range(4):
                        i0 = nxt[i][x]
                        j0 = prv[j][x]
                        if i <= i0 <= j:
                            result = (result + 1) % P
                        if -1 < i0 < j0:
                            result = (result + dp(i0+1, j0-1)) % P
                result %= P
                lookup[i][j] = result
            return lookup[i][j]

        prv = [None] * len(S)
        nxt = [None] * len(S)

        last = [-1] * 4
        for i in range(len(S)):
            last[ord(S[i])-ord('a')] = i
            prv[i] = tuple(last)

        last = [-1] * 4
        for i in reversed(range(len(S))):
            last[ord(S[i])-ord('a')] = i
            nxt[i] = tuple(last)

        P = 10**9 + 7
        lookup = [[0] * len(S) for _ in range(len(S))]
        return dp(0, len(S)-1) - 1

print(Solution().countPalindromicSubsequences("bccb")) # 6
print(Solution().countPalindromicSubsequences(
    "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
)) # 104860361
