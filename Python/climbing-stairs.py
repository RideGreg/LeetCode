# Time:  O(logn)
# Space: O(1)
#
# 70
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

import itertools

# Use MATRIX MULTIPLICATION to obtain the nth Fibonacci Number. The matrix takes the following form:
# Q = | 1 1 |
#     | 1 0 |
#
# Q^2 = | 2 1 |
#       | 1 1 |
# As per the method, the nth Fibonacci Number is given by Q^(n-1)[0,0].
#
# Let's look at the proof of this method.
# Assume F_n = Q^(n-1)[0,0] where
# Q^(n-1) = | F_n    F_n-1 |
#           | F_n-1  F_n-2 |
# Then
# Q^n = | F_n    F_n-1 | * | 1 1 | = | F_n + F_n-1     F_n   | = | F_n+1 F_n   |
#       | F_n-1  F_n-2 |   | 1 0 |   | F_n-1 + F_n-2   F_n-1 |   | F_n   F_n-1 |
# Thus F_n+1 = Q^n[0,0]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def matrix_expo(A, K):
            N = len(A)
            result = [[int(i==j) for j in range(N)]  for i in range(N)]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a*b for a, b in itertools.izip(row, col)) \
                     for col in ZB] for row in A]

        T = [[1, 1],
             [1, 0]]
        return matrix_mult([[1,  0]], matrix_expo(T, n))[0][0]  # [a0, a(-1)] * T^n


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    """
    :type n: int
    :rtype: int
    """
    def climbStairs(self, n): # Fibonacci Number
        prev, current = 0, 1
        for i in xrange(n):
            prev, current = current, prev + current,
        return current

    # Time:  O(2^n), size of recursion tree is 2^n
    # Space: O(n)
    def climbStairs_bruteForce(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # Math formula:
    # F_n = [ Phi^n - phi^n ]/Sqrt[5].
    # where Phi=(1+Sqrt[5])/2，phi=(1-Sqrt[5])/2
    def climbStairs_math(self, n):
        sqrt5 = math.sqrt(5)
        Phi = (1 + sqrt5) / 2
        phi = (1 - sqrt5) / 2
        return int((Phi ** (n + 1) - phi ** (n + 1)) / sqrt5)


if __name__ == "__main__":
    result = Solution().climbStairs(2)
    print result
