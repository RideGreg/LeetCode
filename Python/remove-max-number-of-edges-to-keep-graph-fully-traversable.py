# Time:  O(n + m * α(n)) ~= O(n + m)
# Space: O(n)

# 1579
# Alice and Bob have an undirected graph of n nodes and 3 types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can by traversed by both Alice and Bob.

# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of typei between 
# nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, 
# the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob 
# if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be 
# fully traversed by Alice and Bob.


# SOLUTION: 贪心+并查集。对Alice和Bob各自建立一个并查集。
#
# 首先判断Alice和Bob的是不是连通图，可以通过union所有的type 1和type 3之后，能否把Alice的并查集降到一个group
# (连通分量为1)来检查。这是比较常规的并查集用法。
#
# 问题为可以去除的边，这些边就是多余的(其形成回路)，即union() return False。这是高级的并查集用法。
#
# 直觉说优先保留公共边，这样能保证删除的边数量最多。详细证明为：
# 假设Alice和Bob都为连通图:
# 1.考虑单个用户，共有n个结点，产生连通图需要的最少边数为n-1,假设该用户可以访问的边有m条，那么多余的为m-(n-1)
# 2.现在考虑两个用户，结点为n个，两个用户各自可以通过的边数为p,q（不包含第三种类型的边）,第三种类型的边为K1条
# 假设最终的连通图对两个用户分别而言都是连通的，且对单个用户无回路，并且用了K2条第三种类型的边（无多余的，即这K2条
# 第三种类型的边不构成回路），有K2<=K1,则有：
#   a.对于第一个用户，多余的边为p-(n-1-K2),其中n-1-K2为，对于第一个用户，还需多少条只有第一个用户可以访问的边才能构成连通图
#   b.对于第二个用户，多余的边为q-(n-1-K2)，其中n-1-K2为，对于第二个用户，还需多少条只有第二个用户可以访问的边才能构成连通图
# 那么总的多余边(需删除的)为p-(n-1-K2) + q-(n-1-K2) + (K1-K2) = p+q-2n+2+K1+K2;
# 由于p,q,n,K1为定数，所以要想删除的边最多，那么必须要求最终的图中第三种类型的边K2最多，且无多余

# 因此，先添加第三种类型的边，从中去除多余的，然后再在剩下的各自可以访问的边中去除多余的

class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))
        self.count = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        self.count -= 1
        return True


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        redundant = 0
        union_find_a, union_find_b = UnionFind(n), UnionFind(n)

        for t, i, j in edges:
            if t == 3:
                a = union_find_a.union_set(i-1, j-1)
                b = union_find_b.union_set(i-1, j-1)
                if not a and not b:   # 无效边
                    redundant += 1

        for t, i, j in edges:
            if t == 1:
                if not union_find_a.union_set(i-1, j-1):   # 无效边
                    redundant += 1
            elif t == 2:
                if not union_find_b.union_set(i-1, j-1):   # 无效边
                    redundant += 1
        return redundant if union_find_a.count == union_find_b.count == 1 else -1


# 最小生成树 MST: 找出最少需用的边以满足完全遍历，利用并查集原理实现。
# 
# 反过来想，要想删除最多，必须保留最多公共边，各自的边需要保留最少。也就是剩余的边在保证连通的情况下尽可能选择公共边，那么可以
# 用Kruskal算法生成最小生成树。由于需要尽可能的保留公共边，在赋权时只需保证公共边的权小于各自的边权，同时各自的边权不同即可。
    def maxNumEdgesToRemove2(self, n, edges):
        e1 = []
        e2 = []
        for t, u, v in edges:
            if t == 1:
                e1.append((10, u, v))  # set weight as 10
            elif t == 2:
                e2.append((11, u, v))
            else:
                e1.append((1, u, v))
                e2.append((1, u, v))
        e1.sort()
        e2.sort()

        used1 = set()
        used2 = set()
        dic1 = {i:i for i in range(1,n+1)} # 构造并查集
        dic2 = {i:i for i in range(1,n+1)} 
        connected1 = set()
        connected2 = set()
        for edge in e1:
            _, start, end = edge
            while dic1[start] != start:
                start = dic1[start]
            while dic1[end] != end:
                end = dic1[end]
            if start != end:
                used1.add(edge)
                if start < end:
                    dic1[start] = end
                    dic1[edge[1]] = end # 路径压缩
                else:
                    dic1[end] = start
                    dic1[edge[2]] = start
                connected1.add(start)
                connected1.add(end)
            if len(used1) == n-1: # should enough to connect all nodes
                break
        if len(connected1) != n:
            return -1

        for edge in e2:
            _, start, end = edge
            while dic2[start] != start:
                start = dic2[start]
            while dic2[end] != end:
                end = dic2[end]
            if start != end:
                used2.add(edge)
                if start < end:
                    dic2[start] = end
                    dic2[edge[1]] = end # 路径压缩
                else:
                    dic2[end] = start
                    dic2[edge[2]] = start
                connected2.add(start)
                connected2.add(end)
            if len(used2) == n-1:
                break
        if len(connected2) != n:
            return -1

        used = used1 | used2
        return len(edges) - len(used)


# DFS: 复杂度O(N)，N为边数
# 首先dfs Alice 和 Bob，其中有一位不能dfs走完全部节点，则返回-1.
# 之后，清空数据，从1节点开始，dfs只走3类型的边，dfs完记录最多能访问多少个节点count。这些节点组成一个可用公共边互通的子集，
# 子集内遍历访问的边数就是count-1；
# 再找下一个未访问的节点，继续dfs，并继续形成子集，并把所有的子集边数相加为sumBian = sum(count[i] - 1);
# 这个sum则是Alice和Bob遍历中，能公用的最大边数。
# 则Alice和Bob 访问使用的边数量为： common = (n - 1) + (n - 1) - sum
# 最大可删除的边为： edges.length - common = edges.length - (n - 1) * 2 + sum.


print(Solution().maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])) # 2
print(Solution().maxNumEdgesToRemove(4, [[3,2,3],[1,1,2],[2,3,4]])) # -1