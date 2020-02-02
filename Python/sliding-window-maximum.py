# -*- coding:UTF-8 -*-

# Time:  O(n)
# Space: O(k)

# Given an array nums, there is a sliding window of size k
# which is moving from the very left of the array to the
# very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
#
# Note:
# You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?

# Solution:
# 遍历数组nums，使用双端队列deque维护滑动窗口内有可能成为最大值元素的数组下标 (a "monoqueue" of indices of nums such that nums[dq[0]] > nums[dq[1]])
#
# 记当前下标为i，则滑动窗口的有效下标范围为[i - (k - 1), i]
# 若deque中的头元素下标＜ i - (k - 1)，则将其从*队头*弹出。
#
# deque中的元素按照下标递增顺序从队尾入队。
# 当下标i从队尾入队之前，顺次弹出*队尾*不大于nums[i]的数组下标（这些被弹出的元素由于新元素的加入而变得没有意义）
#
# deque的队头元素即为当前滑动窗口的最大值
# 由于数组中的每一个元素至多只会入队、出队一次，因此均摊时间复杂度为O(n)

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        result = []
        for i in xrange(len(nums)):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                result.append(nums[dq[0]])
        return result

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]