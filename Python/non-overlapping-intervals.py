# Time:  O(nlogn)
# Space: O(1)

# 435
# Given a collection of intervals, find the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.
#
# Note:
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Example 1:
# Input: [ [1,2], [2,3], [3,4], [1,3] ]
#
# Output: 1
#
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
# Input: [ [1,2], [1,2], [1,2] ]
#
# Output: 2
#
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
# Input: [ [1,2], [2,3] ]
#
# Output: 0
#
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# 贪心算法可认为是动态规划算法的一个特例，相比动态规划，用贪心算法需要满足更多条件（贪心选择性质），但效率比动态规划高。
# 比如一个算法问题用暴力解法需要指数级时间，如果用动态规划消除重叠子问题，就降到多项式级别的时间，如果满足贪心选择性质，
# 那么可以进一步降低时间复杂度，达到线性级别的。

# 什么是贪心选择性质呢，简单说就是：每一步都能做出一个局部最优解，最终的结果就是全局最优。这种特殊性质只有一部分问题拥有。
# 比如你面前放着 100 张牌，你只能拿十张，怎么才能拿最多的面额？显然每次选择剩下牌中面值最大的一张，最后你的选择一定最优。

# 然而，大部分问题明显不具有贪心选择性质，得使用动态规划解决。

class Solution(object):
    # greedy O(nlogn) sort by start
    def eraseOverlapIntervals(self, intervals): # USE THIS: easy to understand
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda interval: interval[0])
        result, end = 0, intervals[0][1]
        #for i in range(1, len(intervals)):
        for x, y in intervals[1:]:
            #a, b = intervals[prev], intervals[i]
            if x < end:
                result += 1
                end = min(end, y)
            else:
                end = y
        return result

    # greedy, sort by end. Find maximal non-overlapping intervals
    def eraseOverlapIntervals(self, intervals): # a little hard to think
        if not intervals: return 0
        intervals.sort(key=lambda x: x[1])
        keep = 1
        end = intervals[0][1]
        for x, y in intervals:
            if x >= end:
                keep += 1
                end = y
        return len(intervals) - keep


    # DP time O(n^2) space O(n)
    # Sort first. dp[i] how many non-overlapping intervals existing for 0..i (included) intervals
    #   dp[0] = 1
    #   dp[i] = max(dp[j]) + 1 where 0<=j<i and intervals[j] not overlapped with intervals[i]

    # Brute Force time O(2^n)
    # Check all the possible combinations of removing a subset of intervals
