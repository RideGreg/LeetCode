# Time:  O((|E| + |V|) * log|V|) = O(|E| * log|V|),
#        if we can further to use Fibonacci heap, it would be O(|E| + |V| * log|V|)
# Space: O(|E| + |V|) = O(|E|)

# Starting with an undirected graph (the "original graph")
# with nodes from 0 to N-1, subdivisions are made to some of the edges.
# The graph is given as follows: edges[k] is a list of integer pairs
# (i, j, n) such that (i, j) is an edge of the original graph,
#
# and n is the total number of new nodes on that edge. 
#
# Then, the edge (i, j) is deleted from the original graph,
# n new nodes (x_1, x_2, ..., x_n) are added to the original graph,
#
# and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j)
# are added to the original graph.
#
# Now, you start at node 0 from the original graph, and in each move,
# you travel along one edge. 
#
# Return how many nodes you can reach in at most M moves.
#
# Example 1:
#
# Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
# Output: 13
# Explanation: 
# The nodes that are reachable in the final graph after M = 6 moves are indicated below.
#
# Example 2:
#
# Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
# Output: 23
#
# Note:
# - 0 <= edges.length <= 10000
# - 0 <= edges[i][0] < edges[i][1] < N
# - There does not exist any i != j for which
#   edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
# - The original graph has no parallel edges.
# - 0 <= edges[i][2] <= 10000
# - 0 <= M <= 10^9
# - 1 <= N <= 3000

import collections
import heapq

class Solution(object):
    def reachableNodes(self, edges, M, N):  # USE THIS, more clear
        graph = [{} for _ in xrange(N)]
        for u, v, w in edges:
            graph[u][v] = [w, 0]  # (weight, used-nodes-on-this-directed-edge), regular Dijkstra only save w
            graph[v][u] = [w, 0]

        minHeap = [(0, 0)]
        dist = [M + 1] * N
        dist[0] = 0
        ans = 0

        while minHeap:
            d, node = heapq.heappop(minHeap)
            if d > dist[node]: continue

            ans += 1
            for nei, prop in graph[node].items():
                # M - d is how much further we can walk from this node, prop[0] is how many new nodes
                # there are on this edge. prop[1] is the maximum nodes we can use of this edge.
                prop[1] = min(prop[0], M - d)

                d2 = d + prop[0] + 1 # total distance to reach 'nei' node
                if d2 < dist[nei]:
                    heapq.heappush(minHeap, (d2, nei))
                    dist[nei] = d2

        for u, v, w in edges:
            ans += min(w, graph[u][v][1] + graph[v][u][1])

        return ans


    def reachableNodes_kamyu(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        adj = [[] for _ in xrange(N)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        min_heap = [(0, 0)]
        best = collections.defaultdict(lambda: float("inf"))
        best[0] = 0
        count = collections.defaultdict(lambda: collections.defaultdict(int))
        result = 0
        while min_heap:
            curr_total, u = heapq.heappop(min_heap)  # O(|V|*log|V|) in total
            if best[u] < curr_total:
                continue
            result += 1
            for v, w in adj[u]:
                count[u][v] = min(w, M-curr_total)
                next_total = curr_total+w+1
                if next_total <= M and next_total < best[v]:
                    best[v] = next_total
                    heapq.heappush(min_heap, (next_total, v))  # binary heap O(|E|*log|V|) in total
                                                               # Fibonacci heap O(|E|) in total
        for u, v, w in edges:
            result += min(w, count[u][v]+count[v][u])
        return result

print(Solution().reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3)) #13
print(Solution().reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4)) #23
print(Solution().reachableNodes([[1,2,5],[0,3,3],[1,3,2],[2,3,4],[0,4,1]], 7, 5)) #13
print(Solution().reachableNodes([[0,3,8],[0,1,4],[2,4,3],[1,2,0],[1,3,9],[0,4,7],[3,4,9],[1,4,4],[0,2,7],[2,3,1]], 8, 5)) #40
