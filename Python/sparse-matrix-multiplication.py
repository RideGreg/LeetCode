# Time:  O(m * n * l), A is m x n matrix, B is n x l matrix
# Space: O(m * l)

# 311
# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in xrange(m):
            for k in xrange(n):
                if A[i][k]:
                    for j in xrange(l):
                        res[i][j] += A[i][k] * B[k][j]
        return res

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

print(Solution().multiply(A, B)) # [
#   [7,0.0],
#   [-7,0,3]
# ]