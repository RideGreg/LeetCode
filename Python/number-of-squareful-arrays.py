# Time:  O(n!)
# Space: O(n^2)

# 996
# Given an array A of non-negative integers, the array is squareful if
# for every pair of adjacent elements, their sum is a perfect square.
#
# Return the number of permutations of A that are squareful.  Two permutations
# A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

# Input: [1,17,8]
# Output: 2
# Explanation: [1,8,17] and [17,8,1] are the valid permutations.

# Input: [2,2,2]
# Output: 1

import collections

from functools import lru_cache
import math

class Solution(object):
    # solution 1: backtracking
    #
    # Construct a graph where an edge from i to j exists if A[i]+A[j] is a perfect square.
    # Our goal is to investigate Hamiltonian paths of this graph: paths that visit
    # all the nodes exactly once.
    #
    # Let's keep a current 'count' of what values of nodes are left to visit, and a
    # 'todo' of how many nodes left to visit.
    #
    # From each node, we can explore all neighboring nodes (by value using a Counter,
    # which reduces the complexity blowup).
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def dfs(x, todo):
            if todo == 0:
                self.ans += 1
                return
            count[x] -= 1
            for y in graph[x]:
                if count[y]:
                    dfs(y, todo-1)
            count[x] += 1

        count = collections.Counter(A)
        graph = {i: [] for i in count}
        for i in count:
            for j in count:
                if int((i + j) ** 0.5 + 0.5) ** 2 == i + j:
                    graph[i].append(j)

        self.ans = 0
        for x in count:
            dfs(x, len(A)-1)
        return self.ans

    # solution 2: dynamic programming
    #
    # construct the graph in the same method as in Approach 1.
    #
    # Now, let dfs(node, visited) be the # of ways from node to visit the remaining
    # unvisited nodes. Here, visited is a mask: (visited >> i) & 1 is true if and only if
    # the ith node has been visited.
    #
    # Afterwards, we may have overcounted if there are repeated values in A. To account for
    # this, for every x in A, if A contains x a total of k times, we divide the answer by k!.
    def numSquarefulPerms_LeetcodeOfficial2(self, A):
        N = len(A)

        def edge(x, y):
            r = math.sqrt(x+y)
            return int(r + 0.5) ** 2 == x+y

        graph = [[] for _ in range(len(A))]
        for i, x in enumerate(A):
            for j in range(i):
                if edge(x, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # find num of hamiltonian paths in graph
        @lru_cache(None)
        def dfs(node, visited):
            if visited == (1 << N) - 1:
                return 1

            ans = 0
            for nei in graph[node]:
                if (visited >> nei) & 1 == 0:
                    ans += dfs(nei, visited | (1 << nei))
            return ans

        ans = sum(dfs(i, 1<<i) for i in range(N))
        count = collections.Counter(A)
        for v in count.values():
            ans //= math.factorial(v)
        return ans

print(Solution().numSquarefulPerms([1, 17, 8])) # 2 [1,8,17], [17, 8, 1]
print(Solution().numSquarefulPerms([2,2,2])) # 1