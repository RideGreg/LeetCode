# Time:  O(n^2), n is the number of steps
# Space: O(n)

# 1269 weekly contest 164 11/23/2019

# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left,
# 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).
#
# Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.
#
# Since the answer may be too large, return it modulo 10^9 + 7.

class Solution(object):
    def numWays(self, steps: int, arrLen: int) -> int: # USE THIS (dict, not array): no need to allocate space for positions won't be reached
        import collections
        MOD, dp = 10**9+7, {0:1}
        for _ in range(steps):
            ndp = collections.defaultdict(int)
            for k,v in dp.items():
                ndp[k]= (ndp[k] + v) % MOD
                if k>0:
                    ndp[k-1] = (ndp[k-1] + v) % MOD
                if k<arrLen-1:
                    ndp[k+1] = (ndp[k+1] + v) % MOD
            dp = ndp

        return dp[0]%MOD


    def numWays_kamyu(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = int(1e9+7)
        l = min(1+steps//2, arrLen)
        dp = [0]*(l+2)
        dp[1] = 1
        while steps > 0:
            steps -= 1
            new_dp = [0]*(l+2)
            for i in xrange(1, l+1):
                new_dp[i] = (dp[i] + dp[i-1] + dp[i+1]) % MOD
            dp = new_dp
        return dp[1]

print(Solution().numWays(3,2)) # 4
print(Solution().numWays(2,4)) # 2
print(Solution().numWays(4,2)) # 8