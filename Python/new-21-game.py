# Time:  O(N+W)
# Space: O(N+W)
# we can reduce the time complexity to O(max(K,W)) and the space complexity to O(W)
# by only keeping track of the last WW values of dp, but it isn't required.

# 837
# Alice plays the following game, loosely based on the card game "21".
#
# Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw,
# she gains an integer number of points randomly from the range [1, W], where W is an integer.
# Each draw is independent and the outcomes have equal probabilities.
#
# Alice stops drawing numbers when she gets K or more points.  What is the probability that she has
# N or less points?
#   0 <= K <= N <= 10000
#   1 <= W <= 10000

# DP: The probability that Alice wins the game is only related to how many points x she starts
# the next draw with, so we can try to formulate an answer in terms of x.
#
# Let f(x) be the answer when we already have x points. When she has between K and N points,
# then she stops drawing and wins. If she has more than N points, then she loses.
#
# The key recursion is f(x) = (1/W) * (f(x+1) + f(x+2) + ... + f(x+W))
# # This is because there is a probability of 1/W to draw each card from 1 to W.
#
# With this recursion, we could do a naive dynamic programming solution as follows:
# #psuedocode
# dp[k] = 1.0 when K <= k <= N, else 0.0
# # dp[x] = the answer when Alice has x points
#
# for k from K-1 to 0:
#     dp[k] = (dp[k+1] + ... + dp[k+W]) / W
# return dp[0]
#
# This leads to a solution with O(K*W + (N-K)) time complexity, which isn't efficient enough.
# Every calculation of dp[k] does O(W) work, but the work is quite similar.
#
# Actually, the difference is f(x) - f(x-1) = (1/W) * ( f(x+W) - f(x)). This allows us to
# calculate subsequent f(k)'s in O(1) time, by maintaining the numerator S=f(x+1)+f(x+2)+...+f(x+W).
#
# As we calculate each dp[k] = S / W, we maintain the correct value of S => S + f(k) - f(k+W).

class Solution(object):
    def new21Game(self, N, K, W):
        dp = [0.0] * (N + W + 1)
        # dp[x] = the answer when Alice has x points
        for k in range(K, N + 1):
            dp[k] = 1.0

        S = min(N - K + 1, W)
        # i.e. S = dp[k+1] + dp[k+2] + ... + dp[k+W], for initial value k=K-1, dp[K]+..+dp[N] have min(N-K+1, W) 1.0
        for k in range(K - 1, -1, -1):
            dp[k] = S / float(W)
            S += dp[k] - dp[k + W]

        return dp[0]

    # Time O(NW), forward DP. LTE for new21Game(9811, 8776, 1096).
    def new21Game_ming(self, N: int, K: int, W: int) -> float:
        if N >= K-1+W:
            return 1.0

        dp = [0.0] * (K+W)
        dp[0] = 1.0

        # continue to draw a new number if points < K.
        for i in range(K):
            for delta in range(1, W+1):
                dp[i+delta] += dp[i]/W
        return sum(dp[K:N+1])

print(Solution().new21Game(10, 1, 10)) # 1.000
print(Solution().new21Game(6, 1, 10)) # 0.600
print(Solution().new21Game(6, 2, 10)) # 0.550
print(Solution().new21Game(21, 17, 10)) # 0.73278
print(Solution().new21Game(9811, 8776, 1096)) # 0.996956 LTE for forward solution.