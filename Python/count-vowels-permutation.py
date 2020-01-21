# Time:  O(logn)
# Space: O(1)

# 1220 weekly contest 157 10/5/2019

# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
#
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.

# 1 <= n <= 2 * 10^4

import itertools


class Solution(object):
    def countVowelPermutation(self, n): # USE THIS
        """
        :type n: int
        :rtype: int
        """
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
            ZB = list(zip(*B)) # KENG: if a zip object, only transferable once
            return [[sum(a*b for a, b in zip(row, col)) % MOD \
                     for col in ZB] for row in A]
        
        MOD = 10**9 + 7
        # Use this T makes more sense, multiply each col in T
        T = [[0,1,0,0,0],
             [1,0,1,0,0],
             [1,1,0,1,1],
             [0,0,1,0,1],
             [1,0,0,0,0]]

        '''
        T = [[0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 1, 1, 0]]
        '''

        ans = matrix_expo(T, n-1)
        return sum(map(sum, ans)) % MOD


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a, e, i, o, u = (e+i+u) % MOD, (a+i) % MOD, (e+o) % MOD, i, (i+o) % MOD
        return (a+e+i+o+u) % MOD

    def countVowelPermutation_ming(self, n):
        M = 10 ** 9 + 7
        # take each row in T for zipping
        T = [[0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 1, 1, 0]]
        dp = [1, 1, 1, 1, 1]
        for _ in range(n - 1):
            ndp = [sum(a * b for a, b in zip(dp, x)) % M for x in T]
            dp = ndp
        return sum(dp) % M

print(Solution().countVowelPermutation(1)) # 5
print(Solution().countVowelPermutation(2)) # 10
print(Solution().countVowelPermutation(3)) # 19
print(Solution().countVowelPermutation(5)) # 68
print(Solution().countVowelPermutation(144)) # 18208803