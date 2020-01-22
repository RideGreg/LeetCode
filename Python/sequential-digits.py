# Time:  O((8 + 1) * 8 / 2) = O(1)
# Space: O(8) = O(1)

# 1291 weekly contest 167 12/14/2019

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# 10 <= low <= high <= 10^9

import collections
from typing import List

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        q = collections.deque(range(1, 9))
        while q:
            num = q.popleft()
            if num > high:
                continue
            if low <= num:
                result.append(num)
            if num%10+1 < 10:
                q.append(num*10+num%10+1)
        return result

    def sequentialDigits_ming(self, low: int, high: int) -> List[int]:
        ans = []
        kl, kh = len(str(low)), len(str(high))+1
        for k in range(kl, min(10,kh)):
            for i in range(1, 10-k+1):
                v = sum((i+j)*(10**(k-1-j)) for j in range(k))
                if v < low: continue
                if v > high: return ans
                ans.append(v)
        return ans

print(Solution().sequentialDigits(100, 300)) # [123,234]
print(Solution().sequentialDigits(1000, 13000)) # [1234,2345,3456,4567,5678,6789,12345]
