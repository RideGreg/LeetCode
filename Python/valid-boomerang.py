# Time:  O(1)
# Space: O(1)

# 1037
# A boomerang is a set of 3 points that are all distinct and not in a straight line.
# Given a list of three points in the plane, return whether these points are a boomerang.

class Solution(object):
    def isBoomerang(self, points): # USE THIS: slope
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        a,b,c = points
        return (a[0] - b[0]) * (a[1] - c[1]) !=  (a[0] - c[0]) * (a[1] - b[1])

    # triangle area ( a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]) ) // 2
    def isBoomerang(self, points):
        a,b,c = points
        return a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]) != 0
