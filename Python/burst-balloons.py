# Time:  O(n^3)
# Space: O(n^2)

# Given n balloons, indexed from 0 to n-1.
# Each balloon is painted with a number on it
# represented by array nums.
# You are asked to burst all the balloons.
# If the you burst balloon i you will get
# nums[l] * nums[i] * nums[r] coins.
# Here l and r are adjacent indices of i.
# After the burst, the l and r then
# becomes adjacent.
#
# Find the maximum coins you can collect by
# bursting the balloons wisely.
#
# Note:
# (1) You may imagine nums[-1] = nums[n] = 1.
#     They are not real therefore you can not burst them.
# (2) 0 <= n <= 500, 0 <= nums[i] <= 100
#
# Example:
#
# Given [3, 1, 5, 8]
#
# Return 167
#
#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

# There seems to be many self similar sub problems.
#
# The nature way to divide the problem is burst one balloon and separate the balloons
# into 2 sub sections one on the left and one on the right. However, in this problem
# the left and right become adjacent and have effects on the maxCoins in the future.
#
# Then another idea come up. That is reverse thinking. Like I said the coins you get for a balloon does not depend
# on the balloons already burst. Therefore
# instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.
#
# Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!
# For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].


# 以最后被爆破的气球m为界限，把数组分为左右两个子区域
#
# 状态转移方程：
# dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])
#
# dp[l][r]表示扎破(l, r)范围内所有气球获得的最大硬币数，不含边界；因为m是最后被爆破
# 所以跟两个边界的气球相乘。
#
# l与r的跨度k从2开始逐渐增大；
# 三重循环依次枚举范围跨度k，左边界l，中点m；右边界r = l + k；
# 状态转移方程在形式上有点类似于Floyd最短路算法。

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coins = [1] + [i for i in nums if i > 0] + [1]
        n = len(coins)
        dp = [[0] * n for _ in range(n)]

        for k in xrange(2, n):
            for l in xrange(n - k):
                r = l + k
                for m in xrange(l + 1, r):
                    dp[l][r] = max(dp[l][r],
                                   coins[l] * coins[m] * coins[r] + dp[l][m] + dp[m][r])

        return dp[0][-1]

print(Solution().maxCoins([3,1,5,8])) # 167
print(Solution().maxCoins([3,1,0,8])) # 56 => [3,1,8] => [3,8] => [8]

