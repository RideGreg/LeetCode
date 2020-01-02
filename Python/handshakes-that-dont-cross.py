# Time:  O(n)
# Space: O(1)

# 1259 biweekly contest 13 11/16/2019
# You are given an even number of people num_people that stand around a circle and each person
# shakes hands with someone else, so that there are num_people / 2 handshakes total.
#
# Return the number of ways these handshakes could occur such that none of the handshakes cross.
#
# Since this number could be very big, return the answer mod 10^9 + 7


class Solution(object):
    def numberOfWays(self, num_people):
        import functools, operator
        fact = lambda x,y: functools.reduce(operator.mul, range(x,y+1), 1)
        n = num_people // 2
        return fact(n+1,2*n) // fact(1,n+1)

    def numberOfWays_kamyu(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        MOD = 10**9+7
        def inv(x, m):  # Euler's Theorem
            return pow(x, m-2, m)  # O(logMOD) = O(1)

        def nCr(n, k, m):
            if n-k < k:
                return nCr(n, n-k, m)
            result = 1
            for i in xrange(1, k+1):
                result = result*(n-k+i)*inv(i, m)%m
            return result

        n = num_people//2
        return nCr(2*n, n, MOD)*inv(n+1, MOD) % MOD  # Catalan number


# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(num_people//2+1) # dp[i]: # of ways that n pair people can handshake.
        dp[0] = 1
        for k in range(1, num_people//2+1): # k pair people
            for i in range(k):              # 0 - (k-1) pair people
                dp[k] = (dp[k] + dp[i]*dp[k-1-i]) % MOD
        return dp[num_people//2]

print(Solution().numberOfWays(2)) # 1
print(Solution().numberOfWays(4)) # 2
print(Solution().numberOfWays(6)) # 5
print(Solution().numberOfWays(8)) # 14