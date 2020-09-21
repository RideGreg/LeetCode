# find shortest paths from a "source" node to all other nodes in a weighted directed graph,
# producing a shortest-path tree (a subset of edges of original tree).
# Also apply to undirected graph which is just a directed graph with bidirectional connections.
# BFS is actaully Dijkstra for unweighted graph (all weights are 1).

# https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e

import heapq

class Solution(object):
    # If graph nodes are labelled by a number, we can use list for best distance. List uses less space than dict.
    def dijkstra_listForDist(self, edges, N):
        graph = [{} for _ in range(N)]
        for u, v, w in edges:
            graph[u][v] = w

        dist = [float('inf')] * N
        dist[0] = 0

        pq = [(0, 0)] # minHeap of (dist, node) dist is the key for ordering.
        while pq:
            d, node = heapq.heappop(pq)
            # If dest is given, can return here because this is guaranteed the min distance to dest
            # if node == dest: return d

            # filter out duplicate path to a node. Each node is only visited once which path has min distance.
            # Note shouldn't skip for d==dist[node], because the path w/ same dist may not visited yet.
            if d > dist[node]: continue

            for nei, weight in graph[node].items():
                # d2 is the total distance to reach 'nei' (neighbor) node.
                d2 = d + weight
                if d2 < dist[nei]:
                    heapq.heappush(pq, (d2, nei)) # smaller dist goes to front
                    dist[nei] = d2

        print(dist)
        return

    # Very useful for graph where nodes are not labelled by a number. Refer to LC864 shortest-path-to-get-all-keys.py
    def dijkstra_dictForDist(self, edges, N):
        graph = [{} for _ in range(N)]
        for u, v, w in edges:
            graph[u][v] = w

        dist = {}

        pq = [(0, 0)] # minHeap of (dist, node) dist is the key for ordering.
        while pq:
            d, node = heapq.heappop(pq)
            # If dest is given, can return here because this is guaranteed the min distance to dest
            # if node == dest: return d

            # filter out duplicate path to a node. Each node is only visited once which path has min distance.
            if node in dist: continue
            dist[node] = d

            for nei, weight in graph[node].items():
                if nei not in dist:
                    heapq.heappush(pq, (d + weight, nei)) # smaller dist goes to front

        print(dist)
        return

Solution().dijkstra2_DG([(0,1,4), (0,2,2), (1,2,3), (1,3,2), (1,4,3), (2,1,1), (2,3,4), (2,4,5), (4,3,1)], 5)
# dict implementation: {0: 0, 2: 2, 1: 3, 3: 5, 4: 6}
# list implementation: [0,3,2,5,6]
'''
result: dist = [0,3,2,5,6]
       0
      / \
     1 = 2
     | X |
     3 - 4
'''

