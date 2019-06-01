# Time:  O(nlogn)
# Space: O(n)

# 1046
# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones
# have weights x and y with x <= y.  The result of this smash is:
# - If x == y, both stones are totally destroyed;
# - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has
# new weight y-x.

# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if
# there are no stones left.)

import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
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