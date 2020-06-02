# Time:  O(n)
# Space: O(n)
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree_ming(self, preorder, inorder): #USE THIS
        def build(preleft, inleft, length):
            if length <= 0: return None
            idx = lookup[preorder[preleft]]
            node = TreeNode(preorder[preleft])
            node.left = build(preleft+1, inleft, idx-inleft)
            node.right = build(preleft+idx-inleft+1, idx+1, length-(idx-inleft+1))
            return node

        lookup = {n: i for i, n in enumerate(inorder)}
        return build(0, 0, len(preorder))


    def buildTree(self, preorder, inorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))

    def buildTreeRecu(self, lookup, preorder, inorder, pre_start, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(preorder[pre_start])
        i = lookup[preorder[pre_start]]
        node.left = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1, in_start, i)
        node.right = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1 + i - in_start, i + 1, in_end)
        return node


# time: O(n)
# space: O(n)
class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_iterator = iter(preorder)
        inorder_lookup = {n: i for i, n in enumerate(inorder)}
        
        def helper(start, end):
            if start > end:
                return None
            
            root_val = next(preorder_iterator)
            root = TreeNode(root_val)
            idx = inorder_lookup[root_val]
            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root

        return helper(0, len(inorder)-1)

if __name__ ==  "__main__":
    preorder = [1, 2, 3]
    inorder = [2, 1, 3]
    result = Solution().buildTree(preorder, inorder)
    print(result.val)
    print(result.left.val)
    print(result.right.val)
