class Solution(object):
    def splitArraySameAverage(self, nums):
        def foo(nums, i, sum, size):
            if size == 0:
                return sum == 0
            if i >= len(nums):
                return True if sum==0 and size==0 else False
            return foo(nums, i+1, sum, size) or foo(nums, i+1, sum-nums[i], size-1)

        avg = sum(nums) / float(len(nums))
        for k in xrange(1, len(nums)):
            kk = float(k) * avg
            if kk == int(kk) and foo(nums, 0, kk, k):
                return True
        return False

print Solution().splitArraySameAverage([2, -2, 0])
print Solution().splitArraySameAverage([2, -2, 1,1,-2])

print Solution().splitArraySameAverage([2,3,4])

print Solution().splitArraySameAverage([1,2,3,4,5,6,7,8])
