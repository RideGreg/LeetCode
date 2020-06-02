# Time:  O(nlogn)
# Space: O(n)

# 300
# Given an unsorted array of integers,
# find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more
# than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#

# Binary search solution 贪心 + 二分查找：维护一个数组 LIS_tail，储存最长上升子序列的末尾元素的最小值。因为上升子序列的
# 单调性，可用二分查找优化每一步。理念来源于贪心算法：要使上升子序列尽可能的长，需要让序列上升得尽可能慢。

# LIS[i] stores the smallest tail of LIS with length i+1 : when new elem is larger than all elems in LIS,
# append to the end of LIS; otherwise replace the first LIS elem which is larger than it.
# e.g. given [10, 9, 2, 5, 3, 7, 101, 18],
# [10] -> [9] -> [2] -> [2,5] -> [2,3] -> [2,3,7] -> [2,3,7,101] -> [2,3,7,18]

# given [20, 21, 22, 1, 2, 3, 4]:
# [20] -> [20, 21] -> [20,21,22] -> [1,21,22] -> [1,2,22] -> [1,2,3] -> [1,2,3,4]
#                                   ^ this is not a valid subsequence but the length are correct.
#                1 is smallest tail of length-1 LIS, 21 is tail of length-2 LIS, 22 is tail of length-3 LIS.
# the method in this geeksforgeeks article is similar but not straightforward https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        LIS_tail = []
        for n in nums:
            pos = bisect.bisect_left(LIS_tail, n) # Find the first pos which satisfies seq[pos] >= target
            if pos == len(LIS_tail):
                LIS_tail.append(n)
            else:
                LIS_tail[pos] = n
        return len(LIS_tail)


# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

print(Solution().lengthOfLIS([2,3,4,1]))
