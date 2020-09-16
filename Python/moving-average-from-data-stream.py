# Time:  O(1)
# Space: O(w)

# 346
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.__size = size
        self.__sum = 0
        self.__q = deque([])

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += val
        self.__q.append(val)
        return self.__sum / len(self.__q)


# Your MovingAverage object will be instantiated and called as such:
m = MovingAverage(3)
print(m.next(1)) # 1.0
print(m.next(10)) # (1 + 10) / 2 = 5.5
print(m.next(3)) # (1 + 10 + 3) / 3 = 4.66
print(m.next(5)) # (10 + 3 + 5) / 3 = 6.0
