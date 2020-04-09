# Time:  O((w * b) * log(w * b))
# Space: O(w * b)

# 1057

# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike
# is a 2D coordinate on this grid.
#
# Our goal is to assign a bike to each worker. Among the available bikes and workers, choose the (worker, bike)
# pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there
# are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the
# smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index).
# We repeat this process until there are no available workers.
#
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
#
# Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker
# is assigned to.
#
# All worker and bike locations are distinct.

import heapq


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        distances = [[] for _ in range(len(workers))]
        # calculate distance for all paris, grouping result bu worker id
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances[i].append((manhattan(workers[i], bikes[j]), i, j))
            distances[i].sort(reverse = True)
        
        result = [None] * len(workers)
        lookup = set()
        min_heap = []
        # retrieve pairs w/ min distance for all workers.
        for i in range(len(workers)):
            heapq.heappush(min_heap, distances[i].pop())

        # retrieve the pair w/ smallest distance; if the bike is used, retrieve 2nd bike and refill min_heap.
        while len(lookup) < len(workers):
            _, worker, bike = heapq.heappop(min_heap)
            if bike not in lookup:
                result[worker] = bike
                lookup.add(bike)
            else:
                heapq.heappush(min_heap, distances[worker].pop())
        return result

print(Solution().assignBikes([[0,0],[2,1]], [[1,2],[3,3]])) # [1, 0]
print(Solution().assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]])) # [0, 2, 1]