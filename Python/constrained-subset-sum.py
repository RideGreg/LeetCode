# Time:  O(n)
# Space: O(k)

# 1425
# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of
# that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j],
# where i < j, the condition j - i <= k is satisfied.
#
# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array,
# leaving the remaining elements in their original order.
#
import collections


class Solution(object):
    # mono stack + queue stores (index, max sum of subseq ending with this index) for later accumulation:
    # - sums are in mono decreasing order, i.e. if larger value comes, pop all smaller values from queue tail,
    # so head of values is always the largest. Negative or zero sums don't push to queue as it doesn't help.
    # - index is used to control distance <= k, pop from head the far index.
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result, q = float("-inf"), collections.deque()
        for i in range(len(nums)):
            if q and i - q[0][0] > k: # control the distance between index
                q.popleft()

            curSum = nums[i] + (q[0][1] if q else 0)
            while q and curSum >= q[-1][1]:   # pop from tail
                q.pop()
            if curSum > 0:
                q.append((i, curSum))

            result = max(result, curSum)
        return result

    # DP + mono stack: not best solution
    def constrainedSubsetSum2(self, nums, k):
        import heapq, collections
        dp = list(nums)
        hp = collections.deque([])
        m = float('-inf')
        for i in range(1, len(nums)):
            if len(hp) >= k:
                mm = hp.popleft()
                if mm == m:
                    m = heapq.nlargest(1, hp)[0] if hp else float('-inf')
            hp.append(dp[i-1])
            m = max(m, dp[i-1])
            dp[i] = dp[i] + max(0, m)
        return max(dp)

print(Solution().constrainedSubsetSum([10,2,-10,5,20], 2)) # 37
print(Solution().constrainedSubsetSum([-1,-2,-3], 1)) # -1
print(Solution().constrainedSubsetSum([10,-2,-10,-5,20], 2)) # 23