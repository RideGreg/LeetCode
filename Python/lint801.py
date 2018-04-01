class Solution:
    """
    @param n: the money you have
    @return: the minimum money you have to give
    """
    def backPackX(self, n):
        # write your code here
        dp = [0 for _ in xrange(n+1)
        for j in [150, 250, 350]:
            for i in xrange(j, n+1):
                dp[i] = max(dp[i], j + dp[i-j])
        return n - dp[-1]

print Solution().backPackX(900)