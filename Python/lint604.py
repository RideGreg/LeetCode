class Solution:
    def winSum(self, nums, k):
        ans = [sum(nums[:k])]
        last = ans[0]
        for i in xrange(k, len(nums)):
            last += nums[i] - nums[i-k]
            ans.append(last)
        return ans

print Solution().winSum([1,2,7,8,5], 3)