# Time:  O(n^2)
# Space: O(n)

# 1301 biweekly contest 16 12/28/2019

# Given a square board of chars. You move on the board from the bottom right square marked with the char 'S'.
#
# You need to reach the top left square marked with the char 'E'. The rest of the squares are labeled
# either with a numeric char 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or
# up-left (diagonally) only if there is no obstacle there.
#
# Return a list of two integers: the first integer is the maximum sum of numeric chars you can collect,
# and the second is the # of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
#
# In case there is no path, return [0, 0].

# Constraints:
# 2 <= board.length == board[i].length <= 100

class Solution(object):
    def pathsWithMaxScore(self, board): # USE THIS
        M, n = 10**9+7, len(board)
        dp = [[0, 0] for _ in range(n+1)] # bottom pad row, right pad column, so all cells processed uniformly
        for i in range(n-1, -1, -1):
            ndp = [[0, 0] for _ in range(n+1)]
            for j in range(n-1, -1, -1):
                if board[i][j] == 'S':
                    ndp[j] = [0, 1]
                elif board[i][j] != 'X':
                    for score, ways in (ndp[j+1], dp[j+1], dp[j]):
                        if score > ndp[j][0]:
                            ndp[j] = [score, ways]
                        elif score == ndp[j][0]:
                            ndp[j][1] = (ndp[j][1] + ways) % M
                    if ndp[j][1] and board[i][j] != 'E':
                        ndp[j][0] += int(board[i][j])
            dp = ndp
        return dp[0]


    def pathsWithMaxScore_kamyu(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9+7
        directions = [[1, 0], [0, 1], [1, 1]]
        dp = [[[0, 0] for r in range(len(board[0])+1)] for r in range(2)]
        dp[(len(board)-1)%2][len(board[0])-1] = [0, 1]
        for r in reversed(range(len(board))):
            for c in reversed(range(len(board[0]))):
                if board[r][c] in "XS":
                    continue
                dp[r%2][c] = [0, 0]   # BAD: need to reset as reusing two rows
                for dr, dc in directions:
                    if dp[r%2][c][0] < dp[(r+dr)%2][c+dc][0]:
                        dp[r%2][c] = dp[(r+dr)%2][c+dc][:]
                    elif dp[r%2][c][0] == dp[(r+dr)%2][c+dc][0]:
                        dp[r%2][c][1] = (dp[r%2][c][1]+dp[(r+dr)%2][c+dc][1]) % MOD
                if dp[r%2][c][1] and board[r][c] != 'E':
                    dp[r%2][c][0] += int(board[r][c])
        return dp[0][0]

print(Solution().pathsWithMaxScore(["E23","2X2","12S"])) # [7,1]
# E23
# 2X2
# 12S
print(Solution().pathsWithMaxScore(["E12","1X1","21S"])) # [4,2]
print(Solution().pathsWithMaxScore(["E11","XXX","11S"])) # [0,0]
