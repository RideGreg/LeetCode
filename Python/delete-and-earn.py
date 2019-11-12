# Time:  O(n)
# Space: O(1)

# 740
# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i] points.
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
#
# You start with 0 points.
# Return the maximum number of points you can earn by applying such operations.
#
# Example 1:
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
#
# Example 2:
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
#
# Note:
# - The length of nums is at most 20000.
# - Each element nums[i] is an integer in the range [1, 10000].

import collections

class Solution(object):
    def deleteAndEarn_bookshadow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        prev, take, skip = None, 0, 0
        for k in sorted(c):
            if k - 1 == prev:
                skip, take = max(take, skip), c[k]*k + skip
            else:
                skip, take = max(take, skip), c[k]*k + max(take, skip)
            prev = k
        return max(take, skip)

    def deleteAndEarn(self, nums):
        cnt = collections.Counter(nums)
        maxn = max(nums + [0])
        dp = [0] * (maxn + 1)
        for x in range(1, maxn + 1):
            dp[x] = max(dp[x - 1], dp[x - 2] + cnt[x] * x)
        return dp[maxn]

''' ming DP, bad - for loop iterate dummy zeros
        if not nums:
            return 0
        c = Counter(nums)
        last, now = 0, 0
        for k in xrange(max(c.keys())+1):
            now, last = max(now, last + c[k]*k), now
        return now
'''
''' kamyu DP, bad - for loop iterate dummy zeros, not using Counter
        vals = [0] * 10001
        for num in nums:
            vals[num] += num
        val_i, val_i_1 = vals[0], 0
        for i in xrange(1, len(vals)):
            val_i_1, val_i_2 = val_i, val_i_1
            val_i = max(vals[i] + val_i_2, val_i_1)
        return val_i
'''
''' ming DFS, TLE - many unnecessary steps
    def deleteAndEarn(self, nums):
        from functools import lru_cache

        # 1. use lru_cache cause TypeError: unhashable type: 'defaultdict'
        # becuase lru_cache use param as key of a set.
        # 2. comment out lru_cache -> TLE
        #@lru_cache(None)
        def dfs(dmap):
            ans = 0
            for k in dmap:
                vk = dmap[k]
                dmap[k] -= 1
                if dmap[k] == 0: del dmap[k]
                vk1 = dmap.pop(k - 1, None)
                vk2 = dmap.pop(k + 1, None)

                ans = max(ans, k + dfs(dmap))

                dmap[k] = vk
                if vk1: dmap[k - 1] = vk1
                if vk2: dmap[k + 1] = vk2
            return ans

        dmap = collections.defaultdict(int)
        for n in nums:
            dmap[n] += 1

        return dfs(dmap)
'''
print(Solution().deleteAndEarn([3,4,2])) #6
print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4])) #9
print(Solution().deleteAndEarn([8,7,3,8,1,4,10,10,10,2])) # 52
