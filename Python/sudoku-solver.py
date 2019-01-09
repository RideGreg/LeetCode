# Time:  ((9!)^9)
# Space: (1)
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
#

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku2(self, board):
        def isValid(board, x, y):
            for i in xrange(9):
                if i != x and board[i][y] == board[x][y]:
                    return False
            for j in xrange(9):
                if j != y and board[x][j] == board[x][y]:
                    return False
            i = 3 * (x / 3)
            while i < 3 * (x / 3 + 1):
                j = 3 * (y / 3)
                while j < 3 * (y / 3 + 1):
                    if (i != x or j != y) and board[i][j] == board[x][y]:
                        return False
                    j += 1
                i += 1
            return True

        def solver(board):
            for i in xrange(len(board)):   # this is bad: each time iterate all cells
                for j in xrange(len(board[0])):
                    if(board[i][j] == '.'):
                        for k in xrange(9):
                            board[i][j] = chr(ord('1') + k)
                            if isValid(board, i, j) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        solver(board)

    # USE THIS
    def solveSudoku(self, board):
        def canUse(i, j, v):
            if v in board[i] or v in zip(*board)[j]:
                return False
            xstart, ystart = i // 3 * 3, j // 3 * 3 # made a mistake by not time 3
            for x in xrange(xstart, xstart + 3):
                for y in xrange(ystart, ystart + 3):
                    if board[x][y] == v:
                        return False
            return True

        def backtrack(m):
            for n in xrange(m, 81):
                i, j = divmod(n, 9)
                if board[i][j] == '.':
                    for z in xrange(9):
                        v = chr(z+ord('1'))
                        if canUse(i, j, v):
                            board[i][j] = v
                            if backtrack(n + 1):
                                return True
                            board[i][j] = '.'

                    return False
            return True

        backtrack(0)

print(Solution().solveSudoku([[0,0,9,7,4,8,0,0,0],
                              [7,0,0,0,0,0,0,0,0],
                              [0,2,0,1,0,9,0,0,0],
                              [0,0,7,0,0,0,2,4,0],
                              [0,6,4,0,1,0,5,9,0],
                              [0,9,8,0,0,0,3,0,0],
                              [0,0,0,8,0,3,0,2,0],
                              [0,0,0,0,0,0,0,0,6],
                              [0,0,0,2,7,5,9,0,0]]))