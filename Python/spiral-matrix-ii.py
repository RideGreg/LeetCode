# Time:  O(n^2)
# Space: O(1)
#
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):   # OUT TO INNER LAYERS
        matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]

        left, right, top, bottom, num = 0, n - 1, 0, n - 1, 1

        while left <= right and top <= bottom:
            for j in xrange(left, right + 1):
                matrix[top][j] = num
                num += 1
            for i in xrange(top + 1, bottom):
                matrix[i][right] = num
                num += 1
            for j in reversed(xrange(left, right + 1)):
                if top < bottom:
                    matrix[bottom][j] = num
                    num += 1
            for i in reversed(xrange(top + 1, bottom)):
                if left < right:
                    matrix[i][left] = num
                    num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return matrix

    def generateMatrix(self, n):  # USE THIS: coordinates
        ans = [[False]*n for _ in xrange(n)]
        dirs, k, i, j = [[0,1],[1,0],[0,-1],[-1,0]], 0, 0, 0
        for num in xrange(1, n*n+1):
            ans[i][j] = num
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0<=ni<n and 0<=nj<n and ans[ni][nj] is False:
                i, j = ni, nj
            else:
                k = (k+1) % 4
                i, j = i+dirs[k][0], j+dirs[k][1]
        return ans

if __name__ == "__main__":
    print Solution().generateMatrix(3)
    print Solution().generateMatrix(8)
