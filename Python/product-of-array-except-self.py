# Time:  O(n)
# Space: O(1)
# 238
# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to
# the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
#
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space
# for the purpose of space complexity analysis.)
#

class Solution:
    # for product on any index i, first scan (left->right) get A[0]*A[1]*..A[i-1]
    # second scan (right->left) get A[n-1]*A[n-2]...*A[i+1]
    def productExceptSelf(self, nums):
        if not nums:
            return []

        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        rightMult = 1
        for i in range(len(nums)-2, -1, -1):
            rightMult *= nums[i+1]
            ans[i] *= rightMult
        return ans

    # use division
    def productExceptSelf_useDivision(self, nums):
        import operator
        from functools import reduce

        N = len(nums)
        cntZero = nums.count(0)
        if cntZero > 1:
            return [0] * N
        elif cntZero == 1:
            idx = nums.index(0)
            prod = reduce(operator.__mul__, nums[:idx]+nums[idx+1:])
            ans = [0] * N
            ans[idx] = prod
            return ans
        else:
            prod = reduce(operator.__mul__, nums)
            return [prod//x for x in nums]

print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]