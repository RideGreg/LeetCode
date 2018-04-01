class Solution(object):
    def pivotIndex(self, nums):
        ans = -1
        if not nums:
            return ans
        total = sum(nums)
        l, r = 0, total - nums[0]
        if l == r: return 0
        for i in xrange(1, len(nums)):
            l += nums[i-1]
            r -= nums[i]
            if l == r:
                return i
        return ans


print Solution().pivotIndex([1, 7, 3, 6, 5, 6])
print Solution().pivotIndex([1, 2, 3])
print Solution().pivotIndex([1])
print Solution().pivotIndex([])

