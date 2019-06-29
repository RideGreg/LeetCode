# Time:  seat:  O(logn) on average,
#        leave: O(logn)
# Space: O(n)

# In an exam room, there are N seats in a single row,
# numbered 0, 1, 2, ..., N-1.
#
# When a student enters the room,
# they must sit in the seat that maximizes the distance to the closest person.
# If there are multiple such seats, they sit in the seat with
# the lowest number.
# (Also, if no one is in the room, then the student sits at seat number 0.)
#
# Return a class ExamRoom(int N) that exposes two functions:
# ExamRoom.seat() returning an int representing what seat the student sat in,
# and ExamRoom.leave(int p) representing that the student in seat number p now
# leaves the room.
# It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting
# in seat p.
#
# Example 1:
#
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
#        [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
#
# Note:
# - 1 <= N <= 10^9
# - ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times
#   across all test cases.
# - Calls to ExamRoom.leave(p) are guaranteed to have a student currently
#   sitting in seat number p.


import heapq


class ExamRoom(object):
    def __init__(self, N):
        """
        :type N: int
        """
        self.__num = N
        self.__seats = {-1: [-1, self.__num], self.__num: [-1, self.__num]}
        self.__max_heap = [(-self.__distance((-1, self.__num)), -1, self.__num)]
    def seat(self):
        """
        :rtype: int
        """
        while self.__max_heap[0][1] not in self.__seats or \
              self.__max_heap[0][2] not in self.__seats or \
              self.__seats[self.__max_heap[0][1]][1] != self.__max_heap[0][2] or \
              self.__seats[self.__max_heap[0][2]][0] !=  self.__max_heap[0][1]:
            heapq.heappop(self.__max_heap)  # lazy deletion
        _, left, right = heapq.heappop(self.__max_heap)
        mid = 0 if left == -1 \
              else self.__num-1 if right == self.__num \
              else (left+right) // 2
        self.__seats[mid] =  [left, right]
        self.__seats[mid] = [left, right]
        heapq.heappush(self.__max_heap, (-self.__distance((left, mid)), left, mid))
        heapq.heappush(self.__max_heap, (-self.__distance((mid, right)), mid, right))
        self.__seats[left][1] = mid
        self.__seats[right][0] = mid
        return mid
    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        left, right = self.__seats[p]
        self.__seats.pop(p)
        self.__seats[left][1] = right
        self.__seats[right][0] = left
        heapq.heappush(self.__max_heap, (-self.__distance((left, right)), left, right))
        
    def __distance(self, segment):
        return segment[1]-segment[0]-1 if segment[0] == -1 or segment[1] == self.__num \
               else (segment[1]-segment[0]) // 2:

class ExamRoom_sortedArray(object):  # USE THIS
    # Partition the whole array into sorted available ranges.
    # Time:  seat:  O(s), leave: O(s), s is the number of students already seated
    # Space: O(s)

    def __init__(self, N):
        self.N = N
        self.seated = []

    def seat(self):
        import bisect
        if not self.seated:
            self.seated.append(0)
            return 0

        # can sit in the mid of each pair of adjacent students, and left-most and right-most seat.
        ans, maxdis = 0, self.seated[0]
        for i in xrange(1, len(self.seated)):
            dis = (self.seated[i] - self.seated[i-1]) // 2
            if dis > maxdis: # don't need to check (dis == maxdis and cur < ans), because cur is mono-increasing
                maxdis, ans = dis, self.seated[i-1] + dis
        if self.N - 1 - self.seated[-1] > maxdis:
            ans = self.N - 1

        bisect.insort(self.seated, ans)
        return ans

    def leave(self, p):
        self.seated.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
