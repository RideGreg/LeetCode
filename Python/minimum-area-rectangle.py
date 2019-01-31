# Time:  O(n^1.5) on average
#        O(n^2) on worst
# Space: O(n)

# 939
# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
# with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.

# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct

import collections

class Solution(object):
    # Find all horizontal segments (pair of points). Group by vector (a complex number).
    # USE THIS: only this solution can extend to solve non-horizontal/vertical rectangular.
    def minAreaRect(self, points):
        import collections, itertools
        points.sort()
        points = [complex(*z) for z in points]
        lookup = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            if P.imag == Q.imag: # horizontal segment
                lookup[P - Q].append(P)

        ans = float('inf')
        for k, cands in lookup.iteritems():
            for U, V in itertools.combinations(cands, 2):
                if U.real == V.real:
                    ans = min(ans, abs(k) * abs(U - V))
        return int(ans) if ans < float('inf') else 0


class Solution3(object):
    # Sort by column (if columns more than rows) or row (if rows more than columns)
    # The time consuming part is double loop in each column (or row)

    # Count each rectangle by right-most (or top-most) edge.
    # Group the points by x coordinates, so that we have columns of points. Then, for every pair of points in a column
    # (with coordinates (x,y1) and (x,y2)), check for the smallest rectangle with this pair of points as the rightmost edge.
    # We can do this by keeping memory of what pairs of points we've seen before.
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lookup = {}
        result = float("inf")
        for x in sorted(p):
            p[x].sort()
            for j in xrange(len(p[x])):
                for i in xrange(j):
                    y1, y2 = p[x][i], p[x][j]
                    if (y1, y2) in lookup:
                        result = min(result, (x-lookup[y1, y2]) * abs(y2-y1))
                    lookup[y1, y2] = x
        return result if result != float("inf") else 0
 

# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    # Count by diagonal
    # Put all the points in a set. For each pair of points, if the associated rectangle are 4 distinct points
    # all in the set, then take the area of this rectangle as a candidate answer.
    def minAreaRect(self, points):
        lookup = set()
        result = float("inf")
        for x1, y1 in points:
            for x2, y2 in lookup:
                if (x1, y2) in lookup and (x2, y1) in lookup:
                    result = min(result, abs(x1-x2) * abs(y1-y2))
            lookup.add((x1, y1))
        return result if result != float("inf") else 0


print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]])) # 4