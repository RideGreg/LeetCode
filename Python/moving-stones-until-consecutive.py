# Time:  O(1)
# Space: O(1)

# 1033
# Three stones are on a number line at positions a, b, and c.
#
# Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone),
# and move it to an unoccupied position between those endpoints.  Formally, let's say the stones are
# currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z,
# and move that stone to an integer position k, with x < k < z and k != y.
#
# The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.
#
# When the game ends, what is the minimum and maximum number of moves that you could have made?
# Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x, y, z = sorted((a, b, c))
        mx = z - x - 2
        if x + 1 == y and y + 1 == z:
            mn = 0
        # 1 2 10 or 1 3 10
        elif (x + 1 == y or y + 1 == z) or (x + 2 == y or y + 2 == z):
            mn = 1
        else:
            mn = 2
        return [mn, mx]
