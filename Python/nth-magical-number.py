# Time:  O(log(N*min(A, B))), the binary search upper bound is N*min(A,B)
# Space: O(1)

# A positive integer is magical if it is divisible by either A or B.
#
# Return the N-th magical number.
# Since the answer may be very large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: N = 1, A = 2, B = 3
# Output: 2
# Example 2:
#
# Input: N = 4, A = 2, B = 3
# Output: 6
# Example 3:
#
# Input: N = 5, A = 2, B = 4
# Output: 10
# Example 4:
#
# Input: N = 3, A = 6, B = 4
# Output: 8
#
# Note:
# - 1 <= N <= 10^9
# - 2 <= A <= 40000
# - 2 <= B <= 40000

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        # binary search: The number of magical numbers <= x is a monotone increasing f(x) = x/A+x/B-x/lcm(A,B),
        # upper bound is N*min(A,B), so we can binary search for the answer.

        # or "from fractions import gcd"
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = A*B // gcd(A, B)
        left, right = min(A, B), min(A, B)*N
        while left < right:
            mid = left + (right-left)//2
            if mid//A + mid//B - mid//lcm >= N:
                right = mid
            else:
                left = mid+1
        return left % (10**9 + 7)

    def nthMagicalNumber_math(self, N, A, B):
        """
        Count N-th magical number mathematically. The pattern of magical numbers repeats. Let L be the least common multiple of A and B.
        If X (<=L) is magical, then X + L is magical too. Also note there are M = L/A + L/B - 1 magical numbers <= L.
        Suppose N = M*q + r. Then 1 -> L*q range contain M∗q magical numbers, and we just need to find r more magical ones.

        Time: O(A+B), calculate q*L is O(1), calculate the extra r magic numbers is O(M) ~= O(A+B)
        Space: O(1)
        """
        from fractions import gcd

        L = A / gcd(A, B) * B
        M = L / A + L / B - 1
        q, r = divmod(N, M)

        if r == 0:
            return q * L % (10**9 + 7)

        a, b = A, B
        for _ in xrange(r - 1):
            if a <= b:
                a += A
            else:
                b += B

        return (q * L + min(a, b)) % (10**9 + 7)

    # Time: O(N), TLE 1000000000, 39999, 40000
    def nthMagicalNumber_generator(self, N, A, B):
        if A > B:
            A, B = B, A

        def gen1():
            for i in xrange(A, N*A+1, A):
                yield i
        def gen2():
            for i in xrange(B, N*B+1, B):
                yield i
        gen1, gen2 = gen1(), gen2()

        a, b = 0, 0
        for _ in xrange(N): # generating all N numbers makes TLE
            if a == 0:
                a = next(gen1)
            if b == 0:
                b = next(gen2)
            if a < b:
                ans, a = a, 0
            elif a > b:
                ans, b = b, 0
            else:
                ans, a, b = a, 0, 0
        return ans % (10**9 + 7)

    # Time: O(N), memory over limit, the list of numbers can be huge
    def nthMagicalNumber_set(self, N, A, B):
        if A > B:
            A, B = B, A
        s1 = set(range(A, N*A+1, A))
        s2 = set(range(B, N*A+1, B))
        s1 |= s2

        return sorted(list(s1))[N-1]