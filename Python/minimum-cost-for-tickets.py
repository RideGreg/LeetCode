# Time:  O(n)
# space: O(1)

# 983
# In a country popular for train travel, you have planned some train travelling one year in advance.
# The days of the year that you will travel is given as an array days.  Each day is an integer
# from 1 to 365.
#
# Train tickets are sold in 3 different ways:
#
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
#
# Return the minimum number of dollars you need to travel every day in the given list of days.

# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000

# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.

from functools import lru_cache

class Solution(object):
    def mincostTickets(self, days, costs): # USE THIS
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        spend = [0] * (days[-1] + 1) # only consider up to the last day. 0,1,2...days[-1]+1, use day as list index
        for i, day in enumerate(days):
            if i:
                prev = days[i - 1]
                for k in xrange(prev+1, day):
                    spend[k] = spend[prev]

            spend[day] = min(
                (spend[day - 1] + costs[0]) if day > 1 else costs[0],
                (spend[day - 7] + costs[1]) if day > 7 else costs[1],
                (spend[day - 30] + costs[2]) if day > 30 else costs[2]
            )
        return spend[-1]

    # For each day, if you don't have to travel today, then it's strictly better to wait to buy a pass.
    # If you have to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or 30-day pass.
    #
    # We can express those choices as a recursion and use dynamic programming. Let's say dp(i) is the cost to fulfill
    # your travel plan from day i to the end of the plan. Then, if you have to travel today, your cost is:
    #
    # dp(i)=min( dp(i+1)+costs[0], dp(i+7)+costs[1], dp(i+30)+costs[2] )
    def mincostTickets_LeetcodeOfficial(self, days, costs): # reverse direction, calculate a later day first
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)
        return dp(1)

    # we only need to buy a travel pass on a day we intend to travel.
    #
    # Now, let dp(i) be the cost to travel from day days[i] to the end of the plan. If say, j1 is the largest index
    # such that days[j1] < days[i] + 1, j7 is the largest index such that days[j7] < days[i] + 7, and j30 is the
    # largest index such that days[j30] < days[i] + 30, then we have:
    #
    # dp(i)=min(dp(j1)+costs[0], dp(j7)+costs[1], dp(j30)+costs[2])
    def mincostTickets_LeetcodeOfficial2(self, days, costs):
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i): # How much money to do days[i]+
            if i >= N: return 0
            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans

        return dp(0)

    # ugly code, hard hard to understand
    def mincostTickets_kamyu(self, days, costs):
        durations = [1, 7, 30]
        W = durations[-1]
        dp = [float("inf") for i in xrange(W)]
        dp[0] = 0
        last_buy_days = [0, 0, 0]
        for i in xrange(1,len(days)+1):
            dp[i%W] = float("inf")
            for j in xrange(len(durations)):
                while i-1 < len(days) and \
                      days[i-1] > days[last_buy_days[j]]+durations[j]-1: # last_buy_days needs to maintain a duration to current day
                    last_buy_days[j] += 1  # Time: O(n)
                dp[i%W] = min(dp[i%W], dp[last_buy_days[j]%W]+costs[j])
        return dp[len(days)%W]


print(Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]))