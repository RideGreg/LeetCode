# Time:  O(n)
# Space: O(k)

# 974
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7

import collections


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count = collections.defaultdict(int)
        count[0] = 1
        result, prefix = 0, 0
        for a in A:
            prefix = (prefix+a) % K
            result += count[prefix]
            count[prefix] += 1
        return result
