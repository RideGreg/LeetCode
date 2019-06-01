# Time:  O(nlogn), quick sorting O(NlogN), time of sliding window O(N)
# Space: O(1)

# 1040
# On an infinite number line, the position of the i-th stone is given by stones[i].  Call a stone an endpoint stone
# if it has the smallest or largest position.
#
# Each turn, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.
#
# Say stones = [1,2,5], you cannot move the endpoint stone at position 5, since moving it to any position (such as 0, or 3)
# will still keep that stone as an endpoint stone.
#
# The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.
#
# When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer
# as an length 2 array: answer = [minimum_moves, maximum_moves]


# Solution:
# in case of n stones, we need to find a consecutive n positions and move the stones in.
# This idea led the solution with sliding windows.
#
# Slide a window of size N, and find how many stones are already in this window.
# We want moves other stones into this window. For each missing stone, we need at least one move.
#
# Generally, the number of missing stones and the moves we need are the same.
# For case 1,2,4,5,10,
# 1 move needed from 10 to 3.

# Only one corner case in this problem, we need to move the endpoint to no endpoint.
# For case 1,2,3,4,10,
# 2 move needed from 1 to 6, then from 10 to 5.
#
#
# Upper Bound
# We try to move all stones to leftmost or rightmost.
# For example of to rightmost: we first move the A[0] to A[1] + 1 which needs one move
# and the leftmost position is now A[1].
# Then each time, we pick the stone of left endpoint, move it to the next empty position.
# During this process, the position of leftmost stones increment by 1 each time.
# Until the leftmost is at A[-1] - n + 1, which needs A[-1]-n+1 - A[1] move.
# So the total moves are A[-1]-n+2-A[1].
# Or, the upper bound is to fill in all empty slots between A[1] ~ A[n-1] or A[0] ~ A[n - 2].
#
class Solution(object):
    def numMovesStonesII(self, A):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        A.sort()
        i, n, low = 0, len(A), len(A)
        high = max(A[-1] - n + 2 - A[1], A[-2] - A[0] - n + 2)

        # size-n window sliding from left to right: maintain the left i and right j stones which inside window and
        # don't need to move. The # of stones between A[i] and A[j] inclusive are k = j-i+1. Remaining (n-k) stones
        # not in this window and should move into the n-k empty slots in the window, needs n-k move.
        for j in range(n):
            while A[j] - A[i] >= n: # guarantee left and right stones can be in a size-n window
                i += 1
            k = j - i + 1
            if k == n - 1 and A[j] - A[i] == n - 2: # k stones are consecutive and only 1 left, case (1, 2, 3, 4), 7
                low = min(low, 2)
            else:
                low = min(low, n - k)  # move remaining (n-k) stones not in this window
        return [low, high]

print(Solution().numMovesStonesII([7,4,9])) # [1,2]
print(Solution().numMovesStonesII([6,5,4,3,10])) # [2,3]
print(Solution().numMovesStonesII([100,101,104,102,103])) # [0,0]
