# Time:  O(k*r*c + |E|log|V|) = O(k*r*c + (k*|V|)*log|V|)
#                             = O(k*r*c + (k*(k*2^k))*log(k*2^k))
#                             = O(k*r*c + (k*(k*2^k))*(logk + k*log2))
#                             = O(k*r*c + (k*(k*2^k))*k)
#                             = O(k*r*c + k^3*2^k)
# k is the number of keys. 1st term is BFS, 2nd term is Dijkstra.
# To be accurate, V = (2k+1)*2^k (each vertex can be 1 of the at most 13 POI (6 keys, 6 locks, and start point)
# and at most 2^6 states of owned keys), and E = (2k+1) * V.
#
# Space: O(|V|) = O(k*2^k)

# We are given a 2-dimensional grid. "." is an empty cell,
# "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys,
# and ("A", "B", ...) are locks.
#
# We start at the starting point, and one move consists of walking one space
# in one of the 4 cardinal directions.  We cannot walk outside the grid,
# or walk into a wall.  If we walk over a key, we pick it up.
# We can't walk over a lock unless we have the corresponding key.
#
# For some 1 <= K <= 6, there is exactly one lowercase and one uppercase
# letter of the first K letters of the English alphabet in the grid.
# This means that there is exactly one key for each lock, and one lock for
# each key;
# and also that the letters used to represent the keys and locks were chosen
# in the same order as the English alphabet.
#
# Return the lowest number of moves to acquire all keys.  If it's impossible,
# return -1.
#
# Example 1:
#
# Input: ["@.a.#","###.#","b.A.B"]
# Output: 8
# Example 2:
#
# Input: ["@..aA","..B#.","....b"]
# Output: 6
#
# Note:
# - 1 <= grid.length <= 30
# - 1 <= grid[0].length <= 30
# - grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
# - The number of keys is in [1, 6].  Each key has a different letter and
#   opens exactly one lock.

import collections
import heapq

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        # Points of Interest + Dijkstra
        #
        # We only care about walking between POI: the keys, locks, and starting position. This can speed up our calculation.
        # Use BFS to calculate the distance between any two POI (primitive segment, i.e. no POI between). Then we have a graph
        # (where each node refers to at most 13 places, and at most 2^6 states of keys). We have a starting node (at '@' with no keys)
        # and ending nodes (at anywhere with all keys.) We also know all the costs to go from one node to another -
        # each node has outdegree at most 13. This shortest path problem is now ideal for using Dijkstra's algorithm.
        #
        # Dijkstra's algorithm uses a priority queue to continually searches the path with the lowest cost to destination,
        # so that when we reach the target, we know it must have been through the lowest cost path.

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def bfs(source):
            r, c = locations[source]
            lookup = {(r,c)}
            q = collections.deque([(r, c, 0)])
            dist = {}
            while q:
                r, c, d = q.popleft()
                if source != grid[r][c] and grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue # Stop walking from here if we reach a point of interest
                for dr, dc in directions:
                    cr, cc = r+dr, c+dc
                    if (0 <= cr < len(grid)) and (0 <= cc < len(grid[cr])) and \
                        grid[cr][cc] != '#' and (cr,cc) not in lookup:
                        lookup.add((cr,cc))
                        q.append((cr, cc, d+1))
            return dist

        # The points of interest
        locations = {place: (r, c)
                     for r, row in enumerate(grid)
                     for c, place in enumerate(row)
                     if place not in '.#'}
        # The distance from source to each point of interest
        graph = {place: bfs(place) for place in locations}

        # Dijkstra's algorithm
        min_heap = [(0, '@', 0)]  # distance, place, state
        best = collections.defaultdict(lambda: float("inf"))
        best['@', 0] = 0
        target_state = 2**sum(place.islower() for place in locations)-1 # all keys obtained
        while min_heap:
            cur_d, place, state = heapq.heappop(min_heap)
            if state == target_state:
                return cur_d

            if best[place, state] < cur_d:
                continue

            for dest, d in graph[place].iteritems():
                next_state = state
                if dest.islower(): #key
                    next_state |= (1 << (ord(dest)-ord('a')))
                elif dest.isupper(): #lock
                    if not (state & (1 << (ord(dest)-ord('A')))): #no key
                        continue
                if cur_d+d < best[dest, next_state]: # ok to go back to a visited cell as long as state is different
                    best[dest, next_state] = cur_d+d
                    heapq.heappush(min_heap, (cur_d+d, dest, next_state))
        return -1


    # Brute Force + Permutations
    # Time: O(r*c*k*k!), where r,c are the dimensions of the grid, k is the maximum # of keys. Each BFS is performed up to k*k! times.
    # Space: O(r*c + k!), the space for the bfs and to store the candidate key permutations.
    #
    # Intuition and Algorithm
    # We have to pick up the keys K in some order. For each step in each ordering, do a BFS to find the distance to the next key.
    # E.g, if the keys are 'abcdef', then for a ordering such as 'bafedc', we calculate the candidate distance from '@' -> 'b' -> 'a' -> 'f' -> 'e' -> 'd' -> 'c'.
    #
    # Between each segment of our path (and corresponding BFS), remember what keys we've owned, that helps us identify what locks we are allowed to walk through.
    #
    def shortestPathAllKeys_bruteForcePermutations(self, grid):
        import itertools
        R, C = len(grid), len(grid[0])
        # location['a'] = the coordinates of 'a' on the grid, etc. location contains # of keys, # of locks, and @.
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}
        keys = "".join(chr(ord('a') + i) for i in xrange(len(location) / 2))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ans = R * C + 1

        def bfs(source, target, keys):
            sr, sc = location[source]
            tr, tc = location[target]
            seen = [[False] * C for _ in xrange(R)]
            seen[sr][sc] = True
            queue = collections.deque([(sr, sc, 0)])
            while queue:
                r, c, d = queue.popleft()
                if r == tr and c == tc: return d
                for dx, dy in directions:
                    cr, cc = r + dx, c + dy
                    if 0<=cr<R and 0<=cc<C and not seen[cr][cc] and grid[cr][cc] != '#':
                        if grid[cr][cc].isupper() and grid[cr][cc].lower() not in keys:
                            continue
                        queue.append((cr,cc,d+1))
                        seen[cr][cc] = True
            return float('inf')

        for cand in itertools.permutations(keys):
            # bns : the built candidate answer, consisting of the sum
            # of distances of the segments from '@' to cand[0] to cand[1] etc.
            bns = 0
            for i, target in enumerate(cand):
                source = cand[i-1] if i > 0 else '@'
                d = bfs(source, target, cand[:i])
                bns += d
                if bns >= ans: break
            else:
                ans = bns

        return ans if ans < R * C + 1 else -1

print(Solution().shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))
# dists = {'a': {'A':4, '@':2, 'B':4}, #no direct access to 'b'
#          '@': {'a':2},
#          'B': {'a':4, 'A':2},
#          'b': {'A':2},
#          'A': {'a':4, 'b':2, 'B':2}}
#
# Generate a weighted, undirected graph:
#     2
#   @ - a
#     4/ \4
# b - A - B
#   2   2

print(Solution().shortestPathAllKeys(["@..aA","..B#.","....b"]))