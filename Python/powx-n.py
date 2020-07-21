# Time:  O(logn) = O(1)
# Space: O(1)

# 50
# Implement pow(x, n).
# Note: -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

# Iterative solution.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0: return 0.0 # necessary, otherwise ZeroDivisionError: float division by zero. Eg. myPow(0, -5)
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        ans = 1.0
        while n:
            if n & 1:
                ans *= x
            x *= x # x = x**2 causes error OverflowError: (34, 'Numerical result out of range') when x > 1.34e+154
            n //= 2
        return ans

# Time:  O(logn)
# Space: O(logn), recursion uses stack space
# Recursive solution.
class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def quickPow(x, n):
            if n == 0:
                return 1.0
            v = quickPow(x, n // 2)
            return v * v if n % 2 == 0 else v * v * x

        if x == 0: return 0.0
        if n >= 0:
            return quickPow(x, n)
        else:
            return 1.0 / quickPow(x, -n)


if __name__ == "__main__":
    print(Solution().myPow(0, -5)) # 0.0
    print(Solution().myPow(2.00000, -2147483648)) # 0.0
    print(Solution().myPow(3, 5)) # 243
    print(Solution().myPow(3, -5)) # 0.00411522633745

