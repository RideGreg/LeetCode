# find shortest paths from a "source" node to all other nodes in a weighted directed graph,
# producing a shortest-path tree (a subset of edges of original tree).
# Also apply to undirected graph which is just a directed graph with bidirectional connections.
# BFS is actaully Dijkstra for unweighted graph.

# https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e

import heapq

class Solution(object):
    def dijkstra_DG(self, edges, N):
        graph = [{} for _ in xrange(N)]
        for u, v, w in edges:
            graph[u][v] = w

        pq = [(0, 0)] # minHeap of (dist, node) dist is the key for ordering.
        dist = [float('inf')] * N
        dist[0] = 0

        while pq:
            d, node = heapq.heappop(pq)
            # Each node is only visited once.
            if d > dist[node]: continue

            for nei, weight in graph[node].iteritems():
                # d2 is the total distance to reach 'nei' (neighbor) node.
                d2 = d + weight
                if d2 < dist[nei]:
                    heapq.heappush(pq, (d2, nei)) # smaller dist goes to front
                    dist[nei] = d2

        print dist
        return

Solution().dijkstra_DG([(0,1,4), (0,2,2), (1,2,3), (1,3,2), (1,4,3), (2,1,1), (2,3,4), (2,4,5), (4,3,1)], 5)
'''
result: dist = [0,3,2,5,6]
       0
      / \
     1 = 2
     | X |
     3 - 4
'''

