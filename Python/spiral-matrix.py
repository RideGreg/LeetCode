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
    def spiralOrder(self, matrix):   #  USE THIS: OUT TO INNER LAYERS
        if not matrix: return []
        ans = []
        t, b, l, r = 0, len(matrix)-1, 0, len(matrix[0])-1
        while t <= b and l <= r:
            ans.extend(matrix[t][l:r+1])
            for row in range(t+1, b):
                ans.append(matrix[row][r])
            if b > t:     # KENG: if no check, last single row will be printed twice
                ans.extend(reversed(matrix[b][l:r+1])) # KENG: [r:l-1:-1] wrong when l=0 because -1 is rightmost col
            if r > l:
                for row in range(b-1, t, -1):
                    ans.append(matrix[row][l])
            t, b, l, r = t+1, b-1, l+1, r-1
        return ans

    def spiralOrder_wrong(self, matrix):
        if not matrix: return []
        ans = []
        t, b, l, r = 0, len(matrix)-1, 0, len(matrix[0])-1
        while t <= b or l <= r:
            ans.extend(matrix[t][l:r])  # if each iteration doesn't do last item, the single center
                                        # will be ignored by all 4 iterations
            for row in range(t, b):
                ans.append(matrix[row][r])
            ans.extend(matrix[b][r:l:-1])
            for row in range(b, t, -1):
                ans.append(matrix[row][l])
            t, b, l, r = t+1, b-1, l+1, r-1
        return ans

    def spiralOrder_coord(self, matrix):  # get the next coordinates
        if not matrix: return []
        m, n, ans = len(matrix), len(matrix[0]), []
        dirs, k, i, j = [[0,1],[1,0],[0,-1],[-1,0]], 0, 0, 0
        for _ in xrange(m*n):
            ans.append(matrix[i][j])
            matrix[i][j] = '#'

            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0<=ni<m and 0<=nj<n and matrix[ni][nj]!='#':
                i, j = ni, nj
            else:  # out of boundary
                k = (k+1) % 4
                i, j = i+dirs[k][0], j+dirs[k][1]
        return ans


if __name__ == "__main__":
    print(Solution().spiralOrder([[ 1, 2, 3 ],
                                  [ 4, 5, 6 ],
                                  [ 7, 8, 9 ]])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(Solution().spiralOrder([[2,3]])) # [2,3]
    print(Solution().spiralOrder([[2], [3], [4]])) # [2,3,4]