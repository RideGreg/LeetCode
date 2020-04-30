# Time:  O(n^2)
# Space: O(n)

# 221
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing all 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.
#
# Follow up: Given a 2D binary matrix filled with 0's and 1's, find the largest square
# # which diagonal is all 1 and others is 0. Only consider the main diagonal situation.
#
# For example, given the following matrix:
# 1 0 1 0 0
# 1 0 0 1 0
# 1 1 0 0 1
# 1 0 0 1 0
# Return 9
#
# Hint: maintain two helper matrix left[][] and up[][] storing the consecutive 0s on the left and up direction.
# dp[i][j] = min(dp[i - 1][j - 1], up[i - 1][j], left[i][j - 1]) + 1;

from typing import List

# DP with sliding window.
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare_bookshadow(self, matrix): # USE THIS: bookshadow, best time/space complexity, fully use previous results
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not matrix: return ans
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(2)]
        for i in range(m):
            for j in range(n):
                dp[i % 2][j] = int(matrix[i][j])
                if i and j and dp[i % 2][j]:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1], dp[i % 2][j - 1]) + 1
                ans = max(ans, dp[i % 2][j])
        return ans ** 2

    # Space O(n^2)
    def maximalSquare_ming_badSpace(self, matrix: List[List[str]]) -> int: # similar to bookshadow, but worse space complexity
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        prev, ans = [0]*n, 0
        for i in range(m):
            cur = [0] * n  # allocate a NEW memory each time
            for j in range(n):
                cur[j] = int(matrix[i][j])
                if i and j and cur[j]:
                    cur[j] = 1 + min(prev[j-1], prev[j], cur[j-1])
                ans = max(ans, cur[j])
            prev = cur
        return ans ** 2

    # space: use one line, but not pretty: need to check value in a matrix cell
    def maximalSquare_ming(self, matrix):
        if not matrix: return 0
        dp = [0] + [int(x) for x in matrix[0]]
        maxl = max(dp)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])+1):
                if matrix[i][j-1] == '1':
                    l = min(dp[j], dp[j-1])
                    dp[j] = l+1 if matrix[i-l][j-1-l] == '1' else l
                    maxl = max(maxl, dp[j])
                else:
                    dp[j] = 0
        return maxl**2


# Time:  O(n^2)
# Space: O(n^2)
# DP.
class Solution2:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in range(n)] for i in range(m)]
        max_size = 0

        for j in range(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in range(1, m):
            if matrix[i][0] == '1':
                size[i][0] = 1
            else:
                size[i][0] = 0
            for j in range(1, n):
                if matrix[i][j] == '1':
                    size[i][j] = min(size[i][j - 1],
                                     size[i - 1][j],
                                     size[i - 1][j - 1]) + 1
                    max_size = max(max_size, size[i][j])
                else:
                    size[i][j] = 0

        return max_size * max_size


# Time:  O(n^2)
# Space: O(n^2)
# DP.
class Solution3:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        H, W = 0, 1
        # DP table stores (h, w) for each (i, j).
        table = [[[0, 0] for j in range(len(matrix[0]))] \
                         for i in range(len(matrix))]
        for i in reversed(range(len(matrix))):
            for j in reversed(range(len(matrix[i]))):
                # Find the largest h such that (i, j) to (i + h - 1, j) are feasible.
                # Find the largest w such that (i, j) to (i, j + w - 1) are feasible.
                if matrix[i][j] == '1':
                    h, w = 1, 1
                    if i + 1 < len(matrix):
                        h = table[i + 1][j][H] + 1
                    if j + 1 < len(matrix[i]):
                        w = table[i][j + 1][W] + 1
                    table[i][j] = [h, w]

        # A table stores the length of largest square for each (i, j).
        s = [[0 for j in range(len(matrix[0]))] \
                for i in range(len(matrix))]
        max_square_area = 0
        for i in reversed(range(len(matrix))):
            for j in reversed(range(len(matrix[i]))):
                side = min(table[i][j][H], table[i][j][W])
                if matrix[i][j] == '1':
                    # Get the length of largest square with bottom-left corner (i, j).
                    if i + 1 < len(matrix) and j + 1 < len(matrix[i + 1]):
                        side = min(s[i + 1][j + 1] + 1, side)
                    s[i][j] = side
                    max_square_area = max(max_square_area, side * side)

        return max_square_area

print(Solution().maximalSquare([["0","0","0"],["0","0","0"],["1","1","1"]])) # 1
print(Solution().maximalSquare([
    ["0","0","0","1"],
    ["1","1","0","1"],
    ["1","1","1","1"],
    ["0","1","1","1"],
    ["0","1","1","1"]])) # 9
