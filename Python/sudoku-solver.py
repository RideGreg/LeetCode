# Time:  ((9!)^9), each row to fill 9 cells,  we have 9! cases; all 9 rows are independent and combined.
# Space: (1)
# 37
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
#

from itertools import product
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):  # USE THIS: one optimization is to record what numbers were used
                                   # in the 9 rows, 9 cols, 9 boxes.
        def backtrack(i):
            if i == len(empty): return True

            x, y = empty[i]
            cand = set(map(str, range(1, 10)))
            for z in range(9):
                cand.discard(board[x][z])
                cand.discard(board[z][y])
            bx, by = x//3 * 3, y//3 * 3
            for dx, dy in product(range(3), repeat=2):
                cand.discard(board[bx+dx][by+dy])

            for v in cand:
                board[x][y] = v
                if backtrack(i+1):
                    return True
                board[x][y] = '.'
            return False

        empty = [(x,y) for x in range(9) for y in range(9) if board[x][y] == '.']
        backtrack(0)


    def solveSudoku2(self, board):
        def canUse(i, j, v):
            if v in board[i] or v in zip(*board)[j]:
                return False
            xstart, ystart = i // 3 * 3, j // 3 * 3 # made a mistake by not time 3
            for x in range(xstart, xstart + 3):
                for y in range(ystart, ystart + 3):
                    if board[x][y] == v:
                        return False
            return True

        def backtrack(m):
            for n in range(m, 81): # if n is not '.', go to next cell
                i, j = divmod(n, 9)
                if board[i][j] == '.':
                    for z in range(9):
                        v = chr(z+ord('1'))
                        if canUse(i, j, v):
                            board[i][j] = v
                            if backtrack(n + 1):
                                return True
                            board[i][j] = '.'

                    return False
            return True

        backtrack(0)


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print(board)
'''[
["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]
'''
print(Solution().solveSudoku([[0,0,9,7,4,8,0,0,0],
                              [7,0,0,0,0,0,0,0,0],
                              [0,2,0,1,0,9,0,0,0],
                              [0,0,7,0,0,0,2,4,0],
                              [0,6,4,0,1,0,5,9,0],
                              [0,9,8,0,0,0,3,0,0],
                              [0,0,0,8,0,3,0,2,0],
                              [0,0,0,0,0,0,0,0,6],
                              [0,0,0,2,7,5,9,0,0]]))