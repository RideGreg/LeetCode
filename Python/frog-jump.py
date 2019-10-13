# Time:  O(n^2)
# Space: O(n^2)

# 403
# A frog is crossing a river. The river is divided into x units and
# at each unit there may or may not exist a stone.
# The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order,
# determine if the frog is able to cross the river by landing on the last stone.
# Initially, the frog is on the first stone and assume the first jump must be 1 unit.
#
# If the frog has just jumped k units, then its next jump must be
# either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
#
# Note:
#
# The number of stones is >= 2 and is < 1,100.
# Each stone's position will be a non-negative integer < 231.
# The first stone's position is always 0.
# Example 1:
#
# [0,1,3,5,6,8,12,17]
#
# There are a total of 8 stones.
# The first stone at the 0th unit, second stone at the 1st unit,
# third stone at the 3rd unit, and so on...
# The last stone at the 17th unit.
#
# Return true. The frog can jump to the last stone by jumping
# 1 unit to the 2nd stone, then 2 units to the 3rd stone, then
# 2 units to the 4th stone, then 3 units to the 6th stone,
# 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:
#
# [0,1,2,3,4,8,9,11]
#
# Return false. There is no way to jump to the last stone as
# the gap between the 5th and 6th stone is too large.

import collections


# DP with hash table
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False

        last_jump_units = collections.defaultdict(set) # {s: set() for s in stones}
        last_jump_units[1].add(1)
        for s in stones[:-1]:
            for oldJump in last_jump_units[s]:
                for newJump in (oldJump-1, oldJump, oldJump+1):
                    if newJump > 0 and s+newJump in last_jump_units:
                        last_jump_units[s+newJump].add(newJump)
        return bool(last_jump_units[stones[-1]])

    def canCross_bfs(self, stones):
        q = collections.deque()
        v = collections.defaultdict(lambda : collections.defaultdict(bool))
        stoneSet = set(stones)
        q.append((0, 0))
        v[0][0] = True
        while q:
            x, y = q.popleft()
            if x == stones[-1]: return True
            for z in (y - 1, y, y + 1):
                if z > 0 and not v[x + z][z] and x + z in stoneSet:
                    v[x + z][z] = True
                    q.append((x + z, z))
        return False
