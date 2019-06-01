# Time:  O(nlogn): binary search in range 1 and N O(logn), rolling hash O(n)
# Space: O(n)

# 1044
# Given a string S, consider all duplicated substrings: (contiguous) substrings of S
# that occur 2 or more times.  (The occurrences may overlap.)
#
# Return any duplicated substring that has the longest possible length.  (If S does
# not have a duplicated substring, the answer is "".)


# Solution: Suffix array is typical solution for this problem. Another solution is
# binary search the length of longest duplicate substring and call the help function test(L).
# test(L) slide a window of length L,
# rolling hash the string in this window,
# record the seen string in a hashset,
# and try to find duplicated string.
#
# I give it a big mod for rolling hash and it should be enough for this problem.
# Actually there could be hash collision.
# One solution is to have two different mod for hash.
# Or we can use a hashmap to record the index of string.

# A brute-force solution would be to start from len(S) - 1 and check if there exists a duplicate
# substring of that size. We decrement the size until we find a duplicate. Takes O(S^3).
# This is a tricky one on two sides:
# 1. how to find the longest string that satisfies the condition
# 2. how to compare the string of the same length
# For the first point, we can use binary search for answer since if a string of length n is
# invalid then for all k > n, there's definitely no solution because length n strings would
# become a substring of the length k string.
# For the second point, we are actually trying to compare a sliding window of string, and
# Rabin Karp algorithm https://en.wikipedia.org/wiki/Rabin–Karp_algorithm
# is perfect for doing so. The algorithm basically computes the
# hash value of all the string and start a character by character comparison only if the two
# strings have the same hash value. In order to avoid collision we can use a large prime number
# such as 1e9 + 7, 19260817, 99999989, etc.

# other solution is to apply kasai's algorithm, refer to the link below:
# https://leetcode.com/problems/longest-duplicate-substring/discuss/290852/Suffix-array-clear-solution
# Time Complexity: O(n log(n)* log(n)), Space Complexity: O(n) where n is the length of S

# Please check, Suffix array tutorial
# https://www.geeksforgeeks.org/­­kasais-algorithm-for-construction-of-lcp-array-from-suffix-array/
# https://www.geeksforgeeks.org/suffix-array-set-1-introduction/
# https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/ .

# Given a String we build its Suffix array and LCP (longest common Prefix).
# The maximum LCP is the size of longest duplicated substring.
#
# For example: S= "banana"
#
# start-index	LCP(array)	suffix
# 5	           1	a
# 3	           3	ana
# 1	           0	anana
# 0	           0	banana
# 4	           2	na
# 2	           -	nana

import collections
from functools import reduce

class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
            return 0
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) / 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]

    def longestDupSubstring_kamyu(self, S):
        M = 10**9+7
        D = 26

        def check(L):
            p = pow(D, L, M)
            curr = reduce(lambda x, y: (D*x+ord(y)-ord('a')) % M, S[:L], 0)
            lookup = collections.defaultdict(list)
            lookup[curr].append(L-1)
            for i in range(L, len(S)):
                curr = ((D*curr) % M + ord(S[i])-ord('a') -
                        ((ord(S[i-L])-ord('a'))*p) % M) % M
                if curr in lookup:
                    for j in lookup[curr]:  # check if string is the same when hash is the same
                        if S[j-L+1:j+1] == S[i-L+1:i+1]:
                            return i-L+1
                lookup[curr].append(i)
            return 0

        left, right = 1, len(S)-1
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        result = check(right)
        return S[result:result + right]

print(Solution().longestDupSubstring('banana')) # 'ana'
print(Solution().longestDupSubstring('abcd')) # ''

