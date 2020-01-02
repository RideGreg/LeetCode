# Time:  O(m * n)
# Space: O(m * n)

# 1072  weekly contest 139 6/1/2019
# Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and
# flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.
#
# Return the maximum number of rows that have all values equal after some number of flips.

# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300
# All matrix[i].length's are equal
# matrix[i][j] is 0 or 1

import collections


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        count = collections.Counter(tuple(x^row[0] for x in row)
                                          for row in matrix)
        ''' OR
        lookup = collections.defaultdict(int)
        for row in matrix:
            k = tuple(x^row[0] for x in row)
            lookup[k] += 1
        '''
        return max(count.values())

    def maxEqualRowsAfterFlips_ming(self, matrix):
        N = len(matrix[0])
        lookup = collections.defaultdict(int)
        for row in matrix:
            key1 = tuple([i for i in range(N) if row[i] != 0]) # columns with 1
            key2 = tuple([i for i in range(N) if row[i] == 0]) # columns with 0
            lookup[key1] += 1
            lookup[key2] += 1
        return max(lookup.values())

print(Solution().maxEqualRowsAfterFlips([[0],[1],[0],[0],[1],[1],[1],[1],[0],[1]])) # 10. is this correct?
print(Solution().maxEqualRowsAfterFlips([[0,1], [1,1]])) # 1
print(Solution().maxEqualRowsAfterFlips([[0,1], [1,0]])) # 2
print(Solution().maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]])) # 2