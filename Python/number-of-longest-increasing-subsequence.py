# Time:  O(n^2)
# Space: O(n)

# 673
# Given an unsorted array of integers, find the number of longest increasing subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are
# 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed
# to be fit in 32-bit signed int.

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, max_len = 0, 0
        dp = [[1, 1] for _ in range(len(nums))]  # {longest_length, count} for LIS ending at this elem
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    l, c = dp[j]
                    if dp[i][0] == l+1:
                        dp[i][1] += c
                    elif dp[i][0] < l+1:
                        dp[i] = [l+1, c]
            if max_len == dp[i][0]:
                ans += dp[i][1]
            elif max_len < dp[i][0]:
                max_len, ans = dp[i]
        return ans
