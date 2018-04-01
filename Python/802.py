class Solution(object):
    def eventualSafeNodes(self, graph):
        path, checked, ans = set(), set(), set()

        def visit(vertex):
            if vertex in checked: return False
            checked.add(vertex)
            path.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour in path or visit(neighbour):
                    return True
            path.remove(vertex)
            ans.add(vertex)
            return False

        for v in xrange(len(graph)):
            if v not in checked and not visit(v):
                ans.add(v)

        return sorted(list(ans))

'''
Approach #1: Reverse Edges [Accepted]
Intuition

The crux of the problem is whether you can reach a cycle from the node you start in. If you can, then there is a way to avoid stopping indefinitely; and if you can't, then after some finite number of steps you'll stop.

Thinking about this property more, a node is eventually safe if all it's outgoing edges are to nodes that are eventually safe.

This gives us the following idea: we start with nodes that have no outgoing edges - those are eventually safe. Now, we can update any nodes which only point to eventually safe nodes - those are also eventually safe. Then, we can update again, and so on.

However, we'll need a good algorithm to make sure our updates are efficient.

Algorithm

We'll keep track of graph, a way to know for some node i, what the outgoing edges (i, j) are. We'll also keep track of rgraph, a way to know for some node j, what the incoming edges (i, j) are.

Now for every node j which was declared eventually safe, we'll process them in a queue. We'll look at all parents i = rgraph[j] and remove the edge (i, j) from the graph (from graph). If this causes the graph to have no outgoing edges graph[i], then we'll declare it eventually safe and add it to our queue.

Also, we'll keep track of everything we ever added to the queue, so we can read off the answer in sorted order later.

Complexity Analysis

Time Complexity: O(N+E), where N is the number of nodes in the given graph, and E is the total number of edges.

Space Complexity: O(N) in additional space complexity.

    def eventualSafeNodes(self, graph):
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
        
Approach #2: Depth-First Search [Accepted]
Intuition

As in Approach #1, the crux of the problem is whether you reach a cycle or not.

Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually. This is a classic "white-gray-black"
DFS algorithm that would be part of any textbook on DFS. We mark a node gray on entry, and black on exit. If we see a gray 
node during our DFS, it must be part of a cycle. In a naive view, we'll clear the colors between each search.

Algorithm

We can improve this approach, by noticing that we don't need to clear the colors between each search.

When we visit a node, the only possibilities are that we've marked the entire subtree black (which must be eventually safe), 
or it has a cycle and we have only marked the members of that cycle gray. So indeed, the invariant that gray nodes are 
always part of a cycle, and black nodes are always eventually safe is maintained.

In order to exit our search quickly when we find a cycle (and not paint other nodes erroneously), we'll say the result 
of visiting a node is true if it is eventually safe, otherwise false. This allows information that we've reached a cycle 
to propagate up the call stack so that we can terminate our search early.

Complexity Analysis

Time Complexity: O(N+E), where N is the number of nodes in the given graph, and E is the total number of edges.

Space Complexity: O(N) in additional space complexity.

    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != white:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))
'''

print Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])

