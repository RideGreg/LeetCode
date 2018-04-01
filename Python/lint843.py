class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        if nums[0] == 0:
            zeros, ones = [1], [0]
        else:
            zeros, ones = [0], [1]
        for n in nums[1:]:
            zeros.append(zeros[-1]+(1 if n==0 else 0))
            ones.append(ones[-1] + (1 if n == 1 else 0))

        ans = ones[-1]
        for zeroStart in xrange(1, len(nums)+1):
            cur = zeros[zeroStart-1] + (ones[-1]-ones[zeroStart-1])
            ans = min(ans, cur)
        return ans

print Solution().flipDigit([1,0,0,1,1,1])
print Solution().flipDigit([1,0,1,0,1,0])