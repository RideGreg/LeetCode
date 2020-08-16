# Time:  O(nlogn)
# Space: O(1)

# There are a number of spherical balloons spread in two-dimensional space.
# For each balloon, provided input is the start and end coordinates of the horizontal diameter.
# Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and
# end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.
#
# An arrow can be shot up exactly vertically from different points along the x-axis.
# A balloon with xstart and xend bursts by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot.
# An arrow once shot keeps travelling up infinitely.
# The problem is to find the minimum number of arrows that must be shot to burst all balloons.
#
# Example:
#
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
#
# Output:
# 2
#
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6])
# and another arrow at x = 11 (bursting the other two balloons).

class Solution(object):
    def findMinArrowShots(self, points): # USE THIS: sort by end
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points.sort(key=lambda x: x[1])
        arrow = 1
        end = points[0][1]
        for x, y in points:
            if x > end:
                arrow += 1
                end = y
        return arrow


    def findMinArrowShots2(self, points): # sort by start
        if not points: return 0
        points.sort()
        ans, end = 1, points[0][1]
        for x, y in points[1:]:
            if x > end:
                ans += 1  # need a new arrow
                end = y
            else:
                end = min(end, y)  # keep smaller interval
        return ans


    def findMinArrowShots_kamyu(self, points):
        if not points:
            return 0

        points.sort()

        result = 0
        i = 0
        while i < len(points):
            j = i + 1
            right_bound = points[i][1]
            while j < len(points) and points[j][0] <= right_bound:
                right_bound = min(right_bound, points[j][1])
                j += 1
            result += 1
            i = j
        return result
