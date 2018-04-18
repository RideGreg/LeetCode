# Time:  O(n * S)
# Space: O(S)

# You are given a list of non-negative integers, a1, a2, ..., an,
# and a target, S. Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
import collections

import collections


class Solution(object):
    def findTargetSumWays(self, nums, S): #subset sum
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def subsetSum(nums, S):
            print "S = ", S
            cnt  = 0
            dp = collections.defaultdict(int)
            dp[0] = 1
            for n in nums:
                print "n = ", n
                for i in reversed(xrange(n, S+1)):
                    #print "i = ", i
                    if i-n in dp:
                        cnt += 1
                        dp[i] += dp[i-n]
                        print dp
            print cnt
            return dp[S]

        total = sum(nums)
        if total < S or (S + total) % 2: return 0
        P = (S + total) // 2
        return subsetSum(nums, P)

    def findTargetSumWays_easyPython(self, nums, S):
        if not nums:
            return 0
        sums = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {0:2}
        cnt = 0
        for n in nums[1:]:
            sums_new = {}
            for k in sums:
                cnt += 1
                sums_new[k+n] = sums_new.get(k+n, 0) + sums[k]
                sums_new[k-n] = sums_new.get(k-n, 0) + sums[k]
            sums = sums_new
        print cnt
        return sums.get(S, 0)

    def findTargetSumWays_BruteForce(self, nums, S): #TLE O(2^n)
        self.ans = 0

        def dfs(nums, S, pos):
            if pos == len(nums):
                if S == 0:
                    self.ans += 1
            else:
                dfs(nums, S - nums[pos], pos + 1)
                dfs(nums, S + nums[pos], pos + 1)

        dfs(nums, S, 0)
        return self.ans

#print Solution().findTargetSumWays_easyPython([1,1,1,1,1,1,1,1,1,2,2,3,3,4,4], 3)
print Solution().findTargetSumWays([1,1,1,1,1], 3)