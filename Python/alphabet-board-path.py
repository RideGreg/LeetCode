# Time:  O(n)
# Space: O(1)

# 1138 weekly contest 147 7/27/2019
# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
#
# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.
# a b c d e
# f g h i j
# k l m n o
# p q r s t
# u v w x y
# z

# We may make the following moves:
#
# 'U''D''L''R' moves our position up one row, down one row, left one column,
# right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)
#
# Return a sequence of moves that makes our answer equal to target in the minimum
# number of moves.  You may return any path that does so.

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x, y = 0, 0
        ans = []
        for c in target:
            nx, ny = divmod(ord(c)-ord('a'), 5)
            ans.append('U' * max(x-nx, 0))
            ans.append('L' * max(y-ny, 0))
            ans.append('R' * max(ny-y, 0))
            ans.append('D' * max(nx-x, 0))
            ans.append('!')
            x, y = nx, ny
        return "".join(ans)

    def alphabetBoardPath_wrong(self, target): # WRONG CASE 'zqz' => DDDDD!UUR!DDL!
        ans = []
        x, y = 0, 0
        for c in target:
            nx, ny = divmod(ord(c)-ord('a'), 5)
            di = 'D' if nx >= x else 'U'
            ans.append(di*abs(nx-x))
            di = 'R' if ny >= y else 'L'
            ans.append(di*abs(ny-y))
            ans.append('!')
            x, y = nx, ny
        return ''.join(ans)

print(Solution().alphabetBoardPath('zqz')) # DDDDD!UUR!LDD!  EDGE CASE!!!!
print(Solution().alphabetBoardPath('leet')) # DDR!UURRR!!DDD!
print(Solution().alphabetBoardPath('code')) # RR!DDRR!UUL!R!