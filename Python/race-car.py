# Time : O(nlogn), n is the value of the target
# Space: O(n)

# 818
# Your car starts at position 0 and speed +1 on an infinite number line.
# (Your car can go into negative positions.)
#
# Your car drives automatically according to a sequence of
# instructions A (accelerate) and R (reverse).
#
# When you get an instruction "A", your car does the following:
# position += speed, speed *= 2.
#
# When you get an instruction "R", your car does the following:
# if your speed is positive then speed = -1 , otherwise speed = 1.
# (Your position stays the same.)
#
# For example, after commands "AAR", your car goes to
# positions 0->1->3->3, and your speed goes to 1->2->4->-1.
#
# Now for some target position, say the length of the shortest
# sequence of instructions to get there.
#
# Example 1:
# Input:
# target = 3
# Output: 2
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
# Example 2:
# Input:
# target = 6
# Output: 5
# Explanation:
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
#
# Note:
#  1 <= target <= 10000.


# Approach Framework
# Explanation
#
# Let A^k denote the command AAA⋯A (k times). Starting with an "R" command doesn't help, and the optimal sequence
# does not end on an "R". So let's suppose our command is always of the form A^{k_1} R A^{k_2} R ... A^{k_n}.
# Note that under such a command, the car will move to final position (2^{k_1} - 1) - (2^{k_2} - 1) + (2^{k_3} - 1) - ...
#
# A key claim is that k_i is bounded by a+1, where a is the smallest integer such that 2^a >= target.
# Basically, if you drive past the target, you don't need to keep driving. Because that must get erased
# by one or more negative terms later.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def racecar(self, target):
        dp = [0] * (target+1)
        for i in range(1, target+1):
            # 2^(k-1) <= i < 2^k
            k = i.bit_length()

            # case 1. drive exactly i at best
            #         seq(i) = A^k
            if i == 2**k-1:
                dp[i] = k
                continue

            # case 2. drive cross i at 2^k-1 with k steps A^k, and turn back to i
            #         seq(i) = A^k -> R -> seq(2^k-1 - i)
            dp[i] = k+1 + dp[2**k-1 - i]

            # case 3. drive less than i at 2^(k-1)-1 with k-1 steps A^(k-1), and
            #         turn back distance (2^j-1) with j steps A^j,
            #         and turn back again to make the direction is the same
            #         seq(i) = shortest(seq(i), A^(k-1) -> R -> A^j -> R ->
            #                                   seq(i - (2^(k-1)-1) + (2^j-1)),
            #                  where 0 <= j < k-1)
            #         => dp[i] = min(dp[i], (k-1) + 1 + j + 1 +
            #                               dp[i - (2**(k-1)-1) + (2**j-1)])
            for j in range(k-1):
                dp[i] = min(dp[i], k-1+j+2 + dp[i - (2**(k-1) - 2**j)])

        return dp[-1]

    # With some target, we have different moves we can perform (such as k_1 = 0, 1, 2, ...
    # using the notation from our Approach Framework), with different costs.
    #
    # This is an ideal setup for Dijkstra's algorithm, which finds the shortest cost path in a weighted graph.
    #
    # Algorithm
    # Dijkstra's algorithm uses a priority queue to continually searches the path with the lowest cost
    # to destination, so that when we reach the target, we know it must have been through the lowest cost path.
    #
    # Back to the problem, we have some barrier where we are guaranteed to never cross. We will also handle
    # negative targets; in total we will have 2 * barrier + 1 nodes.
    #
    # After, we could move walk = 2**k - 1 steps for a cost of k + 1 (the 1 is to reverse). If we reach our
    # destination exactly, we don't need the R, so it is just k steps.
    def racecar_dijkstra(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps: continue

            for k in xrange(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ: steps2 -= 1 #No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]

print(Solution().racecar(8)) # [0,1,4,2,5,7,5,3,6]