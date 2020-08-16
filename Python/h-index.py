# Time:  O(n)
# Space: O(n)

# 274
# Given an array of citations (each citation is a non-negative integer)
# of a researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia:
# "A scientist has index h if h of his/her N papers have
# at least h citations each, and the other N − h papers have
# no more than h citations each."
#
# For example, given citations = [3, 0, 6, 1, 5],
# which means the researcher has 5 papers in total
# and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and
# the remaining two with no more than 3 citations each, his h-index is 3.
#
# Note: If there are several possible values for h, the maximum one is taken as the h-index.
#


# h-index不会超过max(citations)最大引用数，也不会超过len(citations)文章篇数。从这两方面下手可得到不同解法。
# counting sort相当于构造一个bounded Counter，binary search里构造了一个unbounded Counter.

import collections

# Counting sort.
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0] * (n + 1)
        for x in citations:
            # Put all x >= n in the same bucket.
            if x >= n:
                count[n] += 1
            else:
                count[x] += 1

        h = 0
        for i in reversed(range(0, n + 1)):
            h += count[i]
            if h >= i:
                return i

# Time:  O(nlogn)
# Space: O(1)
#
# Build a histogram of citations ordered in decreasing order for each paper,
# find the crossing point of the decreasing citation curve and maximal square box.
# |
# |-----
# |     \
# |      -----
# |---        \
# |__|__________\_____
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h

# Time:  O(nlogm), m is max(citations)
# Space: O(n)
# binary search
class Solution3:
    def hIndex(self, citations):
        def valid(m):
            acc = 0
            for k,v in cnt.items():
                if k >= m:
                    acc += v
            return acc >= m

        cnt = collections.Counter(citations)
        l, r = 0, max(citations)
        while l < r:
            m = (l+r+1) // 2
            if valid(m):
                l = m
            else:
                r = m - 1
        return l

print(Solution().hIndex([3,0,6,1,5])) # 3