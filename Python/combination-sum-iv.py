# Time:  O(nlon + n * t), t is the value of target.
# Space: O(t)

# 377
# Given an integer array with all positive numbers and no duplicates,
# find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?


from functools import lru_cache

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1] + [0] * target
        nums.sort()

        for i in range(1, target+1):
            for n in nums:
                if n > i:
                    break
                dp[i] += dp[i - n]
        return dp[target]

# Follow up: The problem with negative numbers is that now the combinations could be potentially of infinite length.
# E.g. nums = [-1, 1] and target = 1. So we should limit the length of the combination sequence (give a bound to the problem).
    def combinationSum4WithLength(self, nums, target, length):
        @lru_cache(None)
        def foo(target, length):
            ans = 0
            if target == 0 and length >= 0:
                ans += 1

            if length == 1:
                ans += 1 * (target in nums)
            elif length > 1:
                for num in nums:
                    ans += foo(target-num, length-1)
            return ans

        return foo(target, length)

    ''' OR use memorization
    def combinationSum4WithLength(self, nums, target, length):
        import collections
        memo = collections.defaultdict(int)

        def recur(target, length):
            if (target, length) not in memo:
                if target == 0 and length >= 0:
                    memo[target, length] += 1 # shorter than length limit is ok as target is reached

                if length == 1:
                    memo[target, length] += 1 * (target in nums)
                elif length > 1:
                    for num in nums:
                        memo[target, length] += self.combinationSum4WithLength(nums, target - num, length - 1)
            return memo[target, length]

        return recur(target, length)
    '''



print(Solution().combinationSum4([1,2,3], 4)) # 7
print(Solution().combinationSum4WithLength([-1, 1], 1, 3)) # 4: [1], [-1,1,1], [1,-1,1], [1,1,-1]
print(Solution().combinationSum4WithLength([-1, 1, 0], 1, 3)) # 9
print(Solution().combinationSum4WithLength([-1, 1], 1, 5)) # 14:
#[1], [-1,1,1], [1,-1,1], [1,1,-1]
#lenth 5: 5C2 = 10

