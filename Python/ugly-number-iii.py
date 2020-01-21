# Time:  O(logn)
# Space: O(1)

# 1201 weekly contest 155 9/21/2020
#
# Write a program to find the n-th ugly number.
# Ugly numbers are positive integers which are divisible by a or b or c.

# 1 <= n, a, b, c <= 10^9
# 1 <= a * b * c <= 10^18
# It's guaranteed that the result will be in range [1, 2 * 10^9]

class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(x, y):
            return x//gcd(x, y)*y

        def count(x, a, b, c, lcm_a_b, lcm_b_c, lcm_c_a, lcm_a_b_c):
            return x//a + x//b + x//c - (x//lcm_a_b + x//lcm_b_c + x//lcm_c_a) + x//lcm_a_b_c

        lcm_a_b, lcm_b_c, lcm_c_a = lcm(a, b), lcm(b, c), lcm(c, a)
        lcm_a_b_c = lcm(lcm_a_b, lcm_b_c)

        left, right = 1, 2*10**9
        while left < right:
            mid = left + (right-left)//2
            if count(mid, a, b, c, lcm_a_b, lcm_b_c, lcm_c_a, lcm_a_b_c) >= n:
                right = mid
            else:
                left = mid+1
        return left

print(Solution().nthUglyNumber(3,2,3,5)) # 4
print(Solution().nthUglyNumber(4,2,3,4)) # 6
print(Solution().nthUglyNumber(5,2,11,13)) # 10
print(Solution().nthUglyNumber(1000000000, 2, 217983653, 336916467)) # 1999999984
