# Time:  O(l * n^2)
# Space: O(1)

# Given a list of strings, you need to find the longest uncommon subsequence among them.
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings
# and this subsequence should not be any subsequence of the other strings.
#
# A subsequence is a sequence that can be derived from one sequence
# by deleting some characters without changing the order of the remaining elements.
# Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
#
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.
#
# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3
# Note:
#
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].

class Solution(object):
    def findLUSlength_bookshadow(self, strs): # USE THIS
        def isSubsequence(a, b):
            m, n, pa, pb = len(a), len(b), 0, 0
            while pa < m and pb < n:
                if a[pa] == b[pb]:
                    pa += 1
                pb += 1
            return pa == m

        from collections import Counter
        cnt = Counter(strs)
        slist = sorted(set(strs), key=len, reverse=True)
        for i, s in enumerate(slist):
            if cnt[s] == 1 and not any(isSubsequence(s, p) for p in slist[:i]):
                return len(s)
        return -1

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubsequence(a, b):
            i = 0
            for j in xrange(len(b)):
                if i >= len(a):
                    break
                if a[i] == b[j]:
                    i += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)
        for i in xrange(len(strs)):
            all_of = True
            for j in xrange(len(strs)):
                if len(strs[j]) < len(strs[i]):
                    break
                if i != j and isSubsequence(strs[i], strs[j]):
                    all_of = False
                    break
            if all_of:
                return len(strs[i])
        return -1
'''
Can we do:
1. 1-loop, i is 1st, j start from 2nd? No. ["aaabb","aaabb","xy"] => 2
2. 2-loop j start from i+1? No. ["aaa","aaa","aa"] => -1
'''
