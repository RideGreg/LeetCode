# Time:  O(1)
# Space: O(1)

# 999
# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops,
# and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively.
# Uppercase characters represent white pieces, and lowercase characters represent black pieces.
#
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east,
# west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board,
# or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot
# move into the same square as other friendly bishops.
#
# Return the number of pawns the rook can capture in one move.

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = None, None
        for i in xrange(8):
            if r is not None:
                break
            for j in xrange(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break

        result = 0
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'p':
                    result += 1
                if board[nr][nc] != '.':
                    break
                nr, nc= nr+dr, nc+dc
        return result

print(Solution().numRookCaptures([
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","R",".",".",".","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]
])) # 3

print(Solution().numRookCaptures([
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    ["p","p",".","R",".","p","B","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","B",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."]
])) # 3
