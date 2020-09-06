# Time:  O(|V| + |E|) 遍历一个图需要访问所有节点和所有临边
# Space: O(|E|)
# 207
# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0
# you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
#  is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1
# you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have
# finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# There are several ways to represent a graph. For example, the input prerequisites is a graph represented by
#  a list of edges. Is this graph representation appropriate?
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts
#  of Topological Sort.
# Topological sort could also be done via BFS.
#

# 通过 拓扑排序 判断此课程安排图是否是 有向无环图(DAG) 。 拓扑排序原理： 对 DAG 的顶点进行排序，
# 使得对每一条有向边 (u, v)，均有 u（在排序记录中）比 v 先出现。
#
# 通过课程前置条件列表 prerequisites 可以得到课程安排图的 邻接表 adjacency，以降低算法时间复杂度


import collections


# bfs solution
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 构建邻接表、和入度数组
        in_degree, graph = defaultdict(int), defaultdict(set)
        for c, pre in prerequisites:
            in_degree[c] += 1
            graph[pre].add(c)

        # 每次只能选 入度为 0 的课，因为它不依赖别的课
        # ok to use a stack/DFS instead of queue/BFS
        zero_in_degree_queue = deque([i for i in range(numCourses) if i not in in_degree])
        while zero_in_degree_queue:
            prerequisite = zero_in_degree_queue.popleft()
            numCourses -= 1
            for course in graph[prerequisite]:
                in_degree[course] -= 1 # 减小相关课的入度
                if in_degree[course] == 0:
                    zero_in_degree_queue.append(course)
        return numCourses == 0


    def findOrder_bfs2(self, numCourses, prerequisites):
        in_degree = collections.defaultdict(set)
        out_degree = collections.defaultdict(set)
        for i, j in prerequisites:
            in_degree[i].add(j)
            out_degree[j].add(i)
        q = collections.deque([i for i in xrange(numCourses) if i not in in_degree])
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for i in out_degree[node]:
                in_degree[i].remove(node)
                if not in_degree[i]:
                    q.append(i)
                    del in_degree[i]
            del out_degree[node]
        return result if not in_degree and not out_degree else []


# Time:  O(|V| + |E|)
# Space: O(|E|)
# dfs solution
class Solution2(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        in_degree = collections.defaultdict(set)
        out_degree = collections.defaultdict(set)
        for i, j in prerequisites:
            in_degree[i].add(j)
            out_degree[j].add(i)
        stk = [i for i in xrange(numCourses) if i not in in_degree]
        result = []
        while stk:
            node = stk.pop()
            result.append(node)
            for i in out_degree[node]:
                in_degree[i].remove(node)
                if not in_degree[i]:
                    stk.append(i)
                    del in_degree[i]
            del out_degree[node]
        return result if not in_degree and not out_degree else []


if __name__ == "__main__":
    print(Solution().canFinish(1, [])) # True
    print(Solution().canFinish(2, [[1, 0]])) # True
    print(Solution().canFinish(2, [[1, 0], [0, 1]])) # False
