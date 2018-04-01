class Solution(object):
    def allPathsSourceTarget(self, graph):
        self.ans = []
        self.N = len(graph)
        def dfs(graph, used, cur):
            if cur[-1] == self.N-1:
                self.ans.append(list(cur))
                return

            for j in graph[cur[-1]]:
                if j not in used:
                    cur.append(j)
                    used.append(j)
                    dfs(graph, used, cur)
                    used.pop()
                    cur.pop()

        used, cur = [0], [0]
        dfs(graph, used, cur)
        return self.ans

print Solution().allPathsSourceTarget([[1,2], [3], [3], []])
