# Time:  O(nklogk), n 是所有列表的平均长度，k 是列表数量。所有的指针移动的总次数最多是 nk 次，
#                  每次从堆中取出元素和添加元素都需要更新堆，时间复杂度是 O(logk)
# Space: O(k)

# 632
# You have k lists of sorted integers in ascending order.
# Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
#
# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -10^5 <= value of elements <= 10^5.
# For Java users, please note that the input type has been changed to List<List<Integer>>.
# And after you reset the code template, you'll see this point.

import heapq

# 把k个列表排序，对每个列表维护一个指针，指针右移之后指向的元素一定大于或等于之前的元素。
# 使用最小堆维护 k个指针指向的元素中的最小值，同时维护堆中元素的最大值。每次从堆中取出最小值，然后将对应列表的新元素加入堆中，
# 并更新堆中元素的最小值和大值。

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        l, r = float('inf'), float('-inf')
        minHeap = []
        for i, row in enumerate(nums): # take first elem from each of k lists
            l, r = min(l, row[0]), max(r, row[0])
            heapq.heappush(minHeap, (row[0], i, 0))
        ans = [l, r]

        while True:
            _, i, j = heapq.heappop(minHeap)
            if j == len(nums[i]) - 1:
                break
            val = nums[i][j+1]
            heapq.heappush(minHeap, (val, i, j+1))

            l, r = minHeap[0][0], max(r, val) # KENG: r must update each time even it is not answer
            if r - l < ans[1] - ans[0]:
                ans = [l, r]
        return ans

    def smallestRange_kamyu(self, nums): # iter remembers both ith list and index in the list
        left, right = float("inf"), float("-inf")
        min_heap = []
        for row in nums:
            left = min(left, row[0])
            right = max(right, row[0])
            heapq.heappush(min_heap, (row[0], iter(row)))
        result = [left, right]

        while True:
            _, it = heapq.heappop(min_heap)
            val = next(it, None)
            if val is None:
                break
            heapq.heappush(min_heap, (val, it))

            left, right = min_heap[0][0], max(right, val)
            if right - left < result[1] - result[0]:
                result = [left, right]
        return result

print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])) # [20, 24]