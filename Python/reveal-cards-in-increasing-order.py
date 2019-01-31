# Time:  O(n)
# Space: O(n)

# 950
# In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.
#
# Initially, all the cards start face down (unrevealed) in one deck.
#
# Now, you do the following steps repeatedly, until all cards are revealed:
#
# 1. Take the top card of the deck, reveal it, and take it out of the deck.
# 2. If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
# 3. If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

# Return an ordering of the deck that would reveal the cards in increasing order.
#
# The first entry in the answer is considered to be the top of the deck.

# Solution: Simulation:
# Simulate the revealing process with an index deck set of [0, 1, 2, ... n]. Put the cards from
# small to large at the index revealed one by one.

import collections


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

    def deckRevealedIncreasing_kamyu(self, deck): # revert the steps
        d = collections.deque()
        deck.sort(reverse=True)
        for i in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(i)
        return list(d)

print(Solution().deckRevealedIncreasing([1,2,3,4,5,6,7])) # 1 6 2 5 3 7 4
