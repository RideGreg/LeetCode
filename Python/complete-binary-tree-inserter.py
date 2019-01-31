# Time:  ctor:     O(n)
#        insert:   O(1)
#        get_root: O(1)
# Space: O(n)

# 919
# A complete binary tree is a binary tree in which every level,
# except possibly the last, is completely filled,
# and all nodes are as far left as possible.
#
# Write a data structure CBTInserter that is initialized with
# a complete binary tree and supports the following operations:
#
# CBTInserter(TreeNode root) initializes
# the data structure on a given tree with head node root;
# CBTInserter.insert(int v) will insert a TreeNode into the tree
# with value node.val = v so that the tree remains complete,
# and returns the value of the parent of the inserted TreeNode;
# CBTInserter.get_root() will return the head node of the tree.
#
# Example 1:
#
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# Example 2:
#
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]
#
# Note:
# - The initial given tree is complete and contains between 1 and 1000 nodes.
# - CBTInserter.insert is called at most 10000 times per test case.
# - Every value of a given or inserted node is between 0 and 5000.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.__tree = []
        level = [root]
        while level:
            nextLevel = []
            for node in level:
                self._addNode(node) # if input tree is not complete, otherwise self.seq.append(node)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        cur = TreeNode(v)
        return self._addNode(cur)

    def _addNode(self, cur):
        n = len(self.__tree)
        self.__tree.append(cur)
        if n == 0: return None

        par = self.__tree[(n-1)//2]
        if n % 2:
            par.left = cur
        else:
            par.right = cur
        return par.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.__tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
