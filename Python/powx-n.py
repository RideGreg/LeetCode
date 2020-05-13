# Time:  O(logn) = O(1)
# Space: O(1)

# Implement pow(x, n).

# Iterative solution.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
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
# Space: O(logn)
# Recursive solution.
class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0 and n != -n:
            return 1.0 / self.myPow(x, -n)
        if n == 0:
            return 1
        v = self.myPow(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x


if __name__ == "__main__":
    print(Solution().myPow(2.00000, -2147483648)) # 0.0
    print(Solution().myPow(3, 5)) # 243
    print(Solution().myPow(3, -5)) # 0.00411522633745

