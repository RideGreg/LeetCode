# Time:  O(1)
# Space: O(1)

# 1025
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:
#
# - Choosing any x with 0 < x < N and N % x == 0.
# - Replacing the number N on the chalkboard with N - x.

# Also, if a player cannot make a move, they lose the game.
#
# Return True if and only if Alice wins the game, assuming both players play optimally.
#
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # 1. if we get an even, we can choose x = 1
        #    to make the opponent always get an odd
        # 2. if the opponent gets an odd, as no even number can be a factor of this odd,
        #    he can only choose x = 1 or other odds
        #    and we can still get an even
        # 3. at the end, the opponent can only choose x = 1 and we win
        # 4. in summary, we win if only if we get an even and 
        #    keeps even until the opponent loses
        return N % 2 == 0


# Time:  O(n^3/2)
# Space: O(n)
# cache solution
class Solution2(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        from functools import lru_cache

        @lru_cache(None)
        def helper(N):
            if N == 1: return False
            return any(not helper(N - x) for x in range(1, N // 2 + 1) if N % x == 0)

        return helper(N)

    def divisorGame_myCache(self, N):
        def memoization(N):
            if N == 1:
                return False

            if N not in cache:
                cache[N] = any(not memoization(N - x) for x in range(1, N // 2 + 1) if N % x == 0)
            return cache[N]

        cache = {}
        return memoization(N)
