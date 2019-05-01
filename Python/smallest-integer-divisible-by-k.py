# Time:  O(k)
# Space: O(1)

# 1015
# Given a positive integer K, you need find the smallest positive integer N such that
# N is divisible by K, and N only contains the digit 1.
#
# Return the length of N.  If there is no such N, return -1.
# 1 <= K <= 10^5

class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        # by observation, K % 2 = 0 or K % 5 = 0, it is impossible
        if K % 2 == 0 or K % 5 == 0:
            return -1

        # Solution: for K not a multiple of 2 or 5, at least one from the K integers (1, 11, 111,
        # ... 11..11 (K-length) will be divisible by K.
        # let f(N) is a N-length integer only containing digit 1
        # if there is no N in range [1..K] s.t. f(N) % K = 0
        # then for the K integers f(1), f(2),... f(K),
        # => there must be K remainders of f(N) % K in range [1..K-1] excluding 0
        # => due to pigeonhole principle, there must be at least 2 same remainders
        # => there must be some x, y in range [1..K] and x > y s.t. f(x) % K = f(y) % K
        # => (f(x) - f(y)) % K = 0
        # => (f(x-y) * 10^y) % K = 0
        # => due to (x-y) in range [1..K] and f(x-y) % K != 0
        # => 10^y % K = 0
        # => K % 2 = 0 or K % 5 = 0
        # => -><-
        # it proves that there must be some N in range (1..K) s.t. f(N) % K = 0

        # In fact, current remainder determines the next remainder, due to next_mod = (mod*10+1) % K
        # so if a duplicate mod is found, it starts a loop. E.g.
        # 1 % 6 = 1
        # 11 % 6 = 5
        # 111 % 6 = 3
        # 1111 % 6 = 1
        # 11111 % 6 = 5
        # 111111 % 6 = 3

        r = 0
        for N in range(1, K+1):
            r = (r*10+1) % K  # module by K can reduce the integer, not affecting result
            if not r:
                return N
        assert(False)
        return -1  # never reach
