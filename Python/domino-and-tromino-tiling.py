# Time:  O(logn)
# Space: O(1)

# 790
# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
# These shapes may be rotated.
#
# XX  <- domino
#
# XX  <- "L" tromino
# X
# Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.
#
# (In a tiling, every square must be covered by a tile.
# Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
# such that exactly one of the tilings has both squares occupied by a tile.)
#
# Example:
# Input: 3
# Output: 5
# Explanation:
# The five different ways are listed below, different letters indicates different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
#
# Note:
# - N  will be in range [1, 1000].

import itertools


class Solution(object):
    # wrong. E.g. for dp[4], L-J and T_7 cannot be obtained from dp[3], dp[2], dp[1]
    def numTilings_wrong(self, N: int) -> int:
        # init for 0, 1, 2
        a, b, c = 1, 1, 2
        if N == 1: return b
        for _ in (3, N+1):
            a, b, c = b, c, (a*2+b+c) % (10**9+7)
        return c

    # bookshadow: A,B,C[x]表示end at column x的tiles拼接方法个数
    #
    # 末尾形状为A: 表示末尾没有多余部分
    # 末尾形状为B: 表示第一行多出1个单元格
    # 末尾形状为C: 表示第二行多出1个单元格
    # Ending state A:
    #       x
    # ...   x
    #       i
    # Ending state B:
    #       x
    # ...   xx
    #        i
    # Ending state C:
    #       xx
    # ...   x
    #        i
    # 状态转移方程见代码。
    #
    def numTilings(self, N): # USE THIS
        """
        :type N: int
        :rtype: int
        """
        MOD = 10**9 + 7
        A = [1, 1]
        B = [0, 0]
        C = [0, 0]
        for _ in range(2, N + 1):
            nA = (A[0] + A[1] + B[1] + C[1]) % MOD
            nB = (A[0] + C[1]) % MOD
            nC = (A[0] + B[1]) % MOD
            A = [A[1], nA]
            B = [B[1], nB]
            C = [C[1], nC]
        return A[1]
        ''' version with full space
        A = [0 for i in range(N + 1)]
        B = [0 for i in range(N + 1)]
        C = [0 for i in range(N + 1)]
        A[0] = 1
        for i in range(1, N + 1):
            A[i] = (B[i - 1] + C[i - 1] + A[i - 1] + (A[i - 2] if i >= 2 else 0)) % MOD
            B[i] = (C[i - 1] + (A[i - 2] if i >= 2 else 0)) % MOD
            C[i] = (B[i - 1] + (A[i - 2] if i >= 2 else 0)) % MOD
        return A[-1]
        '''

    def numTilings_kamyu(self, N):
        M = int(1e9+7)

        def matrix_expo(A, K):
            result = [[int(i==j) for j in range(len(A))] \
                      for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K //= 2
            return result

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b for a, b in zip(row, col)) % M \
                     for col in ZB] for row in A]

        T = [[1, 0, 0, 1],  # #(|) = #(|) + #(=)
             [1, 0, 1, 0],  # #(「) = #(|) + #(L)
             [1, 1, 0, 0],  # #(L) = #(|) + #(「)
             [1, 1, 1, 0]]  # #(=) = #(|) + #(「) + #(L)

        return matrix_expo(T, N)[0][0]  # T^N * [1, 0, 0, 0]


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Prove:
        # dp[n] = dp[n-1](|) + dp[n-2](=) + 2*(dp[n-3](「」) + ... + d[0](「 = ... = 」))
        #       = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-3] + 2*(dp[n-4] + ... + d[0])
        #       = dp[n-1] + dp[n-3] + (dp[n-2] + dp[n-3] + 2*(dp[n-4] + ... + d[0])
        #       = dp[n-1] + dp[n-3] + dp[n-1]
        #       = 2*dp[n-1] + dp[n-3]
        M = int(1e9+7)
        dp = [1, 1, 2]
        for i in range(3, N+1):
            dp[i%3] = (2*dp[(i-1)%3]%M + dp[(i-3)%3])%M
        return dp[N%3]

print(Solution().numTilings(3)) # 5
print(Solution().numTilings(4)) # 11. Note L-J and T_7
