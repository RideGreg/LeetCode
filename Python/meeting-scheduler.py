# Time:  O(n) ~ O(nlogn)
# Space: O(n)

# 1229 biweekly contest 11 10/19/2019
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
# return the earliest time slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements, return an empty array.
#
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
#
# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for
# any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

# Constraints:
#
# 1 <= slots1.length, slots2.length <= 10^4
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 10^9
# 1 <= duration <= 10^6


# Time:  O(nlogn)
# Space: O(n)
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration): # USE THIS
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort() # sort on first item by default
        slots2.sort()
        x, y = 0, 0
        while x < len(slots1) and y < len(slots2):
            s1, e1 = slots1[x]
            s2, e2 = slots2[y]
            start, end = max(s1, s2), min(e1, e2)
            if duration <= end - start:
                return [start, start+duration]

            #if s1 < s2 or (s1==s2 and e1 < e2): # KENG: this is WRONG!! [[10,100]], [[20,25], [30,50]], 10
            if e1 < e2:
                x += 1
            else:
                y += 1
        return []

    # divide start and end makes the solution complext, just for a new idea
    def minAvailableDuration_awice(self, slots1, slots2, duration):
        events = []
        OPEN, CLOSE = 0, 1
        for a, b in slots1:
            events.append((a, OPEN))
            events.append((b, CLOSE))
        for a, b in slots2:
            events.append((a, OPEN))
            events.append((b, CLOSE))

        events.sort()
        prev = events[0][0]
        active = 0
        for x, cmd in events:
            if active == 2 and x - prev >= duration:
                return [prev, prev + duration]

            if cmd == OPEN:
                active += 1
            else:
                active -= 1

            prev = x
        return []

import heapq

class Solution2(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        min_heap = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        heapq.heapify(min_heap)  # Time: O(n)
        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)  # Time: O(logn)
            right = min_heap[0]
            if left[1]-right[0] >= duration:
                return [right[0], right[0]+duration]
        return []


print(Solution().minAvailableDuration([[10,100]], [[20,25], [30,50]], 10)) # [30, 40]
print(Solution().minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], duration = 8)) # [60,68]
print(Solution().minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], duration = 12)) # []
print(Solution().minAvailableDuration(
[[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]],
[[ 50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]],
456085)) # [98730764, 99186849]