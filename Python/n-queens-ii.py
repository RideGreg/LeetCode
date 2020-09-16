# Time:  O(n!)
# Space: O(n)
#
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.
#

class Solution:
    # @return an integer
    def totalNQueens(self, n: int) -> int: # USE THIS 64ms: no need maintain board, since only ask total # valid
        def canPlace(x, y):
            return not col[y] and not diag[y-x+n] and not adiag[x+y]

        # i: place a Q in ith row
        def backtrack(i):
            if i == n:
                self.ans += 1
            else:
                for j in range(n):
                    if canPlace(i, j):
                        col[j] = diag[j-i+n] = adiag[i+j] = True
                        backtrack(i+1)
                        col[j] = diag[j-i+n] = adiag[i+j] = False

        self.ans = 0
        col, diag, adiag = [False]*n, [False]*2*n, [False]*2*n
        backtrack(0)
        return self.ans

    # 3200ms very slow. When Q is placed in a row, we shouldn't check remaining cells on the same row.
    def totalNQueens2(self, n):
        def canPlace(x, y):
            return not row[x] and not col[y] and not diag[y - x + n] and not adiag[x + y]

        # i: how many Q were placed, startPos: from 0 to n^2-1, which cell to check next?
        def backtrack(i, startPos):
            if i == n:
                self.ans += 1
            else:
                for pos in range(startPos, n ** 2):
                    x, y = divmod(pos, n)
                    if canPlace(x, y):
                        row[x] = col[y] = diag[y - x + n] = adiag[x + y] = True
                        backtrack(i + 1, pos + 1)
                        row[x] = col[y] = diag[y - x + n] = adiag[x + y] = False

        self.ans = 0
        row, col, diag, adiag = [False] * n, [False] * n, [False] * 2 * n, [False] * 2 * n
        backtrack(0, 0)
        return self.ans

# similar to solution 1, but use return value not global var self.ans.
class Solution2:
    def totalNQueens(self, n):
        self.cols = [False] * n
        self.main_diag = [False] * (2 * n)
        self.anti_diag = [False] * (2 * n)
        return self.totalNQueensRecu([], 0, n)

    def totalNQueensRecu(self, solution, row, n):
        if row == n:
            return 1
        result = 0
        for i in range(n):
            if not self.cols[i] and not self.main_diag[row + i] and not self.anti_diag[row - i + n]:
                self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = True
                result += self.totalNQueensRecu(solution + [i], row + 1, n)
                self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = False
        return result


if __name__ == "__main__":
    print(Solution().totalNQueens(4)) # 2
    print(Solution().totalNQueens(8)) # 92
