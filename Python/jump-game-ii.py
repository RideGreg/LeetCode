# Time:  O(n)
# Space: O(1)
# 45
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#

# not pass on leetcode because of time limit
class Solution(object):
    # @param A, a list of integers
    # @return an integer
    def jump(self, nums): # USE THIS
        reach, new_reach, step = 0, 0, 0
        for i in range(len(nums)-1):
            if i <= reach:
                new_reach = max(new_reach, i + nums[i])
                #if new_reach >= len(nums) - 1: # don't do early return to keep code simple
                #    return step + 1

                if i == reach:
                    step += 1
                    reach = max(reach, new_reach)
        return step if reach >= len(nums) - 1 else -1

    def jump_kamyu(self, nums): # similar to above
        jump_count = 0
        reachable = 0
        curr_reachable = 0
        for i, length in enumerate(nums):
            if i > reachable:
                return -1
            if i > curr_reachable:
                curr_reachable = reachable
                jump_count += 1
            reachable = max(reachable, i + length)
        return jump_count


    # Time O(n^2) Space O(n) 不好：没必要计算每个位置需要的最小步数
    def jump_TLE(self, nums):
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)-1):
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[-1] if dp[-1] != float('inf') else -1

print(Solution().jump([2,3,1,1,4])) # 2
print(Solution().jump([3,2,1,0,4])) # 0
print(Solution().jump([2,3,1,2,4,2,3])) # 3
