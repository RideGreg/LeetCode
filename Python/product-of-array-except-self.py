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

        left_product = [1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = 1
        for i in xrange(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product

        return left_product

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