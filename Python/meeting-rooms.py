# Time:  O(nlogn)
# Space: O(n)
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # @param {Interval[]} intervals
    # @return {boolean}
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])

        for i in xrange(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
