# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

# 886
# Given a set of N people (numbered 1, 2, ..., N),
# we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people,
# and they should not go into the same group. 
#
# Formally, if dislikes[i] = [a, b],
# it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
# Example 1:
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
# Note:
# - 1 <= N <= 2000
# - 0 <= dislikes.length <= 10000
# - 1 <= dislikes[i][j] <= N
# - dislikes[i][0] < dislikes[i][1]
# - There does not exist i != j for which dislikes[i] == dislikes[j].

# Solution: Consider the graph on N people formed by the given "dislike" edges. We want to check that each
# connected component of this graph is bipartite. Either DFS or BFS to traverse the graph, check whether the graph
# is bipartite by trying to coloring nodes with two colors.

import collections


class Solution(object):
    def possibleBipartition(self, N, dislikes): # DFS, USE THIS
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        stk = []
        color = {}
        for node in xrange(1, N + 1):
            if node not in color:
                color[node] = 0
                stk.append(node)
                while stk:
                    cur = stk.pop()
                    for nei in graph[cur]:
                        if nei not in color:
                            color[nei] = 1 - color[cur]
                            stk.append(nei)
                        elif color[nei] == color[cur]:
                            return False
        return True

    def possibleBipartition_bfs(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        q = collections.deque([])
        color = {}
        for node in xrange(1, N+1):
            if node not in color:
                color[node] = 0
                q.append(node)
                while q:
                    cur = q.popleft()
                    for nei in graph[cur]:
                        if nei not in color:
                            color[nei] = 1-color[cur]
                            q.append(nei)
                        elif color[nei] == color[cur]:
                            return False
        return True
 
