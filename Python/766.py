class Solution(object):
    def isToeplitzMatrix(self, matrix):
        r, c = len(matrix), len(matrix[0])
        if r == 1 or c == 1:
            return True
        for i in xrange(r-1):
            j = 0
            n = matrix[i][j]
            ii, jj = i+1, j+1
            while ii < r and jj < c:
                if matrix[ii][jj] != n:
                    return False
                ii, jj = ii+1, jj+1
        for j in xrange(1, c-1):
            i = 0
            n = matrix[i][j]
            ii, jj = i+1, j+1
            while ii < r and jj < c:
                if matrix[ii][jj] != n:
                    return False
                ii, jj = ii+1, jj+1
        return True

print Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])