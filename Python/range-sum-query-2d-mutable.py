# Time:  ctor:   O(m * n)
#        update: O(logm * logn)
#        query:  O(logm * logn)
# Space: O(m * n)

# 308
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).

try:
    xrange
except NameError:
    xrange = range

# Binary Indexed Tree (BIT) solution.
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.__matrix = [[0]*n for _ in range(m)]
        self.__bit = [[0] * (len(self.__matrix[0]) + 1) \
                      for _ in xrange(len(self.__matrix) + 1)]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                self.update(i, j, matrix[i][j])

        '''
        self.__matrix = matrix
        for i in xrange(1, len(self.__bit)):
            for j in xrange(1, len(self.__bit[0])):
                self.__bit[i][j] = matrix[i-1][j-1] + self.__bit[i-1][j] + \
                                   self.__bit[i][j-1] - self.__bit[i-1][j-1]
        for i in reversed(xrange(1, len(self.__bit))):
            for j in reversed(xrange(1, len(self.__bit[0]))):
                last_i, last_j = i - (i & -i), j - (j & -j)
                self.__bit[i][j] = self.__bit[i][j] - self.__bit[i][last_j] - \
                                   self.__bit[last_i][j] + self.__bit[last_i][last_j]
        '''

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.__matrix[row][col]
        if delta:
            self.__matrix[row][col] = val
            row += 1
            col += 1
            while row <= len(self.__matrix):
                j = col
                while j <= len(self.__matrix[0]):
                    self.__bit[row][j] += delta
                    j += (j & -j)
                row += (row & -row)


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__sum(row2, col2) - self.__sum(row2, col1 - 1) - \
               self.__sum(row1 - 1, col2) + self.__sum(row1 - 1, col1 - 1)

    def __sum(self, row, col):
        row += 1
        col += 1
        ret = 0
        while row > 0:
            j = col
            while j > 0:
                ret += self.__bit[row][j]
                j -= (j & -j)
            row -= (row & -row)
        return ret


# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3)) # 8
numMatrix.update(3, 2, 2)
print(numMatrix.sumRegion(2, 1, 4, 3)) # 10
