# Time:  O(n)
# Space: O(1)

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

class Solution(object):
    def deleteAndEarn(self, nums):
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
        return max(use, avoid)
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
        def dfs(nums, used, ans, cur):
            print "\nnums, used, cur = ", nums, used, cur
            if not nums:
                print ans[0], cur
                ans[0] = max(ans[0], cur)

            for v in nums:
                if v not in used:
                    used[v] = 1
                    earn = nums.count(v) * v
                    newList = [x for x in nums if x > v+1 or x < v-1]
                    dfs(newList, used, ans, cur+earn)
                    del used[v]

        ans, used = [0], {}
        dfs(nums, used, ans, 0)
        return ans[0]
'''
print Solution().deleteAndEarn([3,4,2]) #6
print Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) #9
print Solution().deleteAndEarn([8,7,3,8,1,4,10,10,10,2])
