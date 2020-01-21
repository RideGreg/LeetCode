# Time:  O(n)
# Space: O(1)

# 1262 weekly contest 163 11/16/2019

# Given an array nums of integers, we need to find the maximum possible sum of elements of the array
# such that it is divisible by three.

# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4

class Solution(object):
    def maxSumDivThree(self, nums): # USE THIS: lee215. can get greatest sum of 3x, 3x+1, 3x+2
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0] # current maximum possible sum that sum % 3 = i
        for num in nums:
            temp = [num+x for x in dp]
            for i in temp:
                dp[i%3] = max(dp[i%3], i)
        return dp[0]

    # return value not easy to scale if 3x change to 7x...
    def maxSumDivThree_ming(self, nums):
        total, mod1s, mod1m, mod2s, mod2m = 0, float('inf'), float('inf'), float('inf'), float('inf')
        mod1cnt, mod2cnt = 0, 0
        for n in nums:
            total += n
            if n % 3 == 1:
                mod1cnt += 1
                if n < mod1s:
                    mod1m, mod1s = mod1s, n
                elif n < mod1m:
                    mod1m = n
            elif n % 3 == 2:
                mod2cnt += 1
                if n < mod2s:
                    mod2m, mod2s = mod2s, n
                elif n < mod2m:
                    mod2m = n
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            return total - min(mod1s, mod2s+mod2m)
        else:
            return total - min(mod2s, mod1s+mod1m)

print(Solution().maxSumDivThree([3,6,5,1,8])) # 18
print(Solution().maxSumDivThree([4])) # 0
print(Solution().maxSumDivThree([1,2,3,4,4])) # 12