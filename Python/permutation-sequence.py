# Time:  O(n^2)
# Space: O(n)

# 60
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.

import math

# Cantor ordering solution
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k - 1        # 1 based change to 0 based
        seq, fact = [], math.factorial(n - 1)
        cand = list(range(1, n + 1))
        for i in reversed(range(n)):   # O(n)
            pos, k = divmod(k, fact)
            seq.append(str(cand[pos]))
            cand.pop(pos)              # O(n)

            if i > 0:
                fact //= i
        return ''.join(seq)

    # backtrack + maintain counter, TLE for getPermutation(9,296662)
    # O(n*k), need to generate k results each is n-length
    def getPermutation_TLE(self, n: int, k: int) -> str:
        def backtrack(cur):
            if len(cur) == n:
                self.cnt -= 1
                return ''.join(cur) if self.cnt == 0 else None
            for i in range(1, n+1):
                if not used[i]:
                    used[i] = True
                    cur.append(str(i))
                    s = backtrack(cur)
                    if s:
                        break
                    cur.pop()
                    used[i] = False
            return s

        self.cnt = k
        used = [False] * (n+1)
        return backtrack([])

print(Solution().getPermutation(4, 16)) # '3241'
print(Solution().getPermutation(3, 1)) # '132'
print(Solution().getPermutation(3, 2)) # '132'
print(Solution().getPermutation(3, 3)) # '213'
