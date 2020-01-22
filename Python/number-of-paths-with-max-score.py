# Time:  O(n^2)
# Space: O(n)

# 1301 biweekly contest 16 12/28/2019

# You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.
#
# You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.
#
# Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
#
# In case there is no path, return [0, 0].

# Constraints:
# 2 <= board.length == board[i].length <= 100

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9+7
        directions = [[1, 0], [0, 1], [1, 1]]
        dp = [[[0, 0] for r in xrange(len(board[0])+1)]
              for r in xrange(2)]
        dp[(len(board)-1)%2][len(board[0])-1] = [0, 1]
        for r in reversed(xrange(len(board))):
            for c in reversed(xrange(len(board[0]))):
                if board[r][c] in "XS":
                    continue
                dp[r%2][c] = [0, 0]
                for dr, dc in directions:
                    if dp[r%2][c][0] < dp[(r+dr)%2][c+dc][0]:
                        dp[r%2][c] = dp[(r+dr)%2][c+dc][:]
                    elif dp[r%2][c][0] == dp[(r+dr)%2][c+dc][0]:
                        dp[r%2][c][1] = (dp[r%2][c][1]+dp[(r+dr)%2][c+dc][1]) % MOD
                if dp[r%2][c][1] and board[r][c] != 'E':
                    dp[r%2][c][0] += int(board[r][c])
        return dp[0][0]

print(Solution().pathsWithMaxScore(["E23","2X2","12S"])) # [7,1]
print(Solution().pathsWithMaxScore(["E12","1X1","21S"])) # [4,2]
print(Solution().pathsWithMaxScore(["E11","XXX","11S"])) # [0,0]
