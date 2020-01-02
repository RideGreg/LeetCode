# Time:  O(9^2)
# Space: O(9)

# 36
# Determine if a Sudoku is valid,
# according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled,
# where empty cells are filled with the character '.'.
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for r in board:
            if not self.isValidList(r): return False
        for c in zip(*board):
            if not self.isValidList(c): return False
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValidList(box):
                    return False
        return True

    def isValidList(self, xs):
        xs = [x for x in xs if x != '.']  #list(filter(lambda x: x != '.', xs))
        return len(set(xs)) == len(xs)


if __name__ == "__main__":
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    print(Solution().isValidSudoku(board)) # True
