# Time:  O(1)
# Space: O(1)

# 1275
# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
#
# Here are the rules of Tic-Tac-Toe:
#
# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters, while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid
# where they mark their respective character in the order in which A and B play.
#
# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw",
# if there are still movements to play return "Pending".
#
# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.
#
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def check(x, y, c):
            return board[x][0]==board[x][1]==board[x][2] \
                or board[0][y]==board[1][y]==board[2][y] \
                or board[0][0]==board[1][1]==board[2][2]==c \
                or board[0][2]==board[1][1]==board[2][0]==c


        board = [['.']*3 for _ in range(3)]
        for i, (x,y) in enumerate(moves):
            c = 'A' if i % 2 == 0 else 'B'
            board[x][y] = c
            if check(x, y, c):
                return c
        return 'Draw' if len(moves) == 9 else 'Pending'

    def tictactoe_kamyu(self, moves):
        row, col = [[0]*3 for _ in xrange(2)], [[0]*3 for _ in xrange(2)]
        diag, anti_diag = [0]*2, [0]*2
        p = 0
        for r, c in moves:
            row[p][r] += 1
            col[p][c] += 1
            diag[p] += r == c
            anti_diag[p] += r+c == 2
            if 3 in (row[p][r], col[p][c], diag[p], anti_diag[p]):
                return "AB"[p]
            p ^= 1
        return "Draw" if len(moves) == 9 else "Pending"

print(Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])) # A
print(Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])) # B
print(Solution().tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])) # Draw
print(Solution().tictactoe([[0,0],[1,1]])) # Pending