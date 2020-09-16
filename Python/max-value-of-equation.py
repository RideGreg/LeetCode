# Time:  O(n)
# Space: O(n)

# 1499
# Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values,
# where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.
#
# Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.
# It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.
#
#
import collections


class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        ans, q = float('-inf'), collections.deque()
        for x, y in points:
            while q and x - q[0][0] > k:   # maintain distance k
                q.popleft()

            if q:
                ans = max(ans, y + q[0][1] + x - q[0][0])

            while q and y - q[-1][1] >= x - q[-1][0]:   # prune inferior data
                q.pop()
            q.append((x, y))
        return ans

print(Solution().findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]], 1)) # 4
print(Solution().findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3)) # 3