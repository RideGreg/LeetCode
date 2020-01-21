# Time:  O(m * n)
# Space: O(1)

# 1277 weekly contest 165 11/30/2019

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution(object):
    def countSquares(self, matrix): # USE THIS: pretty solution
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    k = min(matrix[i-1][j], matrix[i][j-1])
                    matrix[i][j] = k+1 if matrix[i-k][j-k] else k
                    ans += matrix[i][j]
        return ans
        #return sum(x for row in matrix for x in row)

    def countSquares_ming(self, matrix):
        m, n = len(matrix), len(matrix[0])
        up, ans = [0]*n, 0
        for i in range(m):
            left = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    left = 0
                    up[j] = 0
                else:
                    left += 1
                    up[j] += 1
                    matrix[i][j] = min(1+(matrix[i-1][j-1] if i and j else 0), left, up[j])
                    ans += matrix[i][j]
        return ans

print(Solution().countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])) # 15
print(Solution().countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
])) # 7