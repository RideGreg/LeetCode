# Time:  O(m * n * sqrt(m * n))
# Space: O(m * n)

# the problem is the same as google codejam 2008 round 3 problem C
# https://github.com/kamyu104/GoogleCodeJam-2008/blob/master/Round%203/no_cheating.py

# 1349 weekly contest 175 2/8/2020

# Given a m * n matrix 'seats' that represent seats distributions in a classroom. If a seat is broken,
# it is denoted by '#' character otherwise it is denoted by a '.' character.
#
# Students can see the answers of those sitting next to the left, right, upper left and upper right,
# but he cannot see the answers of the student sitting directly in front or behind him. Return the
# maximum number of students that can take the exam together without any cheating being possible..
#
# Students must be placed in seats in good condition.

# 1 <= seats.length, seats[i].length <= 8

# Input: seats = [["#", ".", "#", "#", ".", "#"],
#                 [".", "#", "#", "#", "#", "."],
#                 ["#", ".", "#", "#", ".", "#"]]
# Output: 4 (put students in row 1 and row 3)

try:
    xrange
except NameError:
    xrange = range

import collections


# Time:  O(E * sqrt(V))
# Space: O(V)
# Source code from http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/
# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002
def bipartiteMatch(graph):
    '''Find maximum cardinality matching of a bipartite graph (U,V,E).
        The input format is a dictionary mapping members of U to a list
        of their neighbors in V.  The output is a triple (M,A,B) where M is a
        dictionary mapping members of V to their matches in U, A is the part
        of the maximum independent set in U, and B is the part of the MIS in V.
        The same object may occur in both U and V, and is treated as two
        distinct vertices if this happens.'''
    
    # initialize greedy matching (redundant, but faster than full search)
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break
    
    while 1:
        # structure residual graph into layers
        # pred[u] gives the neighbor in the previous layer for u in U
        # preds[v] gives a list of neighbors in the previous layer for v in V
        # unmatched gives a list of unmatched vertices in final layer of V,
        # and is also used as a flag value for pred[u] when u is in the first layer
        preds = {}
        unmatched = []
        pred = dict([(u,unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)
        
        # repeatedly extend layering structure by another pair of layers
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v,[]).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)
        
        # did we finish layering without finding any alternating paths?
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching,list(pred),list(unlayered))
        
        # recursively search backward through layers to find alternating paths
        # recursion returns true if found path, false otherwise
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0
        
        for v in unmatched: recurse(v)


# Hopcroft-Karp bipartite matching
class Solution3(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
        E, count = collections.defaultdict(list), 0
        for i in xrange(len(seats)):
            for j in xrange(len(seats[0])):
                if seats[i][j] != '.':
                    continue
                count += 1
                if j%2:
                    continue
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < len(seats) and \
                       0 <= nj < len(seats[0]) and \
                       seats[ni][nj] == '.':
                        E[i*len(seats[0])+j].append(ni*len(seats[0])+nj)
        return count-len(bipartiteMatch(E)[0])


# Time:  O(|V| * |E|) = O(m^2 * n^2)
# Space: O(|V| + |E|) = O(m * n)
# Hungarian bipartite matching

# The idea is that seats on even columns and seats on odd columns form a bipartite graph.
# Therefore, the maximum independent set on the bipartite graph is the solution.
#
# Solving such a problem with Hungarian is O(VE) where V is the number of vertices and
# E is the number of edges. In this problem, we have O(mn) nodes and O(mn) edges,
# where m and n are the dimensions of the input matrix.

# Similar problem: https://leetcode-cn.com/problems/broken-board-dominoes/
# https://ali-ibrahim137.github.io/competitive/programming/2020/01/02/maximum-independent-set-in-bipartite-graphs.html
# blog: https://www.renfei.org/blog/bipartite-matching.html
# 行列，棋盘，黑白染色，男女
# Seats in each set (odd rows and even rows form two sets of students) are never connected
# to another seat in the same set (means they can never spy each other) thus satisfies
# the definition of a bipartite graph. Students who can spy each other are connected
# through a virtual connection.

class Solution2(object):  # USE THIS
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        R, C = len(seats), len(seats[0])
        matching = [[-1] * C for _ in xrange(R)]
        # assume a virtual edge connecting students who can spy
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]

        def dfs(node, lookup):
            i, j = node
            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if 0 <= ni < R and 0 <= nj < C and \
                    seats[ni][nj] == '.' and not lookup[ni][nj]:
                    lookup[ni][nj] = True
                    if matching[ni][nj] == -1 or dfs(matching[ni][nj], lookup):
                        matching[ni][nj] = node
                        return True
            return False
        
        def Hungarian():
            result = 0
            for i in xrange(R):
                for j in xrange(0, C, 2):
                    if seats[i][j] == '.':
                        lookup = [[False]*C for _ in xrange(R)]
                        if dfs((i, j), lookup):
                            result += 1
            return result
          
        count = 0
        for i in xrange(R):
            for j in xrange(C):
                if seats[i][j] == '.':
                    count += 1
        return count-Hungarian()


# Time:  O(m * 2^n * 2^n) = O(m * 4^n)
# Space: O(2^n)
# bitmasking dp solution

# Bitmasking is related to bit and mask. For bit part, everything is encoded as a single bit,
# so the whole state is encoded as a group of bits (a binary number). For the mask part,
# we use 0/1 to represent the state of something. In most cases, 1 stands for the valid state
# while 0 stands for the invalid state.

# When doing Bitmasking DP, we are handling problems like "what is the ith bit in the state"
# or "what is the number of valid bits in a state":
#  - use (x >> i) & 1 or x & (1 << i) to get ith bit in state x.
#  - use (x & y) == x to check if x is a subset of y. This is useful when y is all the valid bits.
#  - use (x & (x >> 1)) == 0 to check if there are no adjancent valid states in x.

# In this problem, we use a bitmask of n bits to represent the validity of each row.
# dp{mask : v} is total number of seats taken when choosing mask for current row.

class Solution(object):  # OR USE THIS
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        # get the number of valid bits in a masking
        def bit_count(n):
            count = 0
            while n:
                n &= n - 1 # remove rightmost 1
                count += 1
            return count

        n = len(seats[0])
        dp = {0: 0} # dp[mask] = total # of seats taken
        for row in seats:
            invalid_mask = sum(1 << c for c in range(n) if row[c] == '#')
            new_dp = {}
            for mask1, v1 in dp.items():
                for mask2 in xrange(1<<n): # traverse all bits
                    if ((mask2 & invalid_mask) or
                        (mask2 & (mask2 >> 1)) or  # no left/right cheating
                        (mask2 & (mask1 << 1)) or (mask2 & (mask1 >> 1))): # no upper left/rigth cheating
                        continue
                    new_dp[mask2] = max(new_dp.get(mask2, 0), v1+bit_count(mask2))
            dp = new_dp
        return max(dp.values()) if dp else 0

print(Solution().maxStudents([
    ["#",".","#","#",".","#"],
    [".","#","#","#","#","."],
    ["#",".","#","#",".","#"]])) # 4 (row 1 and row 3)
print(Solution().maxStudents([
    [".","#"],
    ["#","#"],
    ["#","."],
    ["#","#"],
    [".","#"]])) # 3
print(Solution().maxStudents([
    ["#",".",".",".","#"],
    [".","#",".","#","."],
    [".",".","#",".","."],
    [".","#",".","#","."],
    ["#",".",".",".","#"]])) # 10 (col 1, 3, 5)