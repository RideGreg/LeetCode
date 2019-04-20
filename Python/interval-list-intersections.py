# Time:  O(m + n)
# Space: O(1)

# 986
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that is either empty, or can be
# represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            left = max(A[i].start, B[j].start)
            right = min(A[i].end, B[j].end)
            if left <= right:
                result.append(Interval(left, right))
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1
        return result
