# Time:  O(t + n)
# Space: O(n)

# 997
# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people
# is secretly the town judge.
#
# If the town judge exists, then:
# - The town judge trusts nobody.
# - Everybody (except for the town judge) trusts the town judge.
# - There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing that the person
# labelled a trusts the person labelled b.
#
# If the town judge exists and can be identified, return it.  Otherwise, return -1.

# Note:
# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N


# Solution: Directed Graph
# Consider trust as a graph, all pairs are directed edge.
# The point with in-degree - out-degree = N - 1 become the judge.

class Solution(object):
    def findJudge(self, N, trust): # USE THIS: excellent
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        degrees = [0] * (N + 1)
        for i, j in trust:
            degrees[i] -= 1
            degrees[j] += 1
        for i in xrange(1, N+1):
            if degrees[i] == N-1:
                return i
        return -1

    def findJudge_ming(self, N, trust): # double the space consumption
        import collections
        fro, to = collections.defaultdict(list), collections.defaultdict(list)
        for a, b in trust:
            fro[a].append(b)
            to[b].append(a)
        for i in xrange(1, N+1):
            if not fro[i] and len(to[i]) == N-1:
                return i
        return -1