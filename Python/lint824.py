class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        l, r = 0, len(nums)-1
        while r-l+1 > 2:
            mid = (r-l)/2 + l
            if (mid-l+1) % 2:
                if nums[mid] == nums[mid+1]:
                    l = mid + 2
                else:
                    r = mid
            else:
                if nums[mid] == nums[mid+1]:
                    r = mid - 1
                else:
                    l = mid + 1

        if r == l:
            return nums[l]
        elif r == l + 1:
            return nums[l] if r%2 else nums[r]

print Solution().getSingleNumber([4,3,3,2,2,5,5])
print Solution().getSingleNumber([3,3,4,2,2,5,5])
print Solution().getSingleNumber([3,3,2,2,4,5,5])
print Solution().getSingleNumber([3,3,2,2,5,5,4])
print Solution().getSingleNumber([2,1,1,3,3])
print Solution().getSingleNumber([1,1,2,3,3])
print Solution().getSingleNumber([1,1,3,3,2])
print Solution().getSingleNumber([4,3,3,2,2,5,5,6,6])
print Solution().getSingleNumber([3,3,4,2,2,5,5,6,6])
print Solution().getSingleNumber([3,3,2,2,4,5,5,6,6])
print Solution().getSingleNumber([3,3,2,2,5,5,4,6,6])
print Solution().getSingleNumber([3,3,2,2,5,5,6,6,4])
print Solution().getSingleNumber([2,3,3])
print Solution().getSingleNumber([3,3,2])
