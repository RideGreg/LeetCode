# Time:  O(n^2)
# Space: O(n^2)

# 375
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
#
# However, when you guess a particular number x, and you guess wrong,
# you pay $x. You win the game when you guess the number I picked.
#
# Example:
#
# n = 10, I pick 8.
#
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
#
# Game over. 8 is the number I picked.
#
# You end up paying $5 + $7 + $9 = $21. ACTUALLY this is NOT the best strategy,
# the best is to pick 7, then if higher, pick 9, if lower, pick 3->5 => total is 16.
#
# Given a particular n >= 1, find out how much money you need to have to guarantee a win.
#
# Hint:
#
# 1. The best strategy to play the game is to minimize the maximum loss
# you could possibly face. Another strategy is to minimize the expected loss.
# Here, we are interested in the first scenario.
# 2. Take a small example (n = 3). What do you end up paying in the worst case?
# 3. Check out https://en.wikipedia.org/wiki/Minimax if you're still stuck.
# 4. The purely recursive implementation of minimax would be worthless (very expensive)
# for even a small n. You MUST use dynamic programming.
# 5. As a follow-up, how would you modify your code to solve the problem of
# minimizing the expected loss, instead of the worst-case loss?


# 状态转移方程：
# dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]))
# 其中dp[i][j]表示猜出范围[i, j]的数字需要花费的最少金额
# each cell only depends on cells which are to the left of it and below it
# two different traverse both work

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for gap in range(1, n):
            for lo in range(1, n+1-gap):
                hi = lo + gap
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi])
                                   for x in range(lo, hi))
        return dp[1][n]


    def getMoneyAmount2(self, n):
        dp = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                dp[lo][hi] = min(x + max(dp[lo][x - 1], dp[x + 1][hi])
                                   for x in range(lo, hi))
        return dp[1][n]

print(Solution().getMoneyAmount(5)) # 6: best steps: 2->4, not BST: 3->4
print(Solution().getMoneyAmount(10)) # 16: best steps: 7->if higher 9, if lower 3->5