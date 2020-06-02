# Time:  O(nlogn)
# Space: O(1)
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start) # no need key, default sorting by x[0], x[1]
        ans = [intervals[0]]
        for interval in intervals:
            if interval.start <= ans[-1].end:
                ans[-1].end = max(interval.end, ans[-1].end)
            else:
                ans.append(interval)
        return ans


if __name__ == "__main__":
    print(Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)]))
