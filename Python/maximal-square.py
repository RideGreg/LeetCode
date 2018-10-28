# Time:  O(n^2)
# Space: O(n)
#
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

# DP with sliding window.
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    class Solution(object):  #USE THIS: concise
        def maximalSquare_bookshadow(self, matrix):
            """
            :type matrix: List[List[str]]
            :rtype: int
            """
            ans = 0
            if not matrix: return ans
            m, n = len(matrix), len(matrix[0])
            dp = [[0] * n for _ in xrange(2)]
            for i in xrange(m):
                for j in xrange(n):
                    dp[i % 2][j] = int(matrix[i][j])
                    if i and j and dp[i % 2][j]:
                        dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1], dp[i % 2][j - 1]) + 1
                    ans = max(ans, dp[i % 2][j])
            return ans ** 2

    # wrong for [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    def maximalSquare(self, matrix):
        def foo(i, j, n):
            ret = 1
            for k in xrange(n):
                if matrix[i][j-1-k] == '1' and matrix[i-1-k][j] == '1':
                    ret += 1
                else:
                    break
            return ret

        if not matrix: return 0
        m, n, dp = len(matrix), len(matrix[0]), [int(c) for c in matrix[0]]
        ans = max(dp)
        for i in xrange(1, m):
            for j in reversed(xrange(0, n)):
                if matrix[i][j] == '0':
                    dp[j] = 0
                elif j == 0:
                    dp[j] = 1
                else:
                    dp[j] = foo(i, j, dp[j-1])
                ans = max(ans, dp[j])
            print(dp)
        return ans ** 2

    def maximalSquare_kamyu(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in xrange(n)] for i in xrange(2)]
        max_size = 0

        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i % 2][0] = 1
            else:
                size[i % 2][0] = 0
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i % 2][j] = min(size[i % 2][j - 1], \
                                         size[(i - 1) % 2][j], \
                                         size[(i - 1) % 2][j - 1]) + 1
                    max_size = max(max_size, size[i % 2][j])
                else:
                    size[i % 2][j] = 0

        return max_size * max_size


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
        size = [[0 for j in xrange(n)] for i in xrange(m)]
        max_size = 0

        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i][0] = 1
            else:
                size[i][0] = 0
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i][j] = min(size[i][j - 1],  \
                                     size[i - 1][j],  \
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
        table = [[[0, 0] for j in xrange(len(matrix[0]))] \
                         for i in xrange(len(matrix))]
        for i in reversed(xrange(len(matrix))):
            for j in reversed(xrange(len(matrix[i]))):
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
        s = [[0 for j in xrange(len(matrix[0]))] \
                for i in xrange(len(matrix))]
        max_square_area = 0
        for i in reversed(xrange(len(matrix))):
            for j in reversed(xrange(len(matrix[i]))):
                side = min(table[i][j][H], table[i][j][W])
                if matrix[i][j] == '1':
                    # Get the length of largest square with bottom-left corner (i, j).
                    if i + 1 < len(matrix) and j + 1 < len(matrix[i + 1]):
                        side = min(s[i + 1][j + 1] + 1, side)
                    s[i][j] = side
                    max_square_area = max(max_square_area, side * side)

        return max_square_area;

print(Solution().maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]))