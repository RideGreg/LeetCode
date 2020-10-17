# Time:  O(n)
# Space: O(n)

# 834
# An undirected, connected tree with N nodes
# labelled 0...N-1 and N-1 edges are given.
#
# The ith edge connects nodes edges[i][0] and edges[i][1] together.
#
# Return a list ans, where ans[i] is the sum of the distances
# between node i and all other nodes.
#
# Example 1:
#
# Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation:
# Here is a diagram of the given tree:
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
# Note: 1 <= N <= 10000

import collections


class Solution(object):

    # Tree Dynamic Programming
    # 首先考虑一个节点的情况，即指定一棵树，以root 为根，问节点root 与其他所有节点的距离之和。
    # 很容易想到一个树形动态规划：定义 dp[u] 表示以 u为根的子树，它的所有子节点到它的距离之和，同时定义 sz[u]
    # 表示以 u 为根的子树的节点数量，不难得出如下的转移方程：dp[u] = sum(dp[v] + sz[v]) where v is all children
    # nodes of u. 转移方程的含义就是考虑每个后代节点 v，已知 v的所有子节点到它的距离之和为 dp[v]，这些节点到 u的
    # 距离之和还要考虑 u→v 这条边的贡献。这条边长度为 1，一共有 sz[v] 个节点到节点 u 的距离会包含这条边，因此贡献为sz[v]。
    # Bottom up 遍历整棵树向上递推到根节点 root 即能得出最后的答案为 dp[root]。
    #
    # 本题要求的其实是上题的扩展，即要求每个节点为根节点的时候，它与其他所有节点的距离之和。暴力的角度我们可以对每个节点
    # 都做一次如上的树形动态规划，这样时间复杂度即为 O(N^2)
    #
    # 更优雅的方法是利用第一次树形动态规划的已有信息来优化时间复杂度。假设 u的某个后代节点为 v，如果要算 v的答案，本来我们
    # 要以 v为根来进行一次树形动态规划。但是利用已有信息，我们可以考虑树的形态做一次改变(换根)，让 v换到根的位置，
    # u变为其孩子节点，同时维护原有的 dp 信息。一次「换根」操作需要O(1)时间；不断换根，O(n)时间内可求出每个节点为根的答案，
    # 实现了时间复杂度的优化。

    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # dfs: bottom up
        # complete 'count' array; 'result' array only has root node completed, all leaf nodes has count 1 and result 0
        # Param 'parent' is a lightweight way in simple graph (no circle) to avoid visiting repeated nodes.
        def dfs(node, parent):
            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node)
                    count[node] += count[nei]
                    result[node] += result[nei]+count[nei]

        # dfs2: top down
        # get 'result' for all non-root nodes: break tree into 2 parts at nei-node edge,
        # the 'result' = result[node] - (# of nodes in subtree rooted at nei) + (# of nodes in the other part)
        def dfs2(node, parent):
            for nei in graph[node]:
                if nei != parent:
                    result[nei] = result[node] - count[nei] + (N -count[nei])
                    dfs2(nei, node)

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * N # number of nodes in the subtree rooted at this node (including this node)
        result = [0] * N # distance to all children nodes

        dfs(0, None)
        dfs2(0, None)
        return result


    # TLE O(n^2), dfs from each node O(n), and each dfs traverses all edges taking O(n)
    def sumOfDistancesInTree_ming(self, N, edges):
        def dfs(i, d, src):
            for nei in graph[i]:
                if nei not in visited:
                    visited.add(nei)
                    dis[src][nei] = dis[nei][src] = 1+d
                    dfs(nei, 1+d, src)

        dis = [[0]*N for _ in range(N)]
        graph = collections.defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        for i in range(N):
            visited = {i}
            dfs(i, 0, i)
        return [sum(dis[i]) for i in range(N)]

print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]])) # [8,12,6,10,10,10]
# after dfs: count = [6,1,4,1,1,1] which is completed,
#           result = [8, 0,3,0,0,0] only has root node done
# dfs2: get 'result' for all non-root nodes.