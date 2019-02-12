# Time:  O(n)
# Space: O(1)

# 904
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following steps:
#
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree. 
# If there is no tree to the right, stop.
#
# Note that you do not have any choice after the initial choice of starting tree:
# you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit,
# but you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?
#
# Example 1:
#
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# Example 2:
#
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# Example 3:
#
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# Example 4:
#
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
#
# Note:
# - 1 <= tree.length <= 40000
# - 0 <= tree[i] < tree.length

import collections

# Sliding Window
# Get the longest subarray with at most two different numbers. Maintain the start of sliding window.
class Solution(object):
    def totalFruit(self, tree): # 200 ms
        """
        :type tree: List[int]
        :rtype: int
        """
        lookup = {} # index of the last time key appears
        s, ans = -1, 0
        for e, v in enumerate(tree):
            lookup[v] = e
            # 3rd new item: need to remove the oldest item and adjust window start point
            if len(lookup) > 2:
                a = min(lookup, key=lookup.get)
                s = lookup[a]
                del lookup[a]
            ans = max(ans, e-s)
        return ans

    # Same as the above, just use OrderedDict so get oldest (but this is slower 800 ms)
    def totalFruit_OrderedDict(self, tree):
        lookup = collections.OrderedDict() # index of the last time key appears
        s, ans = -1, 0
        for e, v in enumerate(tree):
            if v in lookup:
                del lookup[v]
            lookup[v] = e
            # 3rd new item: need to remove the oldest item and adjust window start point
            if len(lookup) > 2:
                k, s = lookup.popitem(last=False)
            ans = max(ans, e-s)
        return ans

    def totalFruit_LeetCodeOfficial(self, tree):
        count = collections.defaultdict(int)
        result, i = 0, 0
        for j, v in enumerate(tree):
            count[v] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            result = max(result, j-i+1)
        return result

    def totalFruit_groupByBlocks(self, tree):
        import itertools
        blocks = [(k, len(list(v)))
                  for k, v in itertools.groupby(tree)]

        ans = i = 0
        while i < len(blocks):
            # We'll start our scan at block[i].
            # types : the different values of tree[i] seen
            # weight : the total number of trees represented
            #          by blocks under consideration
            types, weight = set(), 0

            # For each block from i and going forward,
            for j in xrange(i, len(blocks)):
                # Add each block to consideration
                types.add(blocks[j][0])
                weight += blocks[j][1]

                # If we have 3 types, this is not a legal subarray
                if len(types) >= 3:
                    i = j - 1  # THIS ONLY WORKS FOR 2 TYPES. IF ALLOW 3 TYPES, CANNOT USE THIS TO FIND THE NEXT VALID START POINT.
                    break

                ans = max(ans, weight)

            # If we go to the last block, then stop
            else:
                break

        return ans
