# Time:  O(nlogn)
# Space: O(n)

# 846
# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups
# so that each group is size W,
# and consists of W consecutive cards.
#
# Return true if and only if she can.
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# Example 2:
#
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
#
# Note:
# - 1 <= hand.length <= 10000
# - 0 <= hand[i] <= 10^9
# - 1 <= W <= hand.length

import collections
import heapq

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    # use heap if need min value continuously. heap can only remove min/max, not key based.
    def isNStraightHand(self, hand, W): # USE THIS: O(nlogn) 160ms
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W: return False

        counts = collections.Counter(hand)
        heapq.heapify(hand)

        for _ in xrange(len(hand)//W):
            while counts[hand[0]] == 0:
                heapq.heappop(hand)
            start = heapq.heappop(hand)

            for i in xrange(start, start+W):
                if counts[i] <= 0:
                    return False
                counts[i] -= 1
        return True


    def isNStraightHand_slow(self, hand, W): # O(n^2), 920ms
        if len(hand) % W: return False

        import collections
        cnts = collections.Counter(hand)
        for _ in xrange(len(hand)/W):
            lead = min(cnts)
            for i in xrange(lead, lead+W):
                if cnts[i] <= 0: return False
                cnts[i] -= 1
                if cnts[i] == 0:
                    del cnts[i]
        return True