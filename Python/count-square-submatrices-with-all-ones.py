# Time:  O(m * n)
# Space: O(1)

# 1277 weekly contest 165 11/30/2019

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution(object):
    def countSquares(self, matrix): # USE THIS: pretty solution, reuse input matrix, Space O(1)
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    # for top row and leftmost col, 0 means 0 square, 1 means 1 square. No need further processing.
                    # 0 1 1
                    # 0 1 2
                    # 1 2 1
                    if i > 0 and j > 0:
                        matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                    ans += matrix[i][j]
        return ans
        #return sum(x for row in matrix for x in row)

    # If doesn't allow to modify input matrix: Time O(m*n) Space O(n)
    def countSquares_helperMatrix(self, matrix):
        if not matrix: return 0

        m, n, ans = len(matrix), len(matrix[0]), 0
        dp = [[0] * (n+1) for _ in range(2)]
        for r in range(1, m+1):
            for c in range(1, n+1):
                if matrix[r-1][c-1]:
                    dp[r%2][c] = 1 + min(dp[r%2][c-1], dp[(r-1)%2][c], dp[(r-1)%2][c-1])
                    ans += dp[r%2][c]
                else:
                    dp[r%2][c] = 0
        return ans

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