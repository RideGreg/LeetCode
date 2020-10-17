# Time:  O(n * logm), n is total number of schedule, m is the number of employees, n >= m
# Space: O(m)

# 759
# We are given a list schedule of employees, which represents the working time for each employee.
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
#
# Example 1:
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation:
# There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
#
# Example 2:
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
# (Even though we are representing Intervals in the form [x, y],
#  the objects inside are Intervals, not lists or arrays.
#  For example, schedule[0][0].start = 1, schedule[0][0].end = 2,
# and schedule[0][0][0] is not defined.)
#
# Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
#
# Note:
# - schedule and schedule[i] are lists with lengths in range [1, 50].
# - 0 <= schedule[i].start < schedule[i].end <= 10^8.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# 与 LC 986 interval-list-intersections, LC 1229 meeting-scheduler 不同的是：
# 1. 多个list，不是2个list -> 用two pointers很难做，必须用heap，但每个list自己是sorted，所以只放m entries not all entries； 
# 2. 求不交叉interval，不是求intersections
# 3. 如果pop out by startTime，必须记录last_end；如果pop out by endTime， 需要跟heap里剩下的最小startTime比，
#    像LC 1229 meeting-scheduler那样，这题由于没有把所以entries一次全放入heap，不好copy LC 1229.

import heapq

# insert interval: O(n)
# merge interval: sort all intervals O(nlogn)

class Solution(object):
    # This solution time O(nlogm) better than solution 2 O(nlogn), because each employee's intervals
    # are sorted, we don't need to sort all intervals.
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        result = []
        # heap item (start, eid, idx_in_eid_schedule)
        min_heap = [(times[0][0], eid, 0) for eid, times in enumerate(schedule)]
        heapq.heapify(min_heap)
        last_end = -1
        while min_heap:
            start, eid, i = heapq.heappop(min_heap)
            if 0 <= last_end < start:
                result.append([last_end, start])
            last_end = max(last_end, schedule[eid][i][1])

            if i < len(schedule[eid]) - 1:
                heapq.heappush(min_heap, (schedule[eid][i+1][0], eid, i+1))
        return result

    # Time O(nlogn) similar to LC 253 meeting-room-ii
    def employeeFreeTime2(self, schedule):
        times = [x for sch in schedule for s, e in sch for x in [[s, 1], [e, -1]]]
        times.sort()
        freeTimeStart, busyEmp, ans = None, 0, []
        for time, delta in times:
            busyEmp += delta
            if busyEmp == 1 and freeTimeStart is not None:
                ans.append([freeTimeStart, time])
                freeTimeStart = None
            elif busyEmp == 0:
                freeTimeStart = time
        return ans


print(Solution().employeeFreeTime([[[1,2],[5,6]], [[1,3]], [[4,10]]])) # [[3,4]]
print(Solution().employeeFreeTime([[[1,2],[5,6]], [[0,3]], [[4,10]]])) # [[3,4]]
print(Solution().employeeFreeTime([[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]])) # [[5,6],[7,9]]