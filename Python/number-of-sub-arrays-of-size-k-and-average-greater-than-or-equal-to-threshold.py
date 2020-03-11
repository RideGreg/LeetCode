# Time:  O(n)
# Space: O(1)

# # 1343 biweekly contest 19 2/8/2020

# Given an array of integers arr and two integers k and threshold.
#
# Return the number of sub-arrays of size k and average greater than or equal to threshold.

import itertools


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        result, curr = 0, sum(arr[:k-1]) # or sum(itertools.islice(arr, 0, k-1))
        for i in range(k-1, len(arr)):
            curr += arr[i]-(arr[i-k] if i-k >= 0 else 0)
            result += int(curr >= threshold*k)
        return result

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        accu = [0]
        for x in arr:
            accu.append(accu[-1]+x)
        result = 0
        for i in range(len(accu)-k):
            if accu[i+k]-accu[i] >= threshold*k:
                result += 1
        return result

print(Solution().numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)) # 3
print(Solution().numOfSubarrays([1,1,1,1,1], 1, 0)) # 5
