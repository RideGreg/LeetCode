class Solution:
    def subsetWithTarget(self, nums, target):
        ans = 0
        nums.sort()
        for i, n in enumerate(nums):
            if n*2 >= target:
                break
            l, r = i, len(nums)-1
            while l<=r:
                m = (r - l) / 2 + l
                if nums[i] + nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            ans += 2**(r-i)
        return ans

print Solution().subsetWithTarget([1,5,2,4,3],4)
print Solution().subsetWithTarget([1,5,2,4,3],5)
print Solution().subsetWithTarget([1,5,2,-2,4,3],4)


