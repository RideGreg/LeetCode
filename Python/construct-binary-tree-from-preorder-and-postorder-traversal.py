# Time:  O(n)
# Space: O(h)

# 889
# Return any binary tree that matches the given preorder and postorder traversals.
#
# Values in the traversals pre and post are distinct positive integers.
#
# Example 1:
#
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#
# Note:
#
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists.
# If there exists multiple answers, you can return any of them.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        stack = [TreeNode(pre[0])]
        j = 0
        for i in xrange(1, len(pre)):
            node = TreeNode(pre[i])
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def constructFromPrePost(self, pre, post): # USE THIS
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def re(s1, s2, n):
            if n < 1: return None
            root = TreeNode(pre[s1])
            if n > 1:
                left_size = post_idx_map[pre[s1 + 1]] - s2 + 1
                root.left = re(s1 + 1, s2, left_size)
                root.right = re(s1 + 1 + left_size, s2 + left_size, n - 1 - left_size)
            return root

        post_idx_map = {}
        for i, v in enumerate(post):
            post_idx_map[v] = i
        return re(0, 0, len(pre))


    def constructFromPrePost2(self, pre, post): # same as above, but use start/end
        def constructFromPrePostHelper(pre_s, pre_e, post_s, post_e):
            if pre_s >= pre_e or post_s >= post_e:
                return None
            node = TreeNode(pre[pre_s])
            if pre_e-pre_s > 1:
                left_tree_size = post_entry_idx_map[pre[pre_s+1]]-post_s+1
                node.left = constructFromPrePostHelper(pre_s+1, pre_s+1+left_tree_size,
                                                       post_s, post_s+left_tree_size)
                node.right = constructFromPrePostHelper(pre_s+1+left_tree_size, pre_e,
                                                        post_s+left_tree_size, post_e-1)
            return node

        post_entry_idx_map = {}
        for i, val in enumerate(post):
            post_entry_idx_map[val] = i
        return constructFromPrePostHelper(0, len(pre), 0, len(post))

# not good: create subarrays
class Solution3(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        id = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:id+2], post[:id+1])
        root.right = self.constructFromPrePost(pre[id+2:], post[id+1:-1])
        return root