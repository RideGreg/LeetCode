# Time:  O((|E| + |V|) * log|V|) = O(|E| * log|V|) by using binary heap,
#        since all nodes may add to heap and sort in heap takes log|V| time;
#        if we can further to use Fibonacci heap, it would be O(|E| + |V| * log|V|)
# Space: O(|E| + |V|) = O(|E|)

# 743
# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node,
# and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K.
# How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
# Note:
# - N will be in the range [1, 100].
# - K will be in the range [1, N].
# - The length of times will be in the range [1, 6000].
# - All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

import collections
import heapq

# Dijkstra's algorithm
class Solution(object):
    def networkDelayTime(self, times, N, K): # USE THIS
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u,v,w in times:
            graph[u][v] = w
        delay = [0] + [float('inf')] * N
        delay[K] = 0

        seen = set() # this problem is not ask delay to a specific node. It asks min delay
                     # to reach all nodes, as we saw all nodes, we get min delay due to using minHeap.
        minHeap = [(0, K)]
        while minHeap and len(seen) < N:
            d, node = heapq.heappop(minHeap)
            seen.add(node)
            if d > delay[node]: continue
            for nei, w in graph[node].items():
                if d+w < delay[nei]:
                    delay[nei] = d+w
                    heapq.heappush(minHeap, (d+w, nei))
        return d if len(seen) == N else -1
        #ans = max(delay)
        #return ans if ans < float('inf') else -1

    def networkDelayTime_dictForDist(self, times, N, K): # code seems simpler, dict takes more space
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u,v,w in times:
            graph[u][v] = w
        delay = {}       # more space than [float('inf')] * N

        minHeap = [(0, K)]
        while minHeap and len(delay) < N:
            d, node = heapq.heappop(minHeap)
            if node in delay: continue   # only shortest path will be visited
            delay[node] = d
            for nei, w in graph[node].items():
                if nei not in delay:
                    heapq.heappush(minHeap, (d+w, nei))
        return d if len(delay) == N else -1

    def networkDelayTime_kamyu(self, times, N, K):
        adj = [[] for _ in xrange(N)]
        for u, v, w in times:
            adj[u-1].append((v-1, w))

        result = 0
        lookup = set()
        best = collections.defaultdict(lambda: float("inf"))
        min_heap = [(0, K-1)]
        while min_heap and len(lookup) != N:
            result, u = heapq.heappop(min_heap)
            lookup.add(u)
            if best[u] < result:
                continue
            for v, w in adj[u]:
                if v in lookup: continue
                if result+w < best[v]:
                    best[v] = result+w
                    heapq.heappush(min_heap, (result+w, v))
        return result if len(lookup) == N else -1

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2