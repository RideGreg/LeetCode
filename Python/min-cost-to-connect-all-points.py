# Time:  O(n^2)
# Space: O(n)

# 1584
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
# where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one 
# simple path between any two points.

# Note: All pairs (xi, yi) are distinct.

# 最小生成树（MST），就是连接所有顶点的代价和最少的树，也就是所有边的长度/距离/权重和最小的树。两个常用算法:
# Prim算法(像Dijkstra)和Kruskal算法(像并查集)。

# Prim algorithm
# 此算法可以称为“加点法”，每次迭代选择代价最小的边对应的点，加入到最小生成树中。算法从某一个顶点s开始，
# 逐渐长大覆盖整个连通网的所有顶点。
# 1. 图的所有顶点集合为 V；初始令集合 u=s,v=V−u，可用一个lookup set控制;
# 2. 在两个集合 u,v 能够组成的边中，选择一条代价最小的边 (u_0,v_0)，加入到最小生成树中，并把 v_0并入到集合 u中。
# 3. 重复上述步骤，直到最小生成树有 n-1 条边或者 n 个顶点为止。

from typing import List
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result, u = 0, 0  # we can start from any node as u
        dist = [float("inf")]*len(points)
        lookup = set()
        for _ in range(len(points)-1): # connect the remaining n-1 nodes
            x0, y0 = points[u]
            lookup.add(u)
            for v, (x, y) in enumerate(points):
                if v not in lookup:
                    dist[v] = min(dist[v], abs(x-x0) + abs(y-y0))
            val, u = min((val, v) for v, val in enumerate(dist)) # 最小代价边
            dist[u] = float("inf")  # used
            result += val
        return result


    def minCostConnectPoints2(self, points: List[List[int]]) -> int: # Use queue/deque to implement MST
        from queue import PriorityQueue
        cal = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # 计算曼哈顿距离的函数

        pq = PriorityQueue()  # 来，复习一下优先队列的API | PS:要是卡常，就换成"配对堆"
        to_visit = set([i for i in range(len(points))])  # 待访问的节点集
        res = 0

        pq.put((0, 0))  # (distance, point_id)  # Prim算法从任何一个节点出发都是一样的，这里从0点开始
        while to_visit:  # 当没有访问完所有节点
            dis, now = pq.get()  # 获取优先队列中最小的项 => (到扩展集中某最近点的距离，某最近点的序号)
            if now in to_visit:  # 只做没访问过的
                to_visit.remove(now)  # 随手剪枝，移除出待访问的节点集
                res += dis
                for i in to_visit:  # 构建扩展集，就是把当前点对所有未访问点的距离都求一遍
                    # 以距离为cost丢进优先队列排序就好，想不清明白其它题解费劲构建边结构干啥...
                    pq.put((cal(points[now], points[i]), i))

        return res


# Time:  O(eloge) = O(n^2 * logn)
# Space: O(e) = O(n^2)

# kruskal's algorithm：similar to Union Find
# 此算法可以称为“加边法”，初始最小生成树边数为0，每迭代一次就选择一条满足条件的最小代价边，
# 加入到最小生成树的边集合里。
# 1. 把图中的所有边按代价从小到大排序；
# 2. 把图中的n个顶点看成独立的n棵树组成的森林；
# 3. 按权值从小到大选择边，所选的边连接的两个顶点 u_i, v_i应属于两颗不同的树（一棵树上的两条个顶点
# 相连的话就形成环了），则成为最小生成树的一条边，并将这两颗树合并作为一颗树。
# 4. 重复(3),直到所有顶点都在一颗树内或者有n-1条边为止。

class UnionFind(object):  # Time: (n * α(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = list(range(n))

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:  # union by rank
            self.set[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.set[y_root] = x_root
        else:
            self.set[y_root] = x_root
            self.rank[x_root] += 1
        return True


class Solution2(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        edges = []
        for u in range(len(points)):
            for v in range(u+1, len(points)):
                edges.append((u, v, abs(points[v][0]-points[u][0]) + abs(points[v][1]-points[u][1])))
        edges.sort(key=lambda x: x[2])
        result = 0
        union_find = UnionFind(len(points))
        for u, v, val in edges:
            if union_find.union_set(u, v):
                result += val
        return result

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # 20
print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]])) # 18
print(Solution().minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]])) # 4
print(Solution().minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]])) # 4000000
print(Solution().minCostConnectPoints([[0,0]])) # 0
