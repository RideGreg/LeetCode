# Time:  O(|V| + |E|)
# Space: O(|E|)

# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses
# you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible
# to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0.
# So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
# Another correct ordering is[0,2,1,3].
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
# Read more about how a graph is represented.
#
# Hints:
# This problem is equivalent to finding the topological order in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining
# the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.
#

from collections import defaultdict, deque

import collections


# bfs solution
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        in_degree, graph = defaultdict(int), defaultdict(set)
        for c, pre in prerequisites:
            in_degree[c] += 1
            graph[pre].add(c)

        # 每次只能选 入度为 0 的课，因为它不依赖别的课
        ans = []
        zero_in_degree_queue = deque([i for i in range(numCourses) if i not in in_degree])
        while zero_in_degree_queue:
            prerequisite = zero_in_degree_queue.popleft()
            ans.append(prerequisite)
            for course in graph[prerequisite]:
                in_degree[course] -= 1 # 减小相关课的入度
                if not in_degree[course]:
                    zero_in_degree_queue.append(course)
        return ans if len(ans) == numCourses else []


    def findOrder_bfs2(self, numCourses, prerequisites):
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        for i, j in prerequisites:
            indegree[i].add(j)
            outdegree[j].add(i)
        q = collections.deque([i for i in xrange(numCourses) if i not in indegree])
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for i in outdegree[node]:
                indegree[i].remove(node)
                if not indegree[i]:
                    q.append(i)
                    del indegree[i]
            del outdegree[node]
        return result if not indegree and not outdegree else []


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
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        for i, j in prerequisites:
            indegree[i].add(j)
            outdegree[j].add(i)
        stk = [i for i in xrange(numCourses) if i not in indegree]
        result = []
        while stk:
            node = stk.pop()
            result.append(node)
            for i in outdegree[node]:
                indegree[i].remove(node)
                if not indegree[i]:
                    stk.append(i)
                    del indegree[i]
            del outdegree[node]
        return result if not indegree and not outdegree else []

