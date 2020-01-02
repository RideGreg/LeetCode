# Time:  O(2^n)
# Space: O(1)

# 1238 weekly contest 160 10/26/2019
# Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
#
# p[0] = start
# p[i] and p[i+1] differ by only one bit in their binary representation.
# p[0] and p[2^n -1] must also differ by only one bit in their binary representation.



# refer to gray-code.py

from typing import List

class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        return [start ^ (i>>1) ^ i for i in range(1<<n)] # XOR is associative

    def circularPermutation_ming(self, n: int, start: int) -> List[int]:
        dp = [0]
        for i in range(n):
            for v in reversed(dp):
                dp.append(1 << i | v) # or dp.append(v + 2**i)
        k = dp.index(start)
        return dp[k:] + dp[:k]


print(Solution().circularPermutation(2, 3)) # [3,2,0,1]
print(Solution().circularPermutation(3, 2)) # [2,6,7,5,4,0,1,3]
