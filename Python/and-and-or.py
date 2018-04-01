class Solution:
    """
    @param n:
    @param nums:
    @return: return the sum of maximum OR sum, minimum OR sum, maximum AND sum, minimum AND sum.
    """
    def getSum(self, n, nums):
        s1, s2 = nums[0], nums[0]
        for num in nums[1:]:
            s1 |= num
            s2 &= num
        return s1+s2+max(nums)+min(nums)
print Solution().getSum(3, [1, 2, 3])
print Solution().getSum(3,[1, 0, 0])
print Solution().getSum(5,[12313, 156, 4564, 212, 12])
print Solution().getSum(3,[111111, 333333, 555555])