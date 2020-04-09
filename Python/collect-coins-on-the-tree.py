# Time: O(V+E)

# Given an n-ary tree, which has some coins in the tree nodes.
# Your job is to report the amount of steps needed to gather(and come back) all the coins

# Example: Nodes ABCFG has no coin, DE has coin. The steps to gather all coins and come back is 6.
#         A
#      /  |  \
#     B   C  (D)
#   /  \     /
# (E)   F    G

class Node:
	def __init__(self, hasCoin):
		self.children = []
		self.hasCoin = hasCoin

# Solution: the recursive subcall returns the total number of steps to collect all coins in
# this subtree and return to the root. It does this by recursing through all children,
# and summing total steps + 2 per child if the child has any coins. This 2 is the two steps
# it takes to go down to the child and come back up. If a child has no coins in the subtree,
# it returns -1 to signal that

class Solution(object):
	def collectCoins(self, root):
		def recurse(node: Node) -> int:
			s = 0
			for c in node.children:
				ret = recurse(c)
				if ret > -1:
					s += ret + 2
			return s if s or node.hasCoin else -1

		ans = recurse(root)
		return ans if ans > -1 else 0


a, b, c, d, e, f, g = Node(False), Node(False), Node(False), Node(True), Node(True), Node(False), Node(False)
b.children = [e, f]
d.children = [g]
a.children = [b, c, d]
print(Solution().collectCoins(a)) # 6