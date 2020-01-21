# Time:  O(logn)
# Space: O(1)

# 1287 biweekly contest 15 12/14/2019
#
# Given an integer array SORTED in non-decreasing order, there is exactly one integer in the array
# that occurs more than 25% of the time.
#
# Return that integer.

import bisect
import collections

class Solution(object):
    def findSpecialInteger(self, arr): # UES THIS: binary search
        """
        :type arr: List[int]
        :rtype: int
        """
        for x in [arr[len(arr)//4], arr[len(arr)//2], arr[len(arr)*3//4]]:
            if (bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)) * 4 > len(arr):
                return x
        return -1

    # O(n). Pro: no need to check all items
    def findSpecialInteger_awice(self, A):
        count = collections.Counter(A)
        N = len(A)
        for x in count:
            if count[x] * 4 > N:
                return x

    # O(n)
    def findSpecialInteger_ming(self, arr):
        c = collections.Counter(arr)
        return max(c, key=c.get)

print(Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10])) # 6