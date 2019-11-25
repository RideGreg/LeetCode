# Time:  O(2^n)
# Space: O(2^n)

# 1049 weekly contest 137 5/18/2019
# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y
# with x <= y.  The result of this smash is:
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
#
# At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone
# (the weight is 0 if there are no stones left.)

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100

# DP: The value of the final rock would be a summation of all numbers with +/- signs. We enumerate all
# possible values from +/- all numbers, and get the one with minimum abs value.

class Solution(object):
    def lastStoneWeightII(self, stones):
        dp = {0}
        for stone in stones:
            ndp = set()
            for k in dp:
                ndp.update({k+stone, k-stone})
            dp = ndp
        return min(dp, key=abs)

    def lastStoneWeightII_kamyu(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp = {0}
        for stone in stones:
            dp |= {stone+i for i in dp}
        S = sum(stones)
        return min(abs(i-(S-i)) for i in dp)

    # As we are trying to minimize the size of the final rock, we need to find a partition of numbers
    # in the array into two subsets, which have the least amount of differenc in their summations.
    # We can reformulate this as a 0-1 Knapsack, i.e. collecting some rocks, where the weights of
    # the rocks is maximized and their total weight does not exceed half of the total weight of the rocks.
    def lastStoneWeightII_knapsack(self, stones: List[int]) -> int:
        total = sum(stones)
        Max_weight = int(total / 2)

        current = [0] * (Max_weight + 1)

        for v in stones:
            for w in range(Max_weight, -1, -1):
                if w - v >= 0:
                    current[w] = max(v + current[w - v], current[w])

        return total - 2 * current[-1]

print(Solution().lastStoneWeightII([2,7,4,1,8,1])) # 1