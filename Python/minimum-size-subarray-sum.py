# Time:  O(n)
# Space: O(1)
# 209
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a subarray of which the sum >= s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
#

# Sliding window solution.
class Solution:            # USE THIS
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        l, ans, ssum = 0, float('inf'), 0
        for r in range(len(nums)):
            ssum += nums[r]
            while ssum >= s:
                ans = min(ans, r-l+1)
                if ans == 1: return ans   # found best possible
                ssum -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0

        ''' similar solution
        l, ans, ssum = 0, float('inf'), 0
        for r in range(len(nums)):
            ssum += nums[r]
            if ssum >= s:
                while l < len(nums) and ssum - nums[l] >= s:
                    ssum -= nums[l]
                    l += 1
                ans = min(ans, r-l+1)
        return ans if ans != float('inf') else 0
        '''

# Time:  O(nlogn)
# Space: O(n)
# Binary search solution.
class Solution2:
    def minSubArrayLen(self, s, nums):
        import bisect
        ans, psum= float('inf'), [0]
        for x in nums:
            psum.append(psum[-1] + x) # psum is mono increasing, so bisect can be used

        for r in range(len(psum)):
            if psum[r] >= s:
                l = bisect.bisect(psum, psum[r]-s)
                ans = min(ans, r-l+1)
        return ans if ans != float('inf') else 0

print(Solution().minSubArrayLen(5, [1,1,1,1,2,2,2,5,2,2])) # 1
print(Solution().minSubArrayLen(7, [2,3,1,2,4,3])) # 2
