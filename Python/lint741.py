class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def maxValue(self, str):
        def calc(a, b):
            if a*b==0 or a==1 or b==1:
                return a+b
            else:
                return a*b

        sz = len(str)
        dp = [[-1]*sz for _ in xrange(sz)]
        for i in reversed(xrange(sz)):
            for j in xrange(i, sz):
                if i == j:
                    dp[i][i] = int(str[i])
                else:
                    for k in xrange(i,j):
                        dp[i][j] = max(dp[i][j], calc(dp[i][k], dp[k+1][j]))
        return dp[0][-1]

print Solution().maxValue('891')
print Solution().maxValue('01231')

