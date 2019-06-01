# Time:  O(n^3)
# Space: O(n^2)

# 1039
# Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.
#
# Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is
# the product of the labels of the vertices, and the total score of the triangulation is the sum of these values
# over all N-2 triangles in the triangulation.
#
# Return the smallest possible total score that you can achieve with some triangulation of the polygon.

from typing import List

class Solution(object):
    # [3,7,4,5] only needs to compute 4 multiplications
    # p = 3: mult(3,7,4), mult(7,4,5)
    # p = 4: mult(3,7,5), mult(3,4,5)
    def minScoreTriangulation2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        dp = [[0]*N for _ in range(N)]
        for l in range(3, len(A)+1):
            for i in range(len(A)-l+1):
                j = i+l-1;
                dp[i][j] = float("inf")
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j] + A[i]*A[k]*A[j])
        return dp[0][-1]

    # TLE: dfs + memorization. E.g. [3,7,4,5] needs to compute 8 multiplications containing repeated computation which
    # are not prevented by cache:
    #  mult(5,3,7)+helper(7,4,5)
    #  mult(3,7,4)+helper(3,4,5)
    #  mult(7,4,5)+helper(3,7,5)
    #  mult(4,5,3)+helper(3,7,4)
    def minScoreTriangulation(self, A: List[int]) -> int:
        from functools import reduce, lru_cache
        import operator

        @lru_cache(None)
        def helper(nums):
            N = len(nums)
            if N == 3:
                return reduce(operator.mul, nums)

            return min(nums[(i - 1) % N] * nums[i] * nums[(i + 1) % N] + helper(nums[:i] + nums[i + 1:])
                       for i in range(N))

        return helper(tuple(A))

print(Solution().minScoreTriangulation([3,7,4,5,])) # 144: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144
print(Solution().minScoreTriangulation([1,3,1,4,1,5])) # 13, minimum score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.