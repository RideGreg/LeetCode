# Time:  O(n)
# Space: O(w)

# 958
# Given a binary tree, determine if it is a complete binary tree.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree, every level, except possibly the last, is completely filled, and
# all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    # Representing the position of each node (root is 1, left/right children are 2v and 2v+1)
    # maintain count of total nodes. Location of each node should match the count.
    def isCompleteTree(self, root):  # USE THIS
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque([(root, 1)])
        cnt = 0
        while q:
            node, idx = q.popleft()
            cnt += 1
            if cnt != idx: return False

           if node.left:
                q.append((node.left, 2*idx))
            if node.right:
                q.append((node.right, 2*idx+1))
        return True

        ''' ALTERNATIVELY USE LIST REPLACE, NOT RECOMMENDED AS EACH TIME CREATE A NEW LIST
        cur = [(root, 1)]
        count = 0
        while cur:
            next_level = []
            for node, pos in cur:
                count += 1
                if count != pos: return False
                if node.left:
                    next_level.append((node.left, 2 * pos))
                if node.right:
                    next_level.append((node.right, 2 * pos + 1))
            cur = next_level
        return True
        '''

    def isCompleteTree_geeksforgeeks(self, root):
        # level order tranverse. Once a node is found which is NOT a Full Node, all the following nodes
        # must be leaf nodes. And need to check: if a node has empty left child, then the right child must be empty.
        # https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-complete-tree-or-not/
        import collections
        if not root: return True
        q = collections.deque([root])
        havePartialNode = False
        while q:
            cur = q.popleft()
            if cur.left:
                if havePartialNode: return False
                q.append(cur.left)
            else:
                havePartialNode = True

            if cur.right:
                if havePartialNode: return False
                q.append(cur.right)
            else:
                havePartialNode = True
        return True

    # Code is complex: three cases of incomplete tree, has to level order with list replace
    # because need the # of nodes at this and upper level, cannot use deque.
    def isCompleteTree_ming(self, root: TreeNode) -> bool:
        cur, dep = [root], 0
        while cur:
            nxt = []
            for i, node in enumerate(cur):
                # case 1: has right child but no left child
                if node.right and not node.left:
                    return False
                # case 2: siblings before this node is incomplete
                if (node.left or node.right) and len(nxt) < 2 * i:
                    return False
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            # case 3: upper level is incomplete
            if nxt and len(cur) < 2 ** dep:
                return False
            cur = nxt
            dep += 1
        return True

root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.right = TreeNode(4)
print(Solution().isCompleteTree(root)) # False

root.left.left, root.left.right = TreeNode(4), None
print(Solution().isCompleteTree(root)) # True