# Time:  O(m * n * log(min(m, n))
# Space: O(m * n)

# 1329 biweekly contest 18 1/25/2020

# Given a m * n matrix mat of integers, sort it diagonally in ascending order from the
# top-left to the bottom-right then return the sorted array.

try:
    xrange
except NameError:
    xrange = range

import collections


class Solution(object):
    def diagonalSort(self, mat): # USE THIS: group elements diagonally
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        lookup = collections.defaultdict(list)
        for i in xrange(m):
            for j in xrange(n):
                lookup[i-j].append(mat[i][j])
        for v in lookup.values():
            v.sort()
        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                mat[i][j] = lookup[i-j].pop()
        return mat

    # use less space, but need to be careful about indices
    def diagonalSort_ming(self, mat):
        m, n = len(mat), len(mat[0])
        if m == 1 or n == 1: return mat
        for k in range(n - 2, 1 - m, -1):  # j-i
            temp = []
            for i in range(m):
                j = i + k
                if 0 <= i < m and 0 <= j < n:
                    temp.append(mat[i][j])

            temp.sort(reverse=True)
            for i in range(m):
                j = i + k
                if 0 <= i < m and 0 <= j < n:
                    mat[i][j] = temp.pop()
        return mat


print(Solution().diagonalSort([
    [3,3,1,1],
    [2,2,1,2],
    [1,1,1,2]
]))
# [[1,1,1,1],
#  [1,2,2,2],
#  [1,2,3,3]]