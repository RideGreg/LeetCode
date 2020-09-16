# Time:  O(nlogn) for total n addNums, O(logn) per addNum, O(1) per findMedian.
# Space: O(n), total space

# 295
# Median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value.
# So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
#
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3)
# findMedian() -> 2

# Heap solution.
# minHeap stores larger half, maxHeap stores smaller half. Large number comes into minHeap,
# small number comes into maxHeap.
# Maintain len(minHeap) == len(maxHeap) or len(maxHeap) + 1
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        """Initialize your data structure here."""
        self.__max_heap = []
        self.__min_heap = []

    def addNum(self, num):
        """Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # Balance smaller half and larger half.
        if not self.__max_heap or num > self.__min_heap[0]:
            heappush(self.__min_heap, num)
            if len(self.__min_heap) > len(self.__max_heap) + 1:
                heappush(self.__max_heap, -heappop(self.__min_heap))
        else:
            heappush(self.__max_heap, -num)
            if len(self.__max_heap) > len(self.__min_heap):
                heappush(self.__min_heap, -heappop(self.__max_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.__min_heap) == len(self.__max_heap):
            return (-self.__max_heap[0] + self.__min_heap[0]) / 2
        else:
            return self.__min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
for i in range(1, 10, 2):
    mf.addNum(i)
    print(mf.findMedian()) # 1,2,3,4,5
for i in range(2, 12, 2):
    mf.addNum(i)
    print(mf.findMedian()) # 4, 4, 4.5, 5, 5.5

# minHeap [1]  [3]  [3,5] [5,7]   [5,7,9] [5,7,9]    [4,5,7,9]  [5,6,7,9]     [5,6,9,7,8]   [6,7,9,10,8]
# maxHeap []   [-1] [-1]  [-3,-1] [-3,-1] [-3,-1,-2] [-3,-1,-2] [-4,-3,-2,-1] [-4,-3,-2,-1] [-5,-4,-2,-1,-3]
