# Time:  O(nlogn), n is the max of A
# Space: O(n)

# 982
# Given an array of integers A, find the # of triples of indices (i, j, k) such that:
#
# 0 <= i < A.length
# 0 <= j < A.length
# 0 <= k < A.length
# A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
#
#
# Example 1:
#
# Input: [2,1,3]
# Output: 12
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2

import collections


# Reference: https://blog.csdn.net/john123741/article/details/76576925
# FWT solution
class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def FWT(A, v):
            B = A[:]
            d = 1
            while d < len(B):
                for i in xrange(0, len(B), d << 1):
                    for j in xrange(d):
                        B[i+j] += B[i+j+d] * v
                d <<= 1
            return B

        k = 3
        n, max_A = 1, max(A)
        while n <= max_A:
            n *= 2
        count = collections.Counter(A)
        B = [count[i] for i in xrange(n)]
        C = FWT(map(lambda x : x**k, FWT(B, 1)), -1)
        return C[0]


# Time:  O(n^2), n is the length of A
# Space: O(n^2)
import collections


class Solution2(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # c is a counter of input elem, d is a counter of product of 2 elems
        c = collections.Counter(A)
        d = collections.defaultdict(int)
        for i in c:
            for j in c:
                d[i&j] += c[i]*c[j]

        return sum(c[i]*d[j] for i in c for j in d if i&j == 0)
