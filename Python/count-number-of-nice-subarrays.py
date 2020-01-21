# Time:  O(n)
# Space: O(1)

# 1248 weekly contest 161 11/2/2019

# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#  1<=k<=nums.length

class Solution2(object):
    def numberOfSubarrays(self, nums, k): # USE THIS: best space O(1)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(nums, k):
            result, left, count = 0, 0, 0
            for right in range(len(nums)):
                count += nums[right]%2
                while count > k:
                    count -= nums[left]%2
                    left += 1
                result += right-left+1
            return result

        return atMost(nums, k) - atMost(nums, k-1)


# Time:  O(n)
# Space: O(k)
import collections


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        dq = collections.deque([-1]) # store pos_of_odd
        for i in range(len(nums)):
            if nums[i]%2:
                dq.append(i)
            if len(dq) > k+1:
                dq.popleft()
            if len(dq) == k+1:
                # end is dq[-1], start is indices between (dq[0], dq[1]]
                result += dq[1]-dq[0]
        return result

    def numberOfSubarrays_ming(self, nums, k):
        # dict lookup {k:v} stores how many arrays [0:v] have k odd numbers
        # similar to prefix sum.
        lookup, cnt = collections.defaultdict(int), 0
        lookup[0] = 1
        for n in nums:
            cnt += n & 1
            lookup[cnt] += 1
        ans = 0
        for i in range(k, max(lookup)+1):
            ans += lookup[i]*lookup[i-k]
        return ans

print(Solution().numberOfSubarrays([1,1,2,1,1], 3)) # 2
print(Solution().numberOfSubarrays([2,4,6], 1)) # 0
print(Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)) # 16