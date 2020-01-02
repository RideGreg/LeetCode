# Time:  O(n)
# Space: O(n)

# 1175 weekly contest 152 8/31/2019
# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
#
# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written
# as a product of two positive integers both smaller than it.)
#
# Since the answer may be large, return the answer modulo 10^9 + 7.

# 1 <= n <= 100

class Solution(object):
    def numPrimeArrangements(self, n: int) -> int: # USE THIS
        import functools, operator
        def count(n):
            primes = [True] * (n+1)
            primes[0] = primes[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if primes[i]:
                    # mark all composite numbers which are multiple of prime number i
                    # primes[i * i: n+1: i] = [False] * len(primes[i * i: n+1: i])
                    p = i * i
                    while p <= n:
                        primes[p] = False
                        p += i
            return sum(primes)

        c = count(n)
        fact = lambda x, y: functools.reduce(operator.mul, range(x, y + 1), 1)
        return (fact(1, c) * fact(1, n-c)) % (10**9+7)

    def numPrimeArrangements_kamyu(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count_primes(n):
            if n <= 1:
                return 0
            is_prime = [True]*((n+1)//2)
            cnt = len(is_prime)
            for i in xrange(3, n+1, 2):
                if i*i > n:
                    break
                if not is_prime[i//2]:
                    continue
                for j in xrange(i*i, n+1, 2*i):
                    if not is_prime[j//2]:
                        continue
                    cnt -= 1
                    is_prime[j//2] = False
            return cnt
        
        def factorial(n):
            result = 1
            for i in xrange(2, n+1):
                result = (result*i)%MOD
            return result

        MOD = 10**9+7
        cnt = count_primes(n)
        return factorial(cnt) * factorial(n-cnt) % MOD

print(Solution().numPrimeArrangements(5)) # 12
print(Solution().numPrimeArrangements(100)) # 682289015
