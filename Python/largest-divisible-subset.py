# Time:  O(n^2)
# Space: O(n)

# 368
# Given a set of distinct positive integers,
# find the largest subset such that every pair (Si, Sj) of
# elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
# If there is only 1 item, return a subset of that item.

# Example 1:
# nums: [1,2,3]
# Result: [1,2] (of course, [1,3] will also be ok)

# Example 2:
# nums: [1,2,4,8]
# Result: [1,2,4,8]



# DP: two helper lists: dp is length of largest subset ending with current element.
# prev is the previous item before current element forming the largest subset.

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        prev = [None] * len(nums)
        largest_idx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[largest_idx] < dp[i]:
                largest_idx = i

        ans = []
        while largest_idx is not None:
            ans.append(nums[largest_idx])
            largest_idx = prev[largest_idx]
        return ans[::-1]

    # one helper list: dp stores the actual subset ending with current item
    # Bad: takes much more space.
    def largestDivisibleSubset_ming(self, nums):
        if not nums: return []
        nums.sort()
        dp = [[n] for n in nums]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
                    if len(dp[i]) > len(dp[ans]):
                        ans = i
        return dp[ans]

print(Solution().largestDivisibleSubset([8,4,1,2])) # [1,2,4,8]
print(Solution().largestDivisibleSubset([2,3,6])) # [2,6]

