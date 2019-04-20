# Time:  O(logY)
# Space: O(1)

# 991
# On a broken calculator that has a number showing on its display, we can perform two operations:
#
# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.

# Initially, the calculator is displaying the number X.
# Return the minimum number of operations needed to display the number Y.

# Solution: greedy algorithm

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        result = 0
        while X < Y:
            if Y%2:
                Y += 1
            else:
                Y /= 2
            result += 1
        return result + X-Y
