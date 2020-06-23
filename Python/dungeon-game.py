# Time:  O(m * n)
# Space: O(m + n)
#
# 174
# The demons had captured the princess (P) and imprisoned her
# in the bottom-right corner of a dungeon. T
# he dungeon consists of M x N rooms laid out in a 2D grid.
# Our valiant knight (K) was initially positioned in the top-left room
# and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer.
# If at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons,
# so the knight loses health (negative integers) upon entering these rooms;
# other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible,
# the knight decides to move only rightward or downward in each step.
#
#
# Write a function to determine the knight's minimum initial health
# so that he is able to rescue the princess.
#
# For example, given the dungeon below, the initial health of
# the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
#
# Notes:
#
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters
# and the bottom-right room where the princess is imprisoned.
#

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer

    # At grid P, since "at any point his health point drops to 0 or below, he dies immediately", the remaining health value
    # should be at least 1, that is, start + dungeon >= 1, we have start = max(1, 1 - dungeon[i][j]). (Notice, at any grid,
    # the start health should be at least 1 (for example, test case [1,0,0] require start health 1 even though it has positive
    # remaining health at grid[0][1] and grid[0][2])
    # Similarly, to satisfy the start health of dungeon[i][j], the start health of dungeon[i-1][j] (or dungeon[i][j-1])
    # should be at least start[i-1][j] + dungeon[i-1][j] = start[i][j], that is, start[i-1][j] = start[i][j] - dungeon[i-1][j].
    # In addition, if grid[i][j] can go both grid[i+1][j] and grid[i][j+1] to P, we should choose a path with less start health
    # between grid[i+1][j] and grid[i][j+1] since it require less start health of grid[i][j].

    def calculateMinimumHP(self, dungeon): # USE THIS
        # dp[j] means minimum initial health required before entering this cell
        m, n = len(dungeon), len(dungeon[0])
        dp = [float("inf")] * n
        dp[-1] = 1

        for i in reversed(range(m)):
            dp[-1] = max(1, dp[-1] - dungeon[i][-1])
            for j in reversed(range(n - 1)):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])

        return dp[0]


class Solution_wrong:
    # this method doesn't work, go forward from top-left to bottom-right
    # two helper 2D arrays: _sum for total health travelled, pathMin for min start health needed on this path
    def calculateMinimumHP_wrong_attempt(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        _sum = [[0] * n for _ in range(2)]
        pathMin = [[0] * n for _ in range(2)]
        for j in range(n):
            _sum[0][j] = dungeon[0][j] + (_sum[0][j-1] if j > 0 else 0)
            pathMin[0][j] = min(_sum[0][j], pathMin[0][j-1] if j > 0 else float('inf'))

        for i in range(1, m):
            _sum[i%2][0] = dungeon[i][0] + _sum[(i-1)%2][0]
            pathMin[i%2][0] = min(_sum[i%2][0], pathMin[(i-1)%2][0])
            for j in range(1, n):
                # fail for [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
                # to reach dungeon[2][2], best is right->right->down->down, but
                # the algorithm previously set the best path to reach dungeon[1][2] is down->right->right
                fromUp = min(pathMin[(i-1)%2][j], _sum[(i-1)%2][j] + dungeon[i][j])
                fromLeft = min(pathMin[i%2][j - 1], _sum[i%2][j - 1] + dungeon[i][j])
                if fromUp > fromLeft:
                    pathMin[i % 2][j] = fromUp
                    _sum[i % 2][j] = _sum[(i - 1) % 2][j] + dungeon[i][j]
                else:
                    pathMin[i % 2][j] = fromLeft
                    _sum[i % 2][j] = _sum[i % 2][j - 1] + dungeon[i][j]

                ''' fail for [[1,-4,5,-99], [2,-2,-2,-1]]
                _sum[i%2][j] = max(_sum[(i-1)%2][j], _sum[i%2][j - 1]) + dungeon[i][j]
                pathMin[i%2][j] = max(min(pathMin[(i-1)%2][j], _sum[(i-1)%2][j] + dungeon[i][j]),
                                      min(pathMin[i%2][j - 1], _sum[i%2][j - 1] + dungeon[i][j]))
                '''
        return 1 - pathMin[(m-1)%2][-1] if pathMin[(m-1)%2][-1] <= 0 else 1


# Time:  O(m * n logk), where k is the possible maximum sum of loses
# Space: O(m + n)
class Solution2:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        maximum_loses = 0
        for rooms in dungeon:
            for room in rooms:
                if room < 0:
                    maximum_loses += abs(room)

        return self.binarySearch(dungeon, maximum_loses)

    def binarySearch(self, dungeon, maximum_loses):
        start, end = 1, maximum_loses + 1
        result = 0
        while start < end:
            mid = start + (end - start) / 2
            if self.DP(dungeon, mid):
                end = mid
            else:
                start = mid + 1
        return start

    def DP(self, dungeon, HP):
        remain_HP = [0 for _ in dungeon[0]]
        remain_HP[0] = HP + dungeon[0][0]
        for j in xrange(1, len(remain_HP)):
            if remain_HP[j - 1] > 0:
                remain_HP[j] = max(remain_HP[j - 1] + dungeon[0][j], 0)

        for i in xrange(1, len(dungeon)):
            if remain_HP[0] > 0:
                remain_HP[0] = max(remain_HP[0] + dungeon[i][0], 0)
            else:
                remain_HP[0] = 0

            for j in xrange(1, len(remain_HP)):
                remain = 0
                if remain_HP[j - 1] > 0:
                    remain = max(remain_HP[j - 1] + dungeon[i][j], remain)
                if remain_HP[j] > 0:
                    remain = max(remain_HP[j] + dungeon[i][j], remain)
                remain_HP[j] = remain

        return remain_HP[-1] > 0

if __name__ == "__main__":
    print(Solution().calculateMinimumHP([[1,-4,5,-99],
                                         [2,-2,-2,-1]]))  # 3
    print(Solution().calculateMinimumHP([[1, -3, 3],
                                         [0, -2, 0],
                                         [-3, -3, -3]]))  # 3

    dungeon = [[ -2,  -3,  3], \
               [ -5, -10,  1], \
               [ 10,  30, -5]]
    print(Solution().calculateMinimumHP(dungeon)) # 7

    dungeon = [[ -200]]
    print(Solution().calculateMinimumHP(dungeon)) # 201

    dungeon = [[0, -3]]
    print(Solution().calculateMinimumHP(dungeon)) # 4

    print(Solution().calculateMinimumHP([[200]])) # 1