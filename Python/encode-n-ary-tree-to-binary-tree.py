'''
N-ary tree => binary tree: for each node, first sibling becomes left child, first child becomes right child.
For example, you may encode the following N-ary tree
      1
    / | \
   2  3  4
     / \  \
    5  6  7

into a binary tree (or its mirror)
     1
      \
      2
     /
    3
   / \
  4   5
   \  /
   7  6

https://leetcode.com/articles/introduction-to-n-ary-trees/
https://groups.google.com/forum/#!topic/wncc_iitb/RrgohUZ-uhw
1. Create L to R sibling pointers at each level
2. Remove all but the leftmost child pointer of each node
3. Make the sibling pointer the right pointer.

https://www.careercup.com/question?id=6486564775395328
any N-ary tree can convert to a 1-D array

https://stackoverflow.com/questions/16911521/convert-an-n-ary-expression-tree-to-a-binary-tree
no contents
https://www.educative.io/collection/page/5642554087309312/5679846214598656/820001/preview
need to pay
https://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/
'''
# Time:  O(n)
# Space: O(h)

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        def encodeHelper(root, parent, index):
            if not root:
                return None
            node = TreeNode(root.val);
            if index+1 < len(parent.children):
                node.left = encodeHelper(parent.children[index+1], parent, index+1)
            if root.children:
                node.right = encodeHelper(root.children[0], root, 0);
            return node

        if not root:
            return None
        node = TreeNode(root.val);
        if root.children:
            node.right = encodeHelper(root.children[0], root, 0)
        return node

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        def decodeHelper(root, parent):
            if not root:
                return
            children = []
            node = Node(root.val, children)
            decodeHelper(root.right, node)
            parent.children.append(node)
            decodeHelper(root.left, parent)

        if not data:
            return None
        children = []
        node = Node(data.val, children)
        decodeHelper(data.right, node)
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
