# Time:  O(n)
# Space: O(h)

# 1145
# Two players play a turn based game on a binary tree.  We are given the root of this binary tree,
# and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.
#
# Initially, the first player names a value x with 1 <= x <= n, and the second player names
# a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red,
# and the second player colors the node with value y blue.
#
# Then, the players take turns starting with the first player.  In each turn, that player chooses
# a node of their color (red if player 1, blue if player 2) and colors an UNCOLORED neighbor of
# the chosen node (either the left child, right child, or parent of the chosen node.)
#
# If (and only if) a player cannot choose such a node in this way, they must pass their turn. 
# If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
#
# You are the second player.  Return true or false indicating if it is possible to choose such
# a y to ensure you win the game,

#               1
#        2           3
#    4      5      6   7
#  8  9   10  11
# Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# Output: true. The second player can choose the node with value 2.

# first player选择了一个红色结点，将二叉树切割为3个部分（连通分量）。注意空子树也算一个部分。
# 要想取胜，答案的第一步就是选first player已选用的节点的左孩子，右孩子和父节点中的一个，
# 遍历找到这三个节点的各自联通的节点数，只要有一个超过总节点树的一半，就能赢。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            if node.val == x:
                left_right = [left, right]
            return left + right + 1

        left_right = [0, 0]
        dfs(root)
        parent = n - sum(left_right) - 1
        blue = max(max(left_right), parent)
        return blue > n-blue

root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.left, root.left.right = TreeNode(4), TreeNode(5)
root.right.left, root.right.right = TreeNode(6), TreeNode(7)
root.left.left.left, root.left.left.right = TreeNode(8), TreeNode(9)
root.left.right.left, root.left.right.right = TreeNode(10), TreeNode(11)

print(Solution().btreeGameWinningMove(root, 11, 3)) # True