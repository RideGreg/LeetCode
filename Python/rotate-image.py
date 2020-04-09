# Time:  O(n^2)
# Space: O(1)

# 48
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?
#

# Time:  O(n^2)
# Space: O(1)
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)

        # 90 rotate => m[r][c] -> m[c][n-1-r]
        # we can do horizontal mirror + diagonal mirror
        # r,c -> n-1-r, c -> c, n-1-r
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Or anti-diagonal mirror + horizontal mirror
        # r,c -> n-1-c, n-1-r -> c, n-1-r
        '''
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        for i in range(n // 2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]'''

        return matrix

# Time:  O(n^2)
# Space: O(n^2)
class Solution2:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]


print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [[7,4,1],[8,5,2],[9,6,3]]

