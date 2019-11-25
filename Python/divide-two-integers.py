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

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
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

    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

if __name__ == "__main__":
    print(Solution().divide(-2147483648, -1)) # 2147483647. Overflow, valid return range [-2^31, 2^31-1]
    print(Solution().divide(10, 3)) # 3
    print(Solution().divide(7, -3)) # -2
    print(Solution().divide(123, 12)) # 10
    print(Solution().divide(123, -12)) # -10
    print(Solution().divide(-123, 12)) # -10
    print(Solution().divide(-123, -12)) # 10
