# Time:  O(logn) = O(1)
# Space: O(1)
#
# Divide two integers without using multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.

# - Both dividend and divisor will be 32-bit signed integers.
# - The divisor will never be 0.
# - Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
# range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1
# when the division result overflows.

## SOL: for a / b: rewrite a = (c0*2^0 + c1 * 2^1 + c2 * 2^2... + cn * 2^n) * b
## use shift instead of multiplication when double the factor.
class Solution:
    def divide(self, dividend, divisor): # USE THIS: in first pass, deduct factors (from small to large) as many as possible
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        # OR positive = dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, q = divisor, 1    # 7//3 will run outer loop twice
            while dividend >= temp:
                dividend -= temp
                res += q
                q <<= 1     # double
                temp <<= 1  # double
        if not positive:
            res = -res
        return min(max(-2**31, res), 2**31-1)

    def divide2(self, dividend, divisor):   # same as solution 1, except deduct the biggest factor first
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, q = divisor, 1    # 7//3 will run outer loop once
            while dividend >= (temp << 1):
                q <<= 1     # double
                temp <<= 1  # double
            dividend -= temp
            res += q
        if not positive:
            res = -res
        return min(max(-2**31, res), 2**31-1)

    def divide_recursive(self, dividend: int, divisor: int) -> int:
        def div(a, b):
            ans, olda = 0, a
            while a >= b:
                a -= b
                ans += 1
                q, less = div(a, b<<1)
                a -= less
                ans += q << 1
            return ans, olda - a

        pos = (dividend > 0) is (divisor > 0)
        dvd, dvs = abs(dividend), abs(divisor)
        ans, _ = div(dvd, dvs)
        if not pos:
            ans = -ans
        return min(max(-2**31, ans), 2**31-1)

    def divide3(self, dividend, divisor):   # same as solution 1, except maintain the power of 2
        result, dvd, dvs = 0, abs(dividend), abs(divisor)
        while dvd >= dvs:
            inc = dvs
            i = 0
            while dvd >= inc:
                dvd -= inc
                result += 1 << i
                inc <<= 1
                i += 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            result = -result
        return min(max(result, -2**31), 2**31-1)


if __name__ == "__main__":
    #print(Solution().divide(-2147483648, -1)) # 2147483647. Overflow, valid return range [-2^31, 2^31-1]
    print(Solution().divide(94, 3)) # 31
    print(Solution().divide(10, 3)) # 3
    print(Solution().divide(7, -3)) # -2
    print(Solution().divide(123, 12)) # 10
    print(Solution().divide(123, -12)) # -10
    print(Solution().divide(-123, 12)) # -10
    print(Solution().divide(-123, -12)) # 10
