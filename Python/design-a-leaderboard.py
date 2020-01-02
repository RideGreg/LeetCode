# Time:  ctor:  O(1)
#        add:   O(1)
#        top:   O(n)
#        reset: O(1)
# Space: O(n)

# 1244 biweekly contest 12 11/2/2019
#
# Design a Leaderboard class, which has 3 functions:
#
# 1. addScore(playerId, score): Update the leaderboard by adding score to the given player's score.
#    If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
# 2. top(K): Return the score sum of the top K players.
# 3. reset(playerId): Reset the score of the player with the given id to 0. It is guaranteed that the player
#    was added to the leaderboard before calling this function.
#
# Initially, the leaderboard is empty.

# Constraints:
# 1 <= playerId, K <= 10000
# It's guaranteed that K is less than or equal to the current number of players.
# 1 <= score <= 100
# There will be at most 1000 function calls.

import collections
import random

# fast write, slow read <- usually write is more than read
class Leaderboard(object):
    def __init__(self):
        self.__lookup = collections.Counter()
        
    def addScore(self, playerId: int, score: int) -> None:
        self.__lookup[playerId] += score

    # not need full sort, just quick sort top k O(n)
    def top(self, K: int) -> int:
        def kthElement(nums, k, compare):
            def PartitionAroundPivot(left, right, pivot_idx, nums, compare):
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in range(left, right):
                    if compare(nums[i], nums[right]):
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == k:
                    return
                elif new_pivot_idx > k:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k.
                    left = new_pivot_idx + 1
        
        scores = list(self.__lookup.values())
        kthElement(scores, K, lambda a, b: a > b)
        return sum(scores[:K])

    def reset(self, playerId: int) -> None:
        self.__lookup[playerId] = 0


# slow write, fast read
# maintain top K in a list is expensive for writing
class Leaderboard_ming:
    def __init__(self): # O(1)
        self.scores = [0] * 10001
        self.top = []

    def addScore(self, playerId: int, score: int) -> None: # O(n)
        import bisect
        s = self.scores[playerId]
        if s:
            pos = bisect.bisect_left(self.top, s) # faster than list.remove()
            self.top.pop(pos)
        self.scores[playerId] += score
        bisect.insort_left(self.top, self.scores[playerId]) # this is expensive O(n)

    def top(self, K: int) -> int: # O(k)
        return sum(self.top[-K:])

    def reset(self, playerId: int) -> None: # O(n)
        import bisect
        s = self.scores[playerId]
        if s:
            pos = bisect.bisect_left(self.top, s)
            self.top.pop(pos)  # this is expensive O(n)
        self.scores[playerId] = 0

leaderboard = Leaderboard()
leaderboard.addScore(1,73)   # leaderboard = [[1,73]];
leaderboard.addScore(2,56)   # leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39)   # leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51)   # leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4)    # leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
print(leaderboard.top(1))    # returns 73;
leaderboard.reset(1)         # leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2)         # leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51)   # leaderboard = [[2,51],[3,39],[4,51],[5,4]];
print(leaderboard.top(3))    # returns 141 = 51 + 51 + 39;