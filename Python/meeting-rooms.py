# Time:  O(nlogn)
# Space: O(1)

# 252
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

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
        intervals.sort() # by default sort by 1st item, 2nd item
        return all(intervals[i][0] >= intervals[i-1][1]
                   for i in range(1, len(intervals)))

print(Solution().canAttendMeetings([(0,30),(5,10),(15,20)])) # False
print(Solution().canAttendMeetings([(5,8),(9,15)])) # True
