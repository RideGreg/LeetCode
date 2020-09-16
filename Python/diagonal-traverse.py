# Time:  O(m * n)
# Space: O(1)

# 498
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

from typing import List
import collections
class Solution(object):
    # Time: O(m * n), Space: O(m)
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]: # USE THIS: level order traverse, use deque
        if not matrix: return []

        ans, m, n = [], len(matrix), len(matrix[0])
        q = collections.deque()
        for i in range(m+n-1):
            nextq = collections.deque()
            if i < m:
                if i & 1:
                    q.append([i, 0])
                else:
                    q.appendleft([i, 0])

            for r, c in q:
                ans.append(matrix[r][c])
                if c + 1 < len(matrix[r]):
                    nextq.appendleft([r, c+1])
            q = nextq
        return ans

    # hash table Time:  O(m * n), Space: O(m * n)
    def findDiagonalOrder2(self, matrix: List[List[int]]) -> List[int]:
        lookup = []
        for r, row in enumerate(matrix):
            for c, num in enumerate(row):
                if len(lookup) <= r+c:
                    lookup.append([])
                lookup[r+c].append(num)
        ans = []
        for k, level in enumerate(lookup):
            ans.extend(level if k & 1 else level[::-1])
        return ans

    def findDiagonalOrder_bookshadow(self, matrix): # adjust direction
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n, ans = len(matrix), len(matrix[0]), []
        i, j, d = 0, 0, 0
        dirs = [[-1, 1], [1, -1]]
        for _ in range(m*n):
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


    def sameDiagonalOrder(self, matrix): # modify book_shadow solution for follow up question
                                         # always traverse to right-up direction
        if not matrix: return []
        m, n, ans = len(matrix), len(matrix[0]), []
        i, j, dir = 0, 0, [-1, 1]
        starti, startj = i, j
        for _ in range(m*n):
            ans.append(matrix[i][j])
            ni, nj = i + dir[0], j + dir[1]
            if 0<=ni<m and 0<=nj<n:
                i, j = ni, nj
            else:
                if starti + 1 < m:
                    starti, startj = starti + 1, 0
                else:
                    starti, startj = m - 1, startj + 1
                i, j = starti, startj
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

print(Solution().sameDiagonalOrder([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]))
print(Solution().sameDiagonalOrder([[1,2,3], [4,5,6],[7,8,9], [10, 11, 12],[13,14,15]]))