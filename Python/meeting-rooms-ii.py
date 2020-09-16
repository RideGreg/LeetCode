# Time:  O(nlogn)
# Space: O(n)

# 253
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...]
# find the minimum number of conference rooms required.

# Solution: http://www.cnblogs.com/grandyang/p/5244720.html

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution: # USE THIS
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        result, curr = 0, 0
        line = [x for s, e in intervals for x in [[s, 1], [e, -1]]]
        line.sort()
        for _, num in line:
            curr += num
            result = max(result, curr)
        return result

    # follow up: input is list of list of int (each worker's meeting time), ask the time interval no worker is using any meeting room
    def freeTimes(self, intervals):
        result, curr, start = [], 0, None
        line = [x for interval in intervals for s, e in interval for x in [[s, 1], [e, -1]]]
        line.sort()
        for t, num in line:
            curr += num
            if curr == 0:
                start = t
            elif curr == 1 and start is not None:
                result.append([start, t])
        return result

# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        starts, ends = [], []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1

        return min_rooms


# Time: O(nlogn)
# Space: O(n)
from heapq import heappush, heappop


class Solution3(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        
        heappush(free_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heappop(free_rooms)
            
            heappush(free_rooms, interval[1])
        
        return len(free_rooms)

print(Solution().minMeetingRooms([(2,15), (36,45), (9,29), (16,23), (4,9)])) # 2
print(Solution().minMeetingRooms([(0,30), (5,10), (15,20)])) # 2

print(Solution().freeTimes([[[1,3], [6,7]], [[2, 4]], [[2, 3], [9, 12]]])) # [[4,6], [7,9]]
