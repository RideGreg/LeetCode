class Solution:
    """
    @param x: The vertex of edge
    @param y: The another vertex of edge
    @param cost: The cost of edge
    @param profit: The profit of vertex
    @return: Return the max score
    """
    def getMaxScore(self, x, y, cost, profit):
        self.ans = float("-inf")
        import collections
        e, c = collections.defaultdict(list), collections.defaultdict(list)
        for i, cc in enumerate(cost):
            c[x[i]].append(cc)
            e[x[i]].append(y[i])

        def dfs(node, total):
            if node not in e:
                self.ans = max(self.ans, total)
                return

            for i, nNode in enumerate(e[node]):
                dfs(nNode, total + profit[nNode] - c[node][i])

        dfs(0, profit[0])
        return self.ans

print Solution().getMaxScore([0,0,0], [1,2,3], [1,1,1], [1,1,2,3]) #3
print Solution().getMaxScore([0,0,1,1,4], [1,2,3,4,5], [1,2,1,1,1], [1,2,5,6,1,10]) #11
print Solution().getMaxScore([0,0,1,1,4], [1,2,3,4,5], [1,2,1,1,10], [1,2,5,6,1,10]) #7
