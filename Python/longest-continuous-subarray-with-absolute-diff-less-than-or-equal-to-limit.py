# Time:  O(n)
# Space: O(n)

# 1438
# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray
# such that the absolute difference between any two elements of this subarray is less than or equal to limit.

import collections


# maxq stores all potential max num to the current index -> mono decreasing stack, head is largest in range [left, right]
# minq stores all potential min num to the current index -> mono increasing stack, head is smallest in range [left, right]
class Solution(object):
    def longestSubarray(self, nums, limit): # USE THIS
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        maxq, minq = collections.deque(), collections.deque()
        result, left = 0, 0
        for right, num in enumerate(nums):
            while maxq and num >= nums[maxq[-1]]:
                maxq.pop()
            maxq.append(right)
            while minq and num <= nums[minq[-1]]:
                minq.pop()
            minq.append(right)

            while nums[maxq[0]]-nums[minq[0]] > limit:  # maintain a valid [left, right] range
                left = min(maxq[0], minq[0])
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                left += 1
            result = max(result, right-left+1)  # KENG: have to use left as boundary, cannot use min(maxq[0], minq[0])
                                                # because many valid head was popped
        return result


    def longestSubarray2(self, nums, limit):
        maxq, minq = collections.deque(), collections.deque()
        left = 0
        for right, num in enumerate(nums):
            while maxq and nums[maxq[-1]] <= num:
                maxq.pop()
            maxq.append(right)
            while minq and nums[minq[-1]] >= num:
                minq.pop()
            minq.append(right)

            if nums[maxq[0]]-nums[minq[0]] > limit:
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                left += 1  # advance left by one to not count in result
        return len(nums)-left


    def longestSubarray_wrong(self, nums, limit): # wrong for [6,10,5], 4
        ans, q = 0, collections.deque()
        for i in range(len(nums)):
            while q and abs(nums[i] - nums[q[0]]) > limit:
                q.popleft()
            q.append(i)
            ans = max(ans, q[-1] - q[0] + 1)
        return ans

print(Solution().longestSubarray([6,10,5], 4)) # 2
print(Solution().longestSubarray([9,8,7,6,10,5], 4)) # 5
print(Solution().longestSubarray([8,2,4,7], 4)) # 2
print(Solution().longestSubarray([10,1,2,4,7,2], 5)) # 4
print(Solution().longestSubarray([4,2,2,2,4,4,2,2], 0)) # 3