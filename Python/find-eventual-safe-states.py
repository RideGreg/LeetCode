# Time:  O(|V| + |E|)
# Space: O(|V|)

# In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.
# If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.
#
# Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.
# More specifically, there exists a natural number K so that for any choice of where to walk,
# we must have stopped at a terminal node in less than K steps.
#
# Which nodes are eventually safe?  Return them as an array in sorted order.
#
# The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.
# The graph is given in the following form: graph[i] is a list of labels j
# such that (i, j) is a directed edge of the graph.
#
# Example:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
#
# Note:
# - graph will have length at most 10000.
# - The number of edges in the graph will not exceed 32000.
# - Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].

import collections


class Solution(object):
    '''
    Time Complexity: O(N+E), where N is the number of nodes in the given graph, and E is the total number of edges.
    Space Complexity: O(N) in additional space complexity.

    Intuition
    The crux of the problem is whether you reach a cycle or not.
    Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually. This is a classic "white-gray-black"
    DFS algorithm that would be part of any textbook on DFS.
    https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/
    We mark a node gray on entry, and black on exit. If we see a gray node during our DFS, it must be part of a cycle.
    In a naive view, we'll clear the colors between each search.

    Algorithm
    We can improve this approach, by noticing that we don't need to clear the colors between each search.

    When we visit a node, the only possibilities are that we've marked the entire subtree black (which must be eventually safe),
    or it has a cycle and we have only marked the members of that cycle gray. So indeed, the invariant that gray nodes are always
    part of a cycle, and black nodes are always eventually safe is maintained.

    In order to exit search quickly when we find a cycle (and not paint other nodes erroneously), we'll say the result of
    visiting a node is true if it is eventually safe, otherwise false. This allows information that we reached a cycle
    to propagate up the call stack and terminate search early.
    '''
    def eventualSafeNodes_dfs(self, graph): # USE THIS
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        WHITE, GRAY, BLACK = 0, 1, 2

        def dfs(node):
            if lookup[node] != WHITE:
                return lookup[node] == BLACK

            lookup[node] = GRAY
            for child in graph[node]:
                if lookup[child] == GRAY or \
                    (lookup[child] == WHITE and not dfs(child)):
                    return False
            lookup[node] = BLACK
            return True

        lookup = collections.defaultdict(int)
        return filter(dfs, xrange(len(graph)))

    '''
    Intuition
    The crux of the problem is whether you can reach a cycle from the node you start in.
    Thinking about this property more, a node is eventually safe if all it's outgoing edges are to nodes that are eventually safe.

    This gives us the following idea: we start with nodes that have no outgoing edges - eventually safe. Now, we can update 
    any nodes which only point to eventually safe nodes - those are also eventually safe. Then, we can update again, and so on.
    However, we'll need a good algorithm to make sure our updates are efficient.

    Algorithm
    We'll keep track of graph, a way to know for some node i, what the outgoing edges (i, j) are. We'll also keep track of rgraph, 
    a way to know for some node j, what the incoming edges (i, j) are.

    For every node j which was declared eventually safe, we'll process them in a queue. We'll look at all parents i = rgraph[j] and 
    remove the edge (i, j) from the graph (from graph). If this causes the graph to have no outgoing edges graph[i], 
    then we'll declare it eventually safe and add it to our queue.
    '''
    def eventualSafeNodes_reverseEdge(self, graph):
        N = len(graph)
        safe = [False] * N

        graph = map(set, graph)
        rgraph = [set() for _ in xrange(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, v in enumerate(safe) if v]
