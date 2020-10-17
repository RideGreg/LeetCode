# Time:  O(n)
# Space: O(n)

# 532
# Given an array of integers and an integer k,
# you need to find the number of unique k-diff pairs in the array.
# Here a k-diff pair is defined as an integer pair (i, j),
# where i and j are both numbers in the array and their absolute difference is k.
#
# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107

import collections
class Solution(object):
    # Use set since there may be duplicates: suppose 2 valid pairs (1,3) (3,5):
    # 'result' set only stores the smaller one, 'seen' set for fast lookup of pairs.
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0 # question says k is absolute difference
        result, seen = set(), set()
        for num in nums:
            for cand in (num-k, num+k):
                if cand in seen:
                    result.add(min(num, cand))
            seen.add(num)
        return len(result)


    # get Counter first, then count.
    def findPairs2(self, nums, k):
        cnt = collections.Counter(nums)
        if k == 0:
            return sum(x > 1 for x in cnt.values())
        else:
            return sum(x+k in cnt for x in cnt.keys())


print((Solution().findPairs([3,1,4,1,5], 2))) # 2
print((Solution().findPairs([1,3,1,5,4], 0))) # 1
print((Solution().findPairs([1,2,4,4,3,3,0,9,2,3], 3))) # 2
