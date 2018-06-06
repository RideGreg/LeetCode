# Time:  O(m * n)
# Space: O(1)
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].
#

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):   # OUT TO INNER LAYERS
        result = []
        if matrix == []:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in xrange(left, right + 1):
                result.append(matrix[top][j])
            for i in xrange(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(xrange(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(xrange(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result

    def spiralOrder(self, matrix):  # USE THIS: get the next coordinates
        if not matrix: return []
        m, n, ans = len(matrix), len(matrix[0]), []
        dirs, k, i, j = [[0,1],[1,0],[0,-1],[-1,0]], 0, 0, 0
        for _ in xrange(m*n):
            ans.append(matrix[i][j])
            matrix[i][j] = '#'
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0<=ni<m and 0<=nj<n and matrix[ni][nj]!='#':
                i, j = ni, nj
            else:
                k = (k+1) % 4
                i, j = i+dirs[k][0], j+dirs[k][1]
        return ans

if __name__ == "__main__":
    print Solution().spiralOrder([[ 1, 2, 3 ],
                                  [ 4, 5, 6 ],
                                  [ 7, 8, 9 ]])
    print Solution().spiralOrder([[2,3]])