# Time:  O(logn)
# Space: O(1)

# 509
# F(0) = 0,   F(1) = 1, F(2) = 1, F(3) = 2
# F(N) = F(N - 1) + F(N - 2), for N > 1.

# Given N, calculate F(N).


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        def matrix_expo(A, K):
            # identity matrix
            result = [[int(i==j) for j in range(len(A))] \
                      for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K //= 2
            return result

        def matrix_mult(A, B):
            ZB = list(zip(*B)) # KENG: if a zip object, only transferable once
            return [[sum(a*b for a, b in zip(row, col)) for col in ZB] for row in A]


        # T and zip(*T) transpose are identical
        T = [[1, 1],
             [1, 0]]
        return matrix_expo(T, N)[1][0]


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(N):
            prev, current = current, prev + current,
        return prev

print(Solution().fib(2)) # 1
print(Solution().fib(3)) # 2
print(Solution().fib(4)) # 3
print(Solution().fib(5)) # 5