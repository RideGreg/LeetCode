# Time:  O(nlogn)
# Space: O(n)

# 1235 weekly contest 159 10/19/2019

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
# obtaining a profit of profit[i].
#
# You're given the startTime , endTime and profit arrays, you need to output the maximum profit
# you can take such that there are no 2 jobs in the subset with overlapping time range.
#
# If you choose a job that ends at time X you will be able to start another job that starts at time X.

import itertools
import bisect


class Solution(object):
    # compare to 646. Maximum Length of Pair Chain.
    # For Unweighted Interval Scheduling, we use greedy algorithm. First sort by finish time
    # (ascending order) then decide whether to fit the next interval in based on its start time.
    # See the prove here http://www.cs.cornell.edu/courses/cs482/2007su/ahead.pdf.

    # But Greedy algorithm can fail spectacularly if arbitrary weights are allowed. So need DP.
    # Greedy does local optimization and DP does global optimization.
    # For this problem we still first sort by finish time (ascending order) then use DP to
    # decide whether it is profitable to put in the next interval based on its value.
    # Use bisect to locate the maximum possible profit.
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        import operator
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        # dp (time, profit) means that within the first 'time', we make at most 'profit' money.
        dp = [(0, 0)]
        for s, e, p in jobs:
            # bisect in the dp to find the largest profit we can make before start time s.
            # because items in dp has increasing profit, so the last item current start time can
            # fit in will have largest profit.
            i = bisect.bisect_right(dp, (s, float('inf')))

            # if making more money, choose this job, add pair of [e, newProfit] to end of dp
            if dp[i-1][1]+p > dp[-1][1]:
                dp.append((e, dp[i-1][1]+p))
        return dp[-1][1]

    # dfs: O(2^n)
    def jobScheduling_TLE(self, startTime, endTime, profit):
        def dfs(i, lastEnd, cur):
            if i == N:
                self.ans = max(self.ans, cur)
                return

            dfs(i + 1, lastEnd, cur)
            if jobs[i][0] >= lastEnd:
                dfs(i + 1, jobs[i][1], cur + jobs[i][2])

        jobs = sorted(zip(startTime, endTime, profit))
        N, self.ans = len(jobs), 0
        dfs(0, float('-inf'), 0)
        return self.ans

# Time:  O(nlogn)
# Space: O(n)
import heapq
class Solution2(object): # hard to understand
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        min_heap = list(zip(startTime, endTime, profit))
        heapq.heapify(min_heap)
        result = 0
        while min_heap:
            s, e, p = heapq.heappop(min_heap)
            if s < e:
                heapq.heappush(min_heap, (e, s, result+p))
            else:
                result = max(result, p)
        return result


print(Solution().jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])) # 120=50+70
print(Solution().jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])) # 150 = 20+70+60
print(Solution().jobScheduling([1,1,1],[2,3,4],[5,6,4])) # 6