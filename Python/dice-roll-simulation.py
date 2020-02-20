# Time:  O(m * n), m is the max of rollMax
# Space: O(m)

# 1223 weekly contest 158 10/12/2019

# A die simulator generates a random number from 1 to 6 for each roll. You introduced a
# constraint to the generator such that it cannot roll the number i more than rollMax[i]
# (1-indexed) consecutive times.
#
# Given an array of integers rollMax and an integer n, return the # of distinct sequences
# that can be obtained with exact n rolls.
#
# Two sequences are considered different if at least one element differs from each other.
# Since the answer may be too large, return it modulo 10^9 + 7.

# 1 <= n <= 5000
# rollMax.length == 6
# 1 <= rollMax[i] <= 15

# dp[i][k] means after several rolls,
# the number of sequence that ends with k times i.

try:
    xrange
except NameError:
    xrange = range

class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [[0, 1] + [0] * (rollMax[i]-1) for i in xrange(6)]
        for _ in xrange(n - 1):
            dp2 = [[0] * (rollMax[i]+1) for i in xrange(6)]
            for i in xrange(6):
                for k in xrange(1, rollMax[i] + 1):
                    if dp[i][k] == 0: continue
                    for j in xrange(6): # k times i, then one j
                        if i == j:
                            if k < rollMax[i]:
                                dp2[j][k + 1] += dp[i][k] % mod
                        else:
                            dp2[j][1] += dp[i][k] % mod
            dp = dp2
        return sum(sum(row) for row in dp) % mod

    # DFS: traverse all valid permutation O(2^n)
    def dieSimulator_TLE(self, n, rollMax):
        def dfs(rolls, last, curLen):
            if rolls == n:
                self.ans += 1
                return

            for i in range(6):
                if i == last and curLen == rollMax[i]:
                    continue
                dfs(rolls+1, i, curLen+1 if i==last else 1)

        self.ans = 0
        dfs(0, -1, 0)
        return self.ans

print(Solution().dieSimulator(2, [1,1,2,2,2,3])) #34
# number 1: [0 5 0]
# number 2: [0 5 0]
# number 3: [0 5 1]
# number 4: [0 5 1]
# number 5: [0 5 1]
# number 6: [0 5 1]
print(Solution().dieSimulator(2, [1,1,1,1,1,1])) #30
print(Solution().dieSimulator(3, [1,1,1,2,2,3])) #181