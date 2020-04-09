# Time:  O(n)
# Space: O(n)

# 654
# Given an integer array with no duplicates.
# A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # monotonic stack strictly decreasing.
        # Scan nums, build a tree node per num. For each num, keep popping stack until empty or
        # a bigger num, current smaller elem is on right subtree of the bigger num. Last popped
        # num is current num's left child. Then push current num into stack.
        # https://github.com/kamyu104/LintCode/blob/master/C++/max-tree.cpp
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop() # 弹栈：小数隔离在左边，不再需要
            if stack:
                stack[-1].right = node
            stack.append(node) # 压栈：每个数
        return stack[0]

    # Time: O(nlogn) avg, O(n^2) worst. At each level of the recursive tree, we traverse over all
    # the n elements to find the maximum element. In the average case, there will be a logn levels
    # leading to a complexity of O(nlogn). In the worst case, the depth of the recursive tree
    # can grow up to n, which happens in the case of a sorted nums array, giving a complexity of O(n^2).

    # Space: O(n) worst, i.e. O(h) worst case h = n
    def constructMaximumBinaryTree_recursion(self, nums):
        if not nums:
            return None
        i = 0
        for j in xrange(1, len(nums)):
            if nums[i] < nums[j]:
                i = j
        # better than: i = nums.index(max(nums))
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        return root