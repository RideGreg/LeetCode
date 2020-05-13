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
# 前序遍历为： (根结点) (前序遍历左分支) (前序遍历右分支)
# 而后序遍历为： (后序遍历左分支) (后序遍历右分支) (根结点)
# 如果我们知道左分支有多少个结点，我们就可以对这些数组进行分组，并用递归生成树的每个分支。
# 令左分支有 LL 个节点。我们知道左分支的头节点为 pre[1]，但它也出现在左分支的后序表示的最后。
# 所以 pre[1] = post[L-1]（因为结点的值具有唯一性），因此 L = post.indexOf(pre[1]) + 1。
class Solution2(object):
    def constructFromPrePost(self, pre, post): # USE THIS
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def re(s1, s2, n): # s1, s2: start position of pre/post subarray, n: length of subarray
            if n < 1: return None
            root = TreeNode(pre[s1])
            if n > 1:
                left_size = post_idx_map[pre[s1 + 1]] - s2 + 1   # O(1)
                # OR left_size = post.index(pre[s1+1]) - s2 + 1  O(n)
                root.left = re(s1 + 1, s2, left_size)
                root.right = re(s1 + 1 + left_size, s2 + left_size, n - 1 - left_size)
            return root

        post_idx_map = {v: i for i, v in enumerate(post)} # save multiple search of positions
                                                          # change O(n^2) to O(n)
        return re(0, 0, len(pre))


    def constructFromPrePost2(self, pre, post): # same as above, but recursive function uses 4 params
        def build(prei, prej, posti, postj):
            if prei > prej or posti > postj:
                return None
            node = TreeNode(pre[prei])
            if prej > prei:
                L = post_entry_idx_map[pre[prei+1]] - posti + 1
                node.left = build(prei+1, prei+L, posti, posti+L-1)
                node.right = build(prei+1+L, prej, posti+L, postj-1)
            return node

        post_entry_idx_map = {val : i for i, val in enumerate(post)}
        return build(0, len(pre)-1, 0, len(post)-1)

# space not good: each recursion create new arrays
class Solution3(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root