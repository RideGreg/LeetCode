# Time:  O(n)
# Space: O(1)

# 255
# Given an array of numbers, verify whether it is the correct preorder traversal sequence
# of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Consider the following binary search tree:
#      10
#    /   \
#   2     12
#  / \    /
# 1   5  11
#    / \
#   3   8
#      / \
#     7   9
#    /
#   6
# [10,2,1,5,3,8,7,6,9,12,11] -> True

# Preorder seq of BST should be [high->low high->low high-low ...]
# each high->low sub-seq is a diagonal of leftmost nodes.

class Solution:
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder): # USE THIS: stack
        low = float("-inf")
        path = []
        for p in preorder:
            if p < low:
                return False
            while path and p > path[-1]:  # found a right branch, all subsequent nodes
                low = path.pop()          # should less than parent node which is stored in 'low'
            path.append(p)    # decreasing mono stack, leftmost nodes in preorder
        return True

    def verifyPreorder2(self, preorder): # hard to understand, modify the input
        low, i = float("-inf"), -1
        for p in preorder:
            if p < low:
                return False
            while i >= 0 and p > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p
        return True


print(Solution().verifyPreorder([5,2,1,3,6])) # True
print(Solution().verifyPreorder([10,2,1,5,3,8,7,6,9,12,11])) # True
print(Solution().verifyPreorder([5,2,6,1,3])) # False
