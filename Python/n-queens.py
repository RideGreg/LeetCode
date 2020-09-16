# Time:  O(n!), n possibility for 1st Queen, n-2 possibility for 2nd Queen,
#               n-4 possibility for 3rd Queen
# Space: O(n), record row/col/diag/adiag information.

# 51
# The n-queens puzzle is the problem of placing n queens on
# an nxn chess board such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution(object):
    # USE THIS 60ms: When Q is placed in a row, no need to check remaining cells on the same row.
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def canPlace(x, y):
            return not col[y] and not diag[y-x+n] and not adiag[x+y]

        # i: place a Q in ith row
        def backtrack(i):
            if i == n:
                ans.append([''.join(r) for r in board])
            else:
                for j in range(n):
                    if canPlace(i, j):
                        col[j] = diag[j-i+n] = adiag[i+j] = True
                        board[i][j] = 'Q'
                        backtrack(i+1)
                        board[i][j] = '.'
                        col[j] = diag[j-i+n] = adiag[i+j] = False

        ans, board = [], [['.']*n for _ in range(n)]
        col, diag, adiag = [False]*n, [False]*2*n, [False]*2*n
        backtrack(0)
        return ans


    def solveNQueens2(self, n): # 60ms: 4 lists to remember which row/col/diag/anti-diag already have Q in it
                                # row check can be skipped, because in each backtrack, we only check positions in current row
        def canPlace(x, y):
            return not row[x] and not col[y] and not diag[y-x+n] and not adiag[x+y]

        # i: how many Q were placed, startPos: from 0 to n^2-1, which cell to check next?
        def backtrack(i, startPos):
            if i == n:
                ans.append([''.join(r) for r in board])
            else:
                # should only check current row. If current row cannot place, we already fail.
                for pos in range(startPos, startPos + n): # no need to check all for pos in range(startPos, n**2)
                    x, y = divmod(pos, n)
                    if canPlace(x, y):
                        row[x] = col[y] = diag[y-x+n] = adiag[x+y] = True
                        board[x][y] = 'Q'
                        backtrack(i+1, (x+1)*n) # next position should be first place in next row
                        board[x][y] = '.'
                        row[x] = col[y] = diag[y-x+n] = adiag[x+y] = False

        ans, board = [], [['.']*n for _ in range(n)]
        row, col, diag, adiag = [False]*n, [False]*n, [False]*2*n, [False]*2*n
        backtrack(0, 0)
        return ans


    def solveNQueens3(self, n): # similar to solution 1, fast
        def dfs(curr, cols, main_diag, anti_diag, result):
            row, n = len(curr), len(cols)
            if row == n:
                result.append(map(lambda x: '.'*x + "Q" + '.'*(n-x-1), curr))
                return
            for i in xrange(n):
                if cols[i] or main_diag[row+i] or anti_diag[row-i+n]:
                    continue
                cols[i] = main_diag[row+i] = anti_diag[row-i+n] = True
                curr.append(i)
                dfs(curr, cols, main_diag, anti_diag, result)
                curr.pop()
                cols[i] = main_diag[row+i] = anti_diag[row-i+n] = False

        result = []
        cols, main_diag, anti_diag = [False]*n, [False]*(2*n), [False]*(2*n)
        dfs([], cols, main_diag, anti_diag, result)
        return result


# For any point (x,y), if we want the new point (p,q) don't share the same row, column, or diagonal.
# then there must have ```p+q != x+y``` and ```p-q!= x-y```
# the former focus on eliminate 'left bottom right top' diagonal;
# the latter focus on eliminate 'left top right bottom' diagonal

# - col_per_row: the list of column index per row
# - cur_row：current row we are seraching for valid column
# - xy_diff：the list of x-y
# - xy_sum：the list of x+y
    def solveNQueens4(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(col_per_row, xy_diff, xy_sum):
            cur_row = len(col_per_row)
            if cur_row == n:
                ress.append(col_per_row)
            for col in range(n):
                if col not in col_per_row and cur_row-col not in xy_diff and cur_row+col not in xy_sum:
                    dfs(col_per_row+[col], xy_diff+[cur_row-col], xy_sum+[cur_row+col])
        ress = []
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in res] for res in ress]

                    
if __name__ == "__main__":
    print(Solution().solveNQueens(4))
    # [['.Q..',
    #   '...Q',
    #   'Q...',
    #   '..Q.'],
    #
    #  ['..Q.',
    #   'Q...',
    #   '...Q',
    #   '.Q..']]
