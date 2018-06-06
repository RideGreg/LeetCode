# Time:  O(m * n)
# Space: O(1)

# Given a matrix of M x N elements (M rows, N columns),
# return all elements of the matrix in diagonal order as shown in the below image.
#
# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
#
# Note:
# The total number of elements of the given matrix will not exceed 10,000.
# Show Company Tags

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        row, col, d = 0, 0, 0
        dirs = [(-1, 1), (1, -1)]

        for i in xrange(len(matrix) * len(matrix[0])):
            result.append(matrix[row][col])
            row += dirs[d][0]
            col += dirs[d][1]

            # EASY TO MAKE MISTAKE: have to check row/col against len(matrix), len(matrix[0]) before check 0
            # e.g. [[1,2,3], [4,5,6], [7,8,9]]
            if row >= len(matrix):
                row = len(matrix) - 1
                col += 2
                d = 1 - d
            elif col >= len(matrix[0]):
                col = len(matrix[0]) - 1
                row += 2
                d = 1 - d
            elif row < 0:
                row = 0
                d = 1 - d
            elif col < 0:
                col = 0
                d = 1 - d

        return result

    def findDiagonalOrder_bookshadow(self, matrix): # USE THIS
        if not matrix: return []
        m, n, ans = len(matrix), len(matrix[0]), []
        i, j, d = 0, 0, 0
        dirs = [[-1, 1], [1, -1]]
        for _ in xrange(m*n):
            ans.append(matrix[i][j])
            ni = i + dirs[d][0]
            nj = j + dirs[d][1]

            if 0<=ni<m and 0<=nj<n:
                i, j = ni, nj
            else:
                if d == 0:     # i+1 is always valid
                    if j+1<n:
                        j += 1
                    else:
                        i += 1
                else:          # j+1 is always valid
                    if i+1<m:
                        i += 1
                    else:
                        j += 1
                d = 1 - d
        return ans

    def findDiagonalOrder_ming(self, matrix): # Time Limit Exceeded because checking too many out-of-boundary positions
        if not matrix: return []
        m, n, level, ans = len(matrix), len(matrix[0]), 0, []
        for k in xrange(m+n-1):
            for i in [reversed(xrange(k+1)), xrange(k+1)][level==1]:
                if 0<=i<m and 0<=k-i<n:
                    ans.append(matrix[i][k-i])
            level = 1 - level
        return ans

    def sameDiagonalOrder(self, matrix): # A follow up question, always traverse to right-up direction
        if not matrix: return []
        m, n, ans = len(matrix), len(matrix[0]), []
        i, j, dir = 0, 0, [-1, 1]
        starti, startj = i, j
        for _ in xrange(m*n):
            ans.append(matrix[i][j])
            ni, nj = i + dir[0], j + dir[1]
            if 0<=ni<m and 0<=nj<n:
                i, j = ni, nj
            else:
                if starti + 1 < m:
                    starti += 1
                    startj = 0
                else:
                    starti = m - 1
                    startj += 1
                i, j = starti, startj
        return ans

print Solution().sameDiagonalOrder([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
print Solution().sameDiagonalOrder([[1,2,3], [4,5,6],[7,8,9], [10, 11, 12],[13,14,15]])