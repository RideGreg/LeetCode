# Time:  O(n) ~ O(nlogn)
# Space: O(n)

# 1229 biweekly contest 11 10/19/2019
# Given the availability time slots arrays 'slots1' and 'slots2' of two people and a meeting duration 'duration',
# return the earliest time slot that works for both of them and is of duration 'duration'.
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

import heapq


# if input sorted, similar to LC 986 interval-list-intersection.py. Since input not sorted, need to put all entries in
# heap to auto sort (still better than full sort); and we only need first answer, consider not to full sort (heapify) 
class Solution(object): # USE THIS
    def minAvailableDuration(self, slots1, slots2, duration): # Best time complexity: no need sort all
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        min_heap = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))  # O(n)
        heapq.heapify(min_heap)    # Transform list x into a heap, in-place, in linear time: O(n)
        while len(min_heap) > 1:   # worst case O(n), best case O(1)
            left = heapq.heappop(min_heap)   # Time: O(logn)
            right = min_heap[0]
            if left[1]-right[0] >= duration:
                return [right[0], right[0]+duration]
        return []


# Time:  O(nlogn), n is len(slots1) + len(slots2)
# Space: O(1)
class Solution2(object):
    def minAvailableDuration(self, slots1, slots2, duration): # ALSO GOOD: line sweep
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort() # sort on first item by default, O(nlogn)
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            left = max(slots1[i][0], slots2[j][0])
            right = min(slots1[i][1], slots2[j][1])
            if left+duration <= right:
                return [left, left+duration]

            #if s1 < s2 or (s1==s2 and e1 < e2): # KENG: should discard small endTime, not small beginTime!! [[10,100]], [[20,25], [30,50]], 10
            # in both the following 2 cases, should discard period #2 which has smaller endTime
            # ------1----------
            #  -2-  ----3-----

            #   ------1---------
            #  -2-  ----3-----
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []

    # sort both slots together, code relatively shorter
    def minAvailableDuration_awice(self, slots1, slots2, duration):  # ALSO GOOD
        events = []
        OPEN, CLOSE = 0, 1
        for a, b in slots1:
            events.append((a, OPEN))
            events.append((b, CLOSE))
        for a, b in slots2:
            events.append((a, OPEN))
            events.append((b, CLOSE))

        events.sort() # O(nlogn)
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


print(Solution().minAvailableDuration([[10,100]], [[20,25], [30,50]], 10)) # [30, 40]
print(Solution().minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], duration = 8)) # [60,68]
print(Solution().minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], duration = 12)) # []
print(Solution().minAvailableDuration(
[[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]],
[[ 50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]],
456085)) # [98730764, 99186849]