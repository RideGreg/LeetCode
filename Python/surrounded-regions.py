# Time:  O(m * n)
# Space: O(m + n)

# 130
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#

# Solution: There are 2 types of 'X': surrounded and connected-to-boarder. It is difficult to
# find surrounded 'X' by DFS/BFS because it can only be determined later if the 'X' connects to
# boarder. A good way is to start with four sides and find all 'X' connecting to boarder, mark
# them using another letter, then all remaining 'X' is surrounded 'X'.

import collections


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        q = collections.deque()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == 'O':
                    board[i][j] = 'V'
                    q.append((i, j))

        for j in range(1, n-1):
            for i in [0, m-1]:
                if board[i][j] == 'O':
                    board[i][j] = 'V'
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < len(boardn and \
                   board[x][y] == 'O':
                    board[x][y] = 'V'
                    q.append((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

if __name__ == "__main__":
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    Solution().solve(board)
    print board
