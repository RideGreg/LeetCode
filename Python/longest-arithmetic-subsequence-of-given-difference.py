# Time:  O(n)
# Space: O(n)

# 1218 weekly contest 157 10/5/2019
# Given an integer array arr and an integer difference, return the length of the longest subsequence
# in arr which is an arithmetic sequence such that the difference between adjacent elements
# in the subsequence equals difference.

# 1 <= arr.length <= 10^5
# -10^4 <= arr[i], difference <= 10^4

import collections


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        ans = 1
        for i in A:
            dp[i] = dp[i-d] + 1
            ans = max(ans, dp[i])
        return ans

print(Solution().longestSubsequence([1,2,3,4], 1)) # 4
print(Solution().longestSubsequence([1,3,5,7], 1)) # 1
print(Solution().longestSubsequence([1,5,7,8,5,3,4,2,1], -2)) # 4
