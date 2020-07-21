# Time:  O(|V| + |E|)
# Space: O(|E|)

# 1136
# There are N courses, labelled from 1 to N.
#
# We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and
# course Y: course X has to be studied before course Y.
#
# In one semester you can study any number of courses as long as you have studied all the prerequisites
# for the course you are studying.
#
# Return the minimum number of semesters needed to study all courses.  If there is no way to study
# all the courses, return -1.

# BFS, Topological sort

import collections
class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        g = collections.defaultdict(list)
        in_degree = [0]*N
        for x, y in relations:
            g[x-1].append(y-1)
            in_degree[y-1] += 1
        # course w/o prerequisite can be done in first level
        q = collections.deque([(1, i) for i in range(N) if not in_degree[i]])

        ans, count = 0, N
        while q:
            level, u = q.popleft()
            count -= 1
            ans = level
            for v in g[u]:
                in_degree[v] -= 1
                if not in_degree[v]:
                    q.append((level+1, v)) # course cleared w/ prerequisite can be done in next level
        return ans if count == 0 else -1

print(Solution().minimumSemesters(3, [[1,3], [2,3]]))
print(Solution().minimumSemesters(3, [[1,2], [2,3], [3,1]]))