# Time:  O(m * n)
# Space: O(1)

# 1289 biweekly contest 15 12/14/2019
#
# Given a square grid of integers arr, a falling path with non-zero shifts is a
# choice of exactly one element from each row of arr, such that no two elements
# chosen in adjacent rows are in the same column.
#
# Return the minimum sum of a falling path with non-zero shifts.

import heapq
from typing import List

class Solution(object):
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m1, m2, col = float('inf'), float('inf'), None
        firstRow = True

        for r in arr:
            nm1, nm2, ncol = float('inf'), float('inf'), None

            for j, v in enumerate(r):
                if not firstRow:
                    v += m1 if j != col else m2

                if v < nm1:
                    nm1, nm2, ncol = v, nm1, j
                elif v < nm2:
                    nm2 = v

            m1, m2, col = nm1, nm2, ncol
            if firstRow:
                firstRow = False
        return m1

    def minFallingPathSum_kamyu(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(arr)):
            smallest_two = heapq.nsmallest(2, arr[i-1])
            for j in range(len(arr[0])):
                arr[i][j] += smallest_two[1] if arr[i-1][j] == smallest_two[0] else smallest_two[0]
        return min(arr[-1])

    # Con: not maintain m1,m2,i1, re-calcualte each time
    def minFallingPathSum_awice(self, arr):
        dp = arr[0]
        N = len(dp)

        # dp[i] : currently minimum sum that ends here
        for row in arr[1:]:
            m1 = min(dp)
            i1 = dp.index(m1)

            dp2 = [m1 + x for x in row]
            # dp2 is wrong at i1
            m2 = float('inf')
            for j in range(N):
                if j != i1:
                    x = dp[j]
                    if x < m2:
                        m2 = x

            dp2[i1] = m2 + row[i1]
            dp = dp2
        return min(dp)

print(Solution().minFallingPathSum([
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2]
])) # 7

print(Solution().minFallingPathSum([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])) # 13

print(Solution().minFallingPathSum([
    [2,20,3],
    [200,10,201],
    [500,1,500]
])) # 204
