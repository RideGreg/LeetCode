# Time:  O(nlogn)
# Space: O(n)

# 850
# We are given a list of (axis-aligned) rectangles.
# Each rectangle[i] = [x1, y1, x2, y2] ,
# where (x1, y1) are the coordinates of the bottom-left corner,
# and (x2, y2) are the coordinates of the top-right corner of
# the ith rectangle.
#
# Find the total area covered by all rectangles in the plane.
# Since the answer may be too large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
# Example 2:
#
# Input: [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7),
# which is (10^9)^2 = (-7)^2 = 49.
#
# Note:
# - 1 <= rectangles.length <= 200
# - rectanges[i].length = 4
# - 0 <= rectangles[i][j] <= 10^9
# - The total area covered by all rectangles will never exceed 2^63 - 1 and
#   thus will fit in a 64-bit signed integer.

# Segment Tree VERY HARD TO UNDERSTAND, NOT MY SEGMENT TREE FRAMEWORK
# As in solution below "Line Sweep", we want to support add(x1, x2), remove(x1, x2), and query(). This is
# the perfect setting for using a segment tree.
class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    def mid(self):
        return (self.start+self.end) // 2

    def left(self):
        self._left = self._left or SegmentTreeNode(self.start, self.mid())
        return self._left

    def right(self):
        self._right = self._right or SegmentTreeNode(self.mid(), self.end)
        return self._right

    def update(self, X, i, j, val):
        if i >= j:
            return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left().update(X, i, min(self.mid(), j), val)
            self.right().update(X, max(self.mid(), i), j, val)
        if self.count > 0:
            self.total = X[self.end]-X[self.start]
        else:
            self.total = self.left().total + self.right().total
        return self.total


class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        OPEN, CLOSE = 1, -1
        events = []
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()
        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        st = SegmentTreeNode(0, len(X)-1)
        result = 0
        cur_x_sum = 0
        cur_y = events[0][0]
        for y, typ, x1, x2 in events:
            result += cur_x_sum * (y-cur_y)
            cur_x_sum = st.update(X, Xi[x1], Xi[x2], typ)
            cur_y = y
        return result % (10**9+7)

# Line Sweep  线性扫描 USE THIS
# Time Complexity: O(N^2*logN), where N is the number of rectangles. In 2N events, sort active takes NLogN time.
# Space Complexity: O(N).

# Imagine we pass a horizontal line from bottom to top over the shape. We have some active intervals on this horizontal
# line, which gets updated twice for each rectangle. In total, there are 2 * N events, and we can update our
# (up to N) active horizontal intervals for each update.
#
# Algorithm
#
# For a rectangle like rec = [1,0,3,1], the first update is to add [1, 3] to the active set at y = 0, and the second
# update is to remove [1, 3] at y = 1. Note that adding and removing respects multiplicity - if we also added
# [0, 2] at y = 0, then removing [1, 3] at y = 1 will still leave us with [0, 2] active.
#
# This gives us a plan: create these two events for each rectangle, then process all the events in sorted order of
# y. The issue now is deciding how to process the events add(x1, x2) and remove(x1, x2) such that we are able to
# query() the total horizontal length of our active intervals.
#
# We can use the fact that our remove(...) operation will always be on an interval that was previously added.
# Let's store all the (x1, x2) intervals in sorted order. Then, we can query() in linear time using a technique
# similar to a classic LeetCode problem, Merge Intervals.
class Solution2(object):
    def rectangleArea(self, rectangles):
        def query():
            ans, cur = 0, float('-inf')
            for x1, x2 in active:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans

        # Populate events
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        ans, active = 0, []
        prev_y = events[0][0]
        for y, typ, x1, x2 in events:
            # For all vertical ground covered, update answer
            if y > prev_y:
                ans += query() * (y - prev_y)

            # Update active intervals
            if typ is OPEN:
                active.append((x1, x2))
                active.sort() # O(NlogN)
            else:
                active.remove((x1, x2))
            prev_y = y

        return ans % (10**9 + 7)


# Principle of Inclusion-Exclusion 容斥原理
# Time Complexity: O(N * 2^N), where N is the number of rectangles.
# Space Complexity: O(N).

# Say we have two rectangles, AA and BB. The area of their union is:
# |A union B| = |A| + |B| - |A intersect B|
#
# Say we have three rectangles, A, B, CA,B,C. The area of their union is:
# |A union B union C| = |A| + |B| +|C| - |A intersect B| - |A intersect C| - |B intersect C| + |A intersect B intersect C|
#
# From Rectangle Area I, we know that the intersection of any axis-aligned rectangles is another axis-aligned rectangle (or nothing).
# For every subset of {1,2,...N}, calculate their intersection of rectangles and its area. Then add (or subtract) to total.
class Solution3(object):
    def rectangleArea(self, rectangles):
        import itertools, functools
        def intersect(rec1, rec2):
            return [max(rec1[0], rec2[0]),
                    max(rec1[1], rec2[1]),
                    min(rec1[2], rec2[2]),
                    min(rec1[3], rec2[3])]

        def area(rec):
            dx = max(0, rec[2] - rec[0])
            dy = max(0, rec[3] - rec[1])
            return dx * dy

        ans = 0
        for size in range(1, len(rectangles) + 1):
            for group in itertools.combinations(rectangles, size):
                ans += (-1) ** (size + 1) * area(functools.reduce(intersect, group))

        return ans % (10**9 + 7)

print(Solution().rectangleArea([[0,0,4,4],[3,3,7,6],[1,5,2,6],[1,2,2,3],[4,5,5,7]])) # 29
# 7              __
# 6    __      _|_|__ __ __
# 5   |_|     | |_|       |
# 4  __ __ __ |__         |
# 3 |   __    |_| __ __ __|
# 2 |  |_|      |
# 1 |           |
# 0 |__ __ __ __|
print(Solution().rectangleArea([[0,0,4,2],[2,0,4,3],[2,0,5,1]])) # 11