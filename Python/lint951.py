class Solution:
    """
    @param nums: the num arrays
    @return: the num arrays after rearranging
    """
    def rearrange(self, nums):
        nums.sort()
        k = (len(nums)+1) / 2
        a, b = nums[:k], nums[k:]
        if len(nums)%2:
            b.append(0)
        ans = [i for ab in zip(a,b) for i in ab]
        return ans[:-1] if len(nums)%2 else ans

print Solution().rearrange([-1,0,1,-1,5,10])
print Solution().rearrange([-1,0,1,-1,5])
print Solution().rearrange([2,0,1,-1,5,10])


