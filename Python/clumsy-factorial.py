# Time:  O(1)
# Space: O(1)

# 1006
# Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.
# E.g. factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
#
# We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations
# for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.
#
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied
# using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition
# or subtraction steps, and multiplication and division steps are processed left to right.
#
# Additionally, we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.
#
# Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.


class Solution(object):
    def clumsy(self, N): # USE THIS: brute force recursion
        """
        :type N: int
        :rtype: int
        """
        def foo(x):
            if x == 1: return 1
            elif x == 2: return 1
            elif x == 3: return 1
            elif x == 4: return -2

            return x - (x-1)*(x-2)//(x-3) + foo(x-4)

        if N == 1: return 1
        elif N == 2: return 2
        elif N == 3: return 6
        return N*(N-1)//(N-2) + foo(N-3)


    # observation:
    # i*(i-1)/(i-2) = i+1+2/(i-2)
    #     if i = 3  => i*(i-1)/(i-2) = i + 3
    #     if i = 4  => i*(i-1)/(i-2) = i + 2
    #     if i >= 5 => i*(i-1)/(i-2) = i + 1
    #
    # clumsy(N):
    #     if N = 1 => N
    #     if N = 2 => N
    #     if N = 3 => N + 3
    #     if N = 4 => N + 2 + 1 = N + 3
    #     if N > 4 and N % 4 == 1 => N + 1 + (... = 0) + 2 - 1           = N + 2
    #     if N > 4 and N % 4 == 2 => N + 1 + (... = 0) + 3 - 2 * 1       = N + 2
    #     if N > 4 and N % 4 == 3 => N + 1 + (... = 0) + 4 - 3 * 2 / 1   = N - 1
    #     if N > 4 and N % 4 == 0 => N + 1 + (... = 0) + 5 - (4*3/2) + 1 = N + 1
    def clumsy_deduction(self, N):
        if N <= 2:
            return N
        if N <= 4:
            return N+3
        
        if N % 4 == 0:
            return N+1
        elif N % 4 <= 2:
            return N+2
        return N-1


    def clumsy_ming(self, N): # math, iteration
        def foo(x):
            i = N - 4 * x
            if x == 0:
                return i * (i - 1) // (i - 2) + (i - 3)
            else:
                return -(i * (i - 1) // (i - 2)) + (i - 3)

        q, r = divmod(N, 4)
        ans = 0
        for x in range(q):
            ans += foo(x)

        sign = 1 if q == 0 else -1
        if r == 1:
            return ans + sign
        elif r == 2:
            return ans + sign * 2
        elif r == 3:
            return ans + sign * 6
        else:
            return ans
