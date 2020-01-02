# Time:  O(nlogn)
# Space: O(n)

# 1122 weekly contest 145 7/13/2019
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in
# arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in
# arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.

from typing import List

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        lookup = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: lookup.get(i, len(arr2)+i))

    def relativeSortArray_ming(self, arr1: List[int], arr2: List[int]) -> List[int]:
        import collections
        c = collections.Counter(arr1)
        set2 = set(arr2)
        arr3 = sorted([k for k in c if k not in set2])
        ans = []
        for k in arr2+arr3:
            ans.extend([k]*c[k])
        return ans

print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
# [2,2,2,1,4,3,3,9,6,7,19]
