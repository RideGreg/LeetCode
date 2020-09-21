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
    def sequentialDigits(self, low: int, high: int) -> List[int]:  # USE THIS: enumerate
        m, n = len(str(low)), len(str(high))
        ans = []
        for l in range(m, n + 1):
            for start in range(1, 10 - l + 1):
                cur = 0
                for i in range(start, start + l):
                    cur = 10 * cur + i
                if cur < low: continue
                if cur > high: return ans
                ans.append(cur)
        return ans

    def sequentialDigits_kamyu(self, low, high): # BFS from len-1, len-2 ... numbers, not easy to get this solution
        result = []
        q = collections.deque(range(1, 9))
        while q:
            num = q.popleft()
            if num > high:
                continue
            if low <= num:
                result.append(num)
            if num%10+1 < 10:
                q.append(num*10+num%10+1) # num%10 is rightmost digit, so this appends a sequential digit
        return result


print(Solution().sequentialDigits(100, 300)) # [123,234]
print(Solution().sequentialDigits(1000, 13000)) # [1234,2345,3456,4567,5678,6789,12345]
