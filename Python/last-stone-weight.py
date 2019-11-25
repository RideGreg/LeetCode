# Time:  O(nlogn)
# Space: O(n)

# 1046 weekly contest 137 5/18/2019
# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones
# have weights x and y with x <= y.  The result of this smash is:
# - If x == y, both stones are totally destroyed;
# - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has
# new weight y-x.

# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if
# there are no stones left.)



# Heap push and pop are both O(logn) because it only rearranges log(n) elements in the list,
# doesn't shift every element.
# Binary Search finds the insertion point in O(log n) time, but the insertion step is O(n),
# making multiple insort a rather expensive way to sort.

import heapq


class Solution(object):
    def lastStoneWeight(self, stones): # USE THIS: heap O(nlogn) is faster than multiple insort O(n^2).
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        for i in range(len(stones)-1):
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -abs(x-y))
        return -max_heap[0]

    # Time O(n^2)
    def lastStoneWeight_bs(self, stones: List[int]) -> int:
        import bisect
        stones.sort()
        while len(stones) >= 2:
            a = stones.pop()
            b = stones.pop()
            if a > b:
                bisect.insort(stones, a-b)
        return stones[0] if stones else 0

print(Solution().lastStoneWeight([2,7,4,1,8,1])) # 1