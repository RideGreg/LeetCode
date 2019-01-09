# Time:  O(n^2) ~ O(n^3)
# Space: O(n^2)

# 963
# Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points,
# with sides not necessarily parallel to the x and y axes.
# If there isn't any rectangle, return 0.

# Basic Idea: group points by some observations, check the points in the same group meets requirement.

# Learned: 1. use vector (a complex number) instead of slope+length.
# 2. To tell perpendicular, check dot product of 2 vectors equals to 0, instead compare slope (horizontal edge case).
# 3. Use itertools.combinations(list, repeat).
# 4. Use abs() < EPS (1e-7) to compare float numbers.

import collections
import itertools


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # use vector (combining slope and length) as key
        points.sort()
        points = [complex(*z) for z in points]
        lookup = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            lookup[P-Q].append((P+Q) / 2)
            # key(P-Q) is a vector. Append P+Q/2 is better than append P, no worry for order of points

        result = float("inf")
        for A, candidates in lookup.iteritems():
            for P, Q in itertools.combinations(candidates, 2):
                if A.real * (P-Q).real + A.imag * (P-Q).imag == 0.0:
                    result = min(result, abs(A) * abs(P-Q))
        return result if result < float("inf") else 0.0

    def minAreaFreeRect_slopeKey(self, points): # I did in contest, basically similar to grouping by vector.
        import collections
        lookup = collections.defaultdict(list)
        ans = float('inf')
        points.sort()
        for j, p2 in enumerate(points):
            for i in xrange(j):
                p1 = points[i]
                d2 = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
                if p2[0] == p1[0]:
                    r = 's'
                else:
                    r = float(p2[1] - p1[1]) / (p2[0] - p1[0])

                lookup[(r, d2)].append((p1, p2))

        for k, ps in lookup.iteritems():
            if len(ps) >= 2:
                for j, pair2 in enumerate(ps):
                    for i in xrange(j):
                        p1, p2 = pair2
                        p3, p4 = ps[i]
                        if p2 == p3 or p4 == p1: continue
                        flag = False
                        if k[0] == 0:
                            if p1[0]==p3[0] and p2[0]==p4[0]: flag = True
                        elif k[0]=='s':
                            if p1[1]==p3[1] and p2[1]==p4[1]: flag = True
                        else:
                             if p3[0] != p1[0] and abs(-1-float(p3[1] - p1[1]) / (p3[0] - p1[0]) * k[0]) < 1e-5: flag = True
                        if flag:
                            dd2 = (p3[0] - p1[0])**2 + (p3[1] - p1[1])**2
                            ans = min(ans, (k[1] * dd2)**0.5)
        return ans if ans < float('inf') else 0

    # Consider opposite points AC and BD of a rectangle ABCD. They both have the same center and same radius. A necessary
    # and sufficient condition to form a rectangle with 2 opposite pairs of points is that the points have the same center and radius.
    # For each pair of points, classify them by center and radius. Only need to record one point P, since the other point is P' = 2 * center - P
    # (using vector notation). For each center and radius, look at every possible rectangle (two pairs of points P, P', Q, Q').
    # The area of this rectangle dist(P, Q) * dist(P, Q') is a candidate answer.
    # Time: O(N^2logN). It can be shown that the number of pairs of points with the same classification is bounded by logN
    # Space: O(N)
    def minAreaFreeRect_iterateCenter(self, points):
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.iteritems():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))

        return ans if ans < float("inf") else 0

    # For each triangle, let's try to find the 4th point and whether it is a rectangle. The 4th point must be
    # p4 = p2 + p3 - p1 (using vector notation). The checking perpendicular using the dot product of the two vectors
    # (p2 - p1) and (p3 - p1). (Another way is we could normalize the vectors to length 1, and check that one equals the
    # other rotated by 90 degrees.)
    # Time: O(n^3), Space: O(n)
    def minAreaFreeRect_iterateTriangle(self, points):
        EPS = 1e-7
        points = set(map(tuple, points))

        ans = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            if p4 in points:
                v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
                v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
                if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
                    area = abs(v21) * abs(v31)
                    if area < ans:
                        ans = area

        return ans if ans < float('inf') else 0

print(Solution().minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]])) # 2.0
print(Solution().minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]])) # 1.0 from [1,0],[1,1],[2,1],[2,0]
print(Solution().minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]])) # 0
print(Solution().minAreaFreeRect([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]])) # 2.0 from [2,1],[2,3],[3,3],[3,1]