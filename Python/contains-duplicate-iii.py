# Time:  O(n * t)
# Space: O(max(k, t))
#
# Given an array of integers, find out whether there
# are two distinct inwindowes i and j in the array such
# that the difference between nums[i] and nums[j] is
# at most t and the difference between i and j is at
# most k.
#

# This is not the best solution
# since there is no built-in bst structure in Python.
# The better solution could be found in C++ solution.
'''
hash table (key normalized over t, otherwise need to check 2*t keys). Hash funciton:
  if： | nums[i] - nums[j] | <= t
  equivalent to： | nums[i] / t - nums[j] / t | <= 1
  so： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1 (floor value is int which can be key in HT)
  equivalent to： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}
'''
import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}

    # Simple HashMap, store both k and v. Revised hash function to search only 3 buckets. No need OrderedDict to maintain window.
    def containsNearbyAlmostDuplicate_ming(self, nums, k, t): # USE THIS
        d = {}
        for i, n in enumerate(nums):
            bucket = n if not t else n / t
            for key in (bucket-1, bucket, bucket+1):
                if key in d and i-d[key][0] <= k and abs(n-d[key][1]) <= t:
                    return True

            # each bucket won't have 2 eligible items for current elem, otherwise the 2 items already meets condition.
            d[bucket] = (i, n)
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for i, n in enumerate(nums):
            # Make sure window size
            if i > k:
                window.popitem(False)

            bucket = n if not t else n // t
            # 2t items in at most 3 buckets, otherwise need to check [-t, t] range expensive.
            for m in (bucket - 1, bucket, bucket + 1):
                # need check against, edge case [7,4] k=2, t=2 or [-1,-1] k=1, t=-1
                if m in window and abs(n - window[m]) <= t:
                    return True
            window[bucket] = n
        return False

    # simple HashMap, over all previous numbers. Time Limit Exceeded if input array has many items.
    def containsNearbyAlmostDuplicate_TLE1(self, nums, k, t):
        d = {}
        for i, n in enumerate(nums):
            for key in d.keys():
                if abs(key-n) <= t and i-d[key] <= k:
                    return True
            d[n] = i
        return False

    # simple HashMap, over value range, too many buckets to check. Time Limit Exceeded for input [0,2147483647], 1, 2147483647
    def containsNearbyAlmostDuplicate_TLE2(self, nums, k, t):
        d = {}
        for i, n in enumerate(nums):
            for key in xrange(n-t, n+t+1):
                if key in d and i-d[key] <= k:
                    return True
            d[n] = i
        return False
