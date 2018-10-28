# Time:  O(p + r * n), p is the count of all the possible paths in graph (all paths are traversed),
#                      r is the count of the result (r results (each is up to n nodes) need to copy into return value).
# Space: O(n)

# Given a directed, acyclic graph of N nodes.
# Find all possible paths from node 0 to node N-1, and return them
# in any order.
#
# The graph is given as follows:  the nodes are 0, 1, ...,
# graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
#
# Example:
# Input: [[1,2], [3], [3], []]
# Output: [[0,1,3],[0,2,3]]
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#
# Note:
# - The number of nodes in the graph will be in the range [2, 15].
# - You can print different paths in any order, but you should keep
# the order of nodes inside one path.


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(path):
            if path[-1] == len(graph)-1:
                result.append(path[:])
                return
            for node in graph[path[-1]]:
                path.append(node)
                dfs(path)
                path.pop()

        result = []
        dfs([0])
        return result
