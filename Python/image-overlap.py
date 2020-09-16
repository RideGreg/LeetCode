# Time:  O(n^4)
# Space: O(n^2)

# 835
# Two images A and B are given, represented as binary,
# square matrices of the same size.
# (A binary matrix has only 0s and 1s as values.)
#
# We translate one image however we choose (sliding it left, right, up,
# or down any number of units), and place it on top of the other image.
# After, the overlap of this translation is the number of positions that
# have a 1 in both images.
# (Note also that a translation does not include any kind of rotation.)
#
# What is the largest possible overlap?
#
# Example 1:
#
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
#
# Notes:
# 1. 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 2. 0 <= A[i][j], B[i][j] <= 1

import collections, itertools
class Solution(object):
    # count the delta from each '1' in A to each '1' in B, return the max count.
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        count = collections.Counter()
        for i, j in itertools.product(range(n), range(n)):
            if A[i][j]:
                for i2, j2, in itertools.product(range(n), range(n)):
                    if B[i2][j2]:
                        count[i2 - i, j2 - j] += 1
        '''
        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if v:
                    for i2, row2 in enumerate(B):
                        for j2, v2 in enumerate(row2):
                            if v2:
                                count[i-i2, j-j2] += 1'''
        return max(count.values()) if count else 0

    # Time O(n^6), Space O(n^2)
    # enumerate all possible 2D delta to shift a '1' in A to a '1' in B. O(n^4)
    # when find a delta, count the overlap with B if shifting A by this delta. O(n^2)
    def largestOverlap2(self, A, B):
        N = len(A)
        A2 = [(r, c) for r, row in enumerate(A)
              for c, v in enumerate(row) if v]
        B2 = [(r, c) for r, row in enumerate(B)
              for c, v in enumerate(row) if v]
        Bset = set(B2)

        delta, ans = set(), 0
        for xa, ya in A2:
            for xb, yb in B2:
                d = (xb-xa, yb-ya)
                if d not in delta:
                    delta.add(d)
                    ans = max(ans, sum((s+d[0], t+d[1]) in Bset for s,t in A2))
        return ans

print(Solution().largestOverlap(
    [
        [1,1,0],
        [0,1,0],
        [0,1,0]
    ], [
        [0,0,0],
        [0,1,1],
        [0,0,1]
    ]
)) # 3