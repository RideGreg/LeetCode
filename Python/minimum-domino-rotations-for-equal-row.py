# Time:  O(n)
# Space: O(1)

# 1007
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
# (A domino is a tile with *two* numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
#
# Return the minimum number of rotations so that all the values in A are the same, or all the
# values in B are the same.
#
# If it cannot be done, return -1.

import itertools
from functools import reduce

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        cand = {A[0], B[0]}
        for x in cand:
            if all(x in pair for pair in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1

    # similar algorithm as 1st solution, but not pythonic
    def minDominoRotations_ming(self, A, B):
        n, ans = len(A), float('inf')
        for cand in (A[0], B[0]):         # set is better than tuple
            cntA = cntB = 0
            for i in range(n):
                if cand not in (A[i], B[i]):
                    break
                cntA += A[i] == cand      # array.count is more pythonic
                cntB += B[i] == cand
            else:
                ans = min(ans, n - max(cntA, cntB))  # one of (A[0], B[0]) is enough
        return ans if ans < float('inf') else -1


    # Find intersection set s of {A[i], B[i]}
    # s.size = 0, no possible result.
    # s.size = 1, one and only one result.
    # s.size = 2, it means all dominoes are [a,b] or [b,a], try either one.
    # s.size > 2, impossible.
    def minDominoRotations_set(self, A, B):
        intersect = reduce(set.__and__, [set(d) for d in itertools.izip(A, B)])
        if not intersect:
            return -1
        x = intersect.pop()
        return len(A) - max(A.count(x), B.count(x))


print(Solution().minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2])) # 2