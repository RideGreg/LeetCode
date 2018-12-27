class Solution(object):
    '''
    I. There are n coins in a line. Two players take turns to take one or two coins from right side
    until there are no more coins left. The player who take the last coin wins.
    Could you please decide the first play will win or lose?
    Example
    n = 1, return true.
    n = 2, return true.
    n = 3, return false.
    n = 4, return true.
    n = 5, return true.

    Solution: dp[i] is whether first player wins when i coins left. dp[i] is True if dp[i-1] or db[i-2] is False.
              dp[i] is False if dp[i-1] and dp[i-2] are True.
    '''
    def coinsI(self, n):
        if n==0: return False
        prev, curr = False, True
        for _ in xrange(2, n+1):
            prev, curr = curr, not prev or not curr
        return curr
        '''
        dp = [False, True]
        for i in xrange(2, n+1):
            dp[i%2] = not dp[(i+1)%2] or not dp[i%2]
        return dp[n%2]
        '''
        '''
        dp = [False, True]
        for i in xrange(2, n+1):
            dp.append(not dp[-1] or not dp[-2])
        return dp[n]
        '''

    '''
    II. There are n coins with different value in a line. Two players take turns to take one or two coins from left side 
    until there are no more coins left. The player who take the coins with the most value wins.
    Could you please decide the first player will win or lose?
    Example: Given [1,2,4], return false. Given [5,1,2,10], return True.
    
    Solution: dp[i] is the most value first player can get when i coins left, postfixSum[i] is the total
    of i coins left. dp[i] = postfixSum[i] - min(dp[i-1], dp[i-2]). return True if dp[n] * 2 >= allsum
    '''
    def coinsII(self, coins):
        if len(coins) <= 2: return True

        postfixSum = [0]*(len(coins)+1)
        dp = [0]*(len(coins)+1)
        postfixSum[1] = dp[1] = coins[-1]

        for i in xrange(2,len(coins)+1):
            postfixSum[i] = coins[-i] + postfixSum[i-1]
            dp[i] = postfixSum[i] - min(dp[i-1], dp[i-2])

        print dp[-1]
        return dp[-1] * 2 >= sum(coins)

        '''
        n = len(coins)
        if n <= 2: return True

        sums = [0] * (n + 1)
        for i, c in enumerate(coins):
            sums[i+1] = sums[i] + c
        prev, curr = 0, coins[-1]
        for i in xrange(2, n+1): # i coins left
            prev, curr = curr, (sums[-1]-sums[-1-i]) - min(prev, curr)

        print curr
        return curr * 2 >= sums[-1]
        '''

    ''''
    III.  There are n coins in a line. Two players take turns to take a coin from one of the ends of the line 
    until there are no more coins left. The player with the larger amount of money wins. Could you please decide 
    the first player will win or lose? Example
    Given array A = [3,2,2], return true.
    Given array A = [1,2,4], return true.
    Given array A = [1,20,4], return false.
    
    Solution: dp[i][j] is the most value first player can get when i to j coins left, sums[i][j] is the total
    when i to j coins left. dp[i][j] = sum[i][j] - min(dp[i+1][j], dp[i][j-1])
    Initialize dp[i][i] = coins[i], return dp[0][n-1]
    '''
    def coinsIII(self, coins):
        n = len(coins)
        sums = [0] * (n+1)
        for i, c in enumerate(coins):
            sums[i+1] = sums[i]+c
        dp = [0]*n
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if i == j:
                    dp[j] = coins[i]
                else:
                    dp[j] = (sums[j+1]-sums[i]) - min(dp[j], dp[j-1])

        print dp[n-1]
        return dp[n-1]*2 >= sums[-1]
        '''
        n = len(coins)
        dp = [[0]*n for _ in xrange(n)]
        sums = [0] * (n+1)
        for i, c in enumerate(coins):
            sums[i+1] = sums[i]+c
            dp[i][i] = c
        for i in reversed(xrange(n-1)):
            for j in xrange(i+1, n):
                dp[i][j] = (sums[j+1]-sums[i]) - min(dp[i+1][j], dp[i][j-1])

        print dp[0][n-1]
        return dp[0][n-1] * 2 >= sums[-1]
        '''

print Solution().coinsI(0) #False
print Solution().coinsI(1) #True
print Solution().coinsI(2) #True
print Solution().coinsI(3) #False
print Solution().coinsI(4) #True
print Solution().coinsI(5) #True
print Solution().coinsI(6) #False

print Solution().coinsII([1,2,4]) #3 False
print Solution().coinsII([5,1,2,10]) #15 True

print Solution().coinsIII([3,2,2]) #5 True
print Solution().coinsIII([1,2,4]) #5 True
print Solution().coinsIII([1,20,4]) #5 False
