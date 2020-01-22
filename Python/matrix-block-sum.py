# Time:  O(m * n)
# Space: O(m * n)

# 1314 biweekly contest 17 1/11/2020

# Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum
# of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.

from typing import List

class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        accu = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(m):
            for j in xrange(n):
                accu[i+1][j+1] = accu[i+1][j]+accu[i][j+1]-accu[i][j]+mat[i][j]
        result = [[0 for _ in xrange(n)] for _ in xrange(m)]        
        for i in xrange(m):
            for j in xrange(n):
                r1, c1, r2, c2 = max(i-K, 0), max(j-K, 0), min(i+K+1, m), min(j+K+1, n)
                result[i][j] = accu[r2][c2]-accu[r1][c2]-accu[r2][c1]+accu[r1][c1]
        return result

    def matrixBlockSum_ming(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        psum = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                psum[i][j] = mat[i][j]
                if j > 0:
                    psum[i][j] += psum[i][j-1]
                if i > 0:
                    psum[i][j] += psum[i-1][j]
                if i and j:
                    psum[i][j] -= psum[i - 1][j-1]
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                li, ri = max(i-K, 0), min(i+K, m-1)
                lj, rj = max(j-K, 0), min(j+K, n-1)
                ans[i][j] = psum[ri][rj]
                if li:
                    ans[i][j] -= psum[li-1][rj]
                if lj:
                    ans[i][j] -= psum[ri][lj-1]
                if li and lj:
                    ans[i][j] += psum[li-1][lj - 1]
        return ans

print(Solution().matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1))
print(Solution().matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],2))
