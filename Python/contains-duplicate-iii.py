# Time:  O(n)
# Space: O(n)
# 220
# Given an array of integers, find out whether there
# are two distinct inwindowes i and j in the array such
# that the difference between nums[i] and nums[j] is
# at most t and the difference between i and j is at
# most k.
#

'''
Brute Force:
1. O(n*k) for a new item, check previous k numbers to see if value diff <= t
2. O(n*t) use hash table to store everything seen (i,v) pair. For a new item v1, check if any from [v1-t, v1+t]
was seen. Search range may be large, so need to shrink search range (by normalization).

Bucket + hash table:
hash table key is bucketID (= input int num normalized by dividing t), value is the index and real value
of that int num; for a new int, all int having a value difference up to t will be in current bucket or its left/right
neighbor buckets.
This bucketization is much better than using a set to record nums already seen, which needs to
check 2*t numbers.
  | nums[i] - nums[j] | <= t
  equivalent to： | nums[i] / t - nums[j] / t | <= 1
  so： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1 (floor value is int bucketID used as HT key)
  equivalent to： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}

BST:
C++(multiset) / Java(TreeSet) has a data structure of self-balanced BST, which
can be used to solve this problem in O(nlogk) time.
No built-in bst structure in Python.
'''
import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}

    # HashTable stores both index and int. Only need to search current bucket and left/right
    # neighbors. No need OrderedDict to maintain window.
    def containsNearbyAlmostDuplicate(self, nums, k, t): # USE THIS
        buckets = {}
        for i, n in enumerate(nums):
            bucket = n if t == 0 else n // t
            for b in (bucket-1, bucket, bucket+1):
                if b in buckets:
                    j, m = buckets[b]
                    if i-j <= k and abs(n-m) <= t:
                        return True

            # replace the item in bucket which has smaller index is ok, because if 2 items fall into the same bucket
            # (means their value diff <= t), and they are not answer means index diff not <= k. We only need to keep the
            # new item which has larger index for future items.
            buckets[bucket] = (i, n)
        return False

    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        window = collections.OrderedDict()
        for i, n in enumerate(nums):
            # Make sure window size. All items stayed in window meet the index diff <= k.
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

    # TLE: search over all previous numbers. Time Limit Exceeded if input array has many items.
    def containsNearbyAlmostDuplicate_BruteForce1(self, nums, k, t):
        d = {}
        for i, n in enumerate(nums):
            for key in d.keys():
                if abs(key-n) <= t and i-d[key] <= k:
                    return True
            d[n] = i
        return False

    # TLE: search over value range, too many buckets to check. Time Limit Exceeded for input [0,2147483647], 1, 2147483647
    def containsNearbyAlmostDuplicate_BruteForce2(self, nums, k, t):
        d = {}
        for i, n in enumerate(nums):
            for key in range(n-t, n+t+1):
                if key in d and i-d[key] <= k:
                    return True
            d[n] = i
        return False

print(Solution().containsNearbyAlmostDuplicate2([1,12,22,1,12,21], 2, 3)) # False
print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3)) # False
print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)) # True
print(Solution().containsNearbyAlmostDuplicate([1,0,1,1], 1, 2)) # True