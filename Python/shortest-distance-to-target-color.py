# Time:  O(n)
# Space: O(n)

# 1182 biweekly contest 8 9/7/2019

# You are given an array colors, in which there are three colors: 1, 2 and 3.
#
# You are also given some queries. Each query consists of two integers i and c, return the shortest distance
# between the given index i and the target color c. If there is no solution return -1.

# 1 <= colors.length, queries.length <= 5*10^4

# Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
# Output: [3,0,3]

try:
    xrange
except NameError:
    xrange = range

class Solution(object):
    # dp[c][j] distance from nearest color c to jth elem
    def shortestDistanceColor(self, colors, queries):
        N = len(colors)
        dp = [[float('inf')] * N for _ in xrange(4)]

        # forward pass, get nearest to the left
        dp[colors[0]][0] = 0
        for i in range(1, N):
            for c in range(1, 4):
                dp[c][i] = 1 + dp[c][i-1]
            dp[colors[i]][i] = 0

        # backward pass, get nearest to the right
        for i in reversed(range(N-1)):
            for c in range(1, 4):
                dp[c][i] = min(dp[c][i], dp[c][i+1] + 1)

        return [dp[c][i] if dp[c][i] != float('inf') else -1 for i, c in queries]

    # dp[c][j] index of nearest color c to jth elem
    def shortestDistanceColor_kamyu(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        N = len(colors)
        dp = [[-1] * N for _ in xrange(4)]

        dp[colors[0]][0] = 0
        for i in xrange(1, N):
            for color in xrange(1, 4):
                dp[color][i] = dp[color][i-1]
            dp[colors[i]][i] = i

        for i in reversed(xrange(N-1)):
            for color in xrange(1, 4):
                if dp[color][i+1] == -1:
                    continue
                if dp[color][i] == -1 or \
                   abs(dp[color][i+1]-i) < abs(dp[color][i]-i):
                    dp[color][i] = dp[color][i+1]
         
        return [abs(dp[color][i]-i) if dp[color][i] != -1 else -1 \
                    for i, color in queries]

print(Solution().shortestDistanceColor([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]])) # [3,0,3]
print(Solution().shortestDistanceColor([1,2], [[0,3]])) # [-1]