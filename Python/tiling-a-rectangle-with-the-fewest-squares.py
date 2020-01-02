# Time:  O(n^2 * m^2 * m^(n * m)), given m < n
# Space: O(n * m)

# 1240 weekly contest 160 10/26/2019
# Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

# Constraints:
# 1 <= n, m <= 13

# solution: http://int-e.eu/~bf3/squares/young.cc
# cheat table: http://int-e.eu/~bf3/squares/young.txt
# special case which DP cannot solve: 11x13 (ans 6), 16x17 (ans 8), 16x19 (ans 7)

import itertools

class Solution(object):
    def tilingRectangle_dp(self, n, m): # wrong, optimal cut for [11,13] has small square in the middle.
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        dp = [[float('inf')]*14 for _ in range(14)]
        dp[1] = list(range(14))
        for i in range(2, 14):
            dp[i][1] = i
            for j in range(i, 14):
                if j == i:
                    dp[i][j] = 1
                else:
                    for x in range(1, i//2+1):
                        dp[i][j] = min(dp[i][j], dp[x][j]+dp[i-x][j])
                    for y in range(1, j//2+1):
                        dp[i][j] = min(dp[i][j], dp[i][y]+dp[i][j-y])
                    dp[j][i] = dp[i][j]
        return dp[n][m]


    def tilingRectangle_bruteforce(self, R, C):
        if R > C: return self.tilingRectangle(C, R)
        ans = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
               [0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8],
               [0, 3, 3, 1, 4, 4, 2, 5, 5, 3, 6, 6, 4, 7],
               [0, 4, 2, 4, 1, 5, 3, 5, 2, 6, 4, 6, 3, 7],
               [0, 5, 4, 4, 5, 1, 5, 5, 5, 6, 2, 6, 6, 6],
               [0, 6, 3, 2, 3, 5, 1, 5, 4, 3, 4, 6, 2, 6],
               [0, 7, 5, 5, 5, 5, 5, 1, 7, 6, 6, 6, 6, 6],
               [0, 8, 4, 5, 2, 5, 4, 7, 1, 7, 5, 6, 3, 6],
               [0, 9, 6, 3, 6, 6, 3, 6, 7, 1, 6, 7, 4, 7],
               [0, 10, 5, 6, 4, 2, 4, 6, 5, 6, 1, 6, 5, 7],
               [0, 11, 7, 6, 6, 6, 6, 6, 6, 7, 6, 1, 7, 6],
               [0, 12, 6, 4, 3, 6, 2, 6, 3, 4, 5, 7, 1, 7],
               [0, 13, 8, 7, 7, 6, 6, 6, 6, 7, 7, 6, 7, 1]]
        return ans[R][C]

    def tilingRectangle(self, n, m): # USE THIS
        def find_maxlen(i, j):
            maxlen = 2
            # check all cells in rightmost column and bottom row are not filled
            while i+maxlen <= len(board) and \
                  j+maxlen <= len(board[0]) and \
                  all(board[r][j+maxlen-1] == 0 for r in range(i, i+maxlen)) and \
                  all(board[i+maxlen-1][c] == 0 for c in range(j, j+maxlen)):
                maxlen += 1
            return maxlen-1

        def fill(i, j, length, val):
            for r in range(i, i+length):
                for c in range(j, j+length):
                    board[r][c] = val

        def backtracking(count, row):
            if count >= self.ans:  # pruning
                return

            # product is equivalent to a nested for-loop!! Best way to break 2 loops is re-write 2 loops
            # to as 1 loop https://nedbatchelder.com/blog/201608/breaking_out_of_two_loops.html
            for i, j in itertools.product(range(row, len(board)), range(len(board[0]))):
                if not board[i][j]:
                    break
            else: # all cells are filled
                self.ans = min(self.ans, count)
                return

            maxlen = find_maxlen(i, j)
            for k in reversed(range(1, maxlen+1)):
                fill(i, j, k, 1)
                backtracking(count+1, i)
                fill(i, j, k, 0)


        if m > n:
            return self.tilingRectangle(m, n)
        board = [[0]*m for _ in range(n)]
        self.ans = float("inf")
        # count: how many rect used so far, row: starting row to check next empty cell
        count, row = 0, 0
        backtracking(count, row)
        return self.ans

print(Solution().tilingRectangle(2, 3)) # 3
print(Solution().tilingRectangle(5, 8)) # 5
print(Solution().tilingRectangle(11, 13)) # 6
# 7x7 4x4
#     4x4
#   1x1
# 6x6 5x5
