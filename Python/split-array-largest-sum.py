# Time:  O(nlog(s-maxn)), s is the sum of nums, s-maxn is the range for binary search
# Space: O(1)

# 410
# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note:
# Given m satisfies the following constraint: 1 <= m <= length(nums) <= 14,000.
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# Minimize the largest subarray sum.
class Solution(object):
    # "使……最大值尽可能小"是二分搜索题目常见的问法
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(nums, m, s):
            curr_sum = 0
            for num in nums:
                if curr_sum + num > s:
                    curr_sum = 0
                    m -= 1
                    if m <= 0: return False
                curr_sum += num
            return True

        import math
        left, right = max(nums), sum(nums)
        left = max(left, (right + m-1)//m) # alternative to get ceil
        #left = max(left, math.ceil(right/m)) #optimization, search range low end is max(largest item, subarray average)
        while left < right:
            mid = left + (right - left) // 2

            if canSplit(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return left

    # "将数组分割为 m段，求…"是动态规划题目常见的问法
    # Time O(n^2*m) Space(m*n)
    def splitArray_dp(self, nums, m):
        n = len(nums)
        dp = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        psum = [0]
        for elem in nums:
            psum.append(psum[-1] + elem)

        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], psum[i] - psum[k]))

        return dp[n][m]



# Time:  O(nlogs), s is the sum of nums
# Space: O(1)

# Maximize the smallest subarray sum.
class SolutionFindMaxMin(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(nums, m, s):
            cnt, curr_sum = 1, 0
            for num in nums:
                curr_sum += num
                if curr_sum > s:
                    curr_sum = 0
                    cnt += 1
            return cnt <= m

        left, right = min(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) / 2
            x = canSplit(nums, m, mid)
            if x:
                right = mid - 1
            else:
                left = mid + 1
        return left

    
# Time:  O(nlogs), s is the sum of nums
# Space: O(1)

# Maximize the smallest subarray sum.
class SolutionFindMaxMin2(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(nums, m, s):
            cnt, curr_sum = 0, 0
            for num in nums:
                curr_sum += num
                if curr_sum >= s:
                    curr_sum = 0
                    cnt += 1
            return cnt < m

        left, right = min(nums), sum(nums)
        for i in xrange(left, right+1):
            canSplit(nums, m, i)
        while left <= right:
            mid = left + (right - left) / 2
            x = canSplit(nums, m, mid)
            if x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1

print(Solution().splitArray([7,2,5,10,8], 2)) # 18