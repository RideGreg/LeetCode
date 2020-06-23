# Time:  O(m * n)
# Space: O(1)
# 73
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.

# A simple improvement uses O(m + n) space, but still not the best solution.
# 记录为0的所有行号和列号

# Could you devise a constant space solution?
# 不能使用额外空间，那么只能修改原始矩阵

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.


    # 利用第一行和第一列存储为0的信息 USE THIS
    def setZeroes(self, matrix):
        import itertools
        R = len(matrix)
        C = len(matrix[0])
        row1_zero = any(matrix[0][j] == 0 for j in range(C))
        col1_zero = any(matrix[i][0] == 0 for i in range(R))

        for i, j in itertools.product(range(1, R), range(1, C)):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0

        for i, j in itertools.product(range(1, R), range(1, C)):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

        if row1_zero:
            for j in range(C):
                matrix[0][j] = 0

        if col1_zero:
            for i in range(R):
                matrix[i][0] = 0

    # Mark the non zeros elements needs change. zero elem should be kept to set other row/col
    # Constant space, but bad time O(m*n*(m+n)) potentially set the row/col for every cell
    def setZeroes_bruteForce(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] is 0: # cannot use == because 0==False is True
                    for k in range(C):
                        matrix[r][k] = False if matrix[r][k] is not 0 else 0
                    for k in range(R):
                        matrix[k][c] = False if matrix[k][c] is not 0 else 0
        for r in range(R):
            for c in range(C):
                if matrix[r][c] is False:
                    matrix[r][c] = 0


    # use m+n extra space to store the row/cod ids which should be zero
    def setZeroes_extraSpace(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [ [1, 0, 1, 1]
             , [1, 1, 0, 1]
             , [1, 1, 1, 0]
             , [1, 1, 1, 1]]
    Solution().setZeroes_bruteForce(matrix)
    print(matrix) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]