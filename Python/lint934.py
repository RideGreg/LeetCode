class Solution:
    """
    @param n: the number of keys
    @param m: the number of locks
    @return: the numbers of open locks
    """
    def unlock(self, n, m):
        if n == 1: return m
        def divi(i, n):
            return sum(1 for j in xrange(1, min(n, i)+1) if i%j==0)
        dp, ans = [0], 0
        for i in xrange(1, m + 1):
            if i%2:
                cur = divi(i, n)%2
            else:
                cur = dp[i/2]
                if n>=i:
                    cur += 1
                if (i/2)%2 and i != 2:
                    cur += 1
                cur %= 2
            dp.append(cur)
            ans += cur
        return ans

print Solution().unlock(10,10)
print Solution().unlock(2,5)