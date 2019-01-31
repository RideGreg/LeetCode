# Time:  O(n * 3^(n/2))
# Space: O(3^(n/2))

# 956
# You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports,
# one on each side.  Each steel support must be an equal height.
#
# You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3,
# you can weld them together to make a support of length 6.
#
# Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.

# 0 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# The sum of rods is at most 5000.

import collections


# Meet in the Middle:
# Typically, the complexity of brute force can be reduced with a "meet in the middle" technique.
# As applied to this problem, we have 3^N possible states, from writing either +x, -x, or 0 for each rod x,
# i.e. x used in left support, right support or not use.

# Split the rods into two halves: left and right, each of them contains 3^{N/2} states separately. E.g. if we
# have rods [1, 3, 5, 7], then the first two rods create up to nine states: [0+0, 0+3, 0-3, 1+0, 1+3, 1-3, -1+0, -1+3, -1-3],
# and the last two rods also create nine states.
#
# Use brute force to compute all reachable states. Store each state as the sum of positive terms, and absolute values of
# the sum of negative terms. E.g., +1 +2 -3 -4 becomes (3, 7).

# DELTA and SCORE
# Let's also call the difference 3 - 7 to be the DELTA of this state, so this state has a DELTA of -4.
# The SCORE of a state will be the sum of the positive terms, and we want the highest SCORE for a DELTA.

# To have 2 equal height steel support means delta from left half and right half sum to 0.

class Solution(object):
    def tallestBillboard(self, rods): # LeetCode official
        def make(A):
            states = {(0, 0)}
            for x in A:
                states1 = {(a+x, b) for a,b in states}
                states2 = {(a, b+x) for a,b in states}
                states |= (states1 | states2)

            delta = {}
            for a, b in states:
                delta[a-b] = max(delta.get(a-b, 0), a)
            return delta

        N = len(rods)
        Ldelta = make(rods[:N/2])
        Rdelta = make(rods[N/2:])

        return max(Ldelta[d] + Rdelta[-d] for d in Ldelta if -d in Rdelta)

    def tallestBillboard_kamyu(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        def dp(A):
            lookup = collections.defaultdict(int)
            lookup[0] = 0
            for x in A:
                for d, y in lookup.items():
                    lookup[d+x] = max(lookup[d+x], y)
                    lookup[abs(d-x)] = max(lookup[abs(d-x)], y + min(d, x))
            return lookup

        left, right = dp(rods[:len(rods)//2]), dp(rods[len(rods)//2:])
        return max(left[d]+right[d]+d for d in left if d in right)

print(Solution().tallestBillboard([1,2,3,6])) # 6: {1,2,3} {6}
print(Solution().tallestBillboard([1,2,3,4,5,6])) # 10: {2,3,5} {4,6}
print(Solution().tallestBillboard([1,2])) # 0