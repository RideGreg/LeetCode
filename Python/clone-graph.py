# Time:  O(n)
# Space: O(n)
#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
# Definition for a undirected graph node
class Node:
    def __init__(self, x = 0, nei = []):
        self.val = x
        self.neighbors = list(nei)


# 图的深拷贝即构建一张与原图结构，值均一样的图，但是其中的节点不再是原来图节点的引用，所以邻节点list不是简单复制，而是重建。
# 本题就是遍历整张图，对每个节点进行拷贝。
# 为避免在深拷贝时陷入死循环，需要用一种数据结构记录已经被克隆过的节点。

# DFS or BFS to iterate all nodes, use a dict to manage the src-dest mapping and nodes already visited.
# For each SRC node: init its clone DEST node (set up 'val'), add mapping to dict; add SRC to stack/queue.
# For each SRC node in stack/queue: set its DEST's neighbors (the DEST may be new or created before).
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        mapping = {}
        mapping[node] = Node(node.val)
        stack = [node]

        while stack:
            current = stack.pop()
            for neighbor in current.neighbors:
                if neighbor not in mapping:
                    stack.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val)

                mapping[current].neighbors.append(mapping[neighbor])
        return mapping[node]

# 1-2
# | |
# 4-3
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.extend([n2, n4])
n2.neighbors.extend([n1, n3])
n3.neighbors.extend([n2, n4])
n4.neighbors.extend([n1, n3])
ans = Solution().cloneGraph(n1)

#   1
#  / \
# 0--2--
#    |_|
n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n0.neighbors.extend([n1, n2])
n1.neighbors.extend([n0, n2])
n2.neighbors.extend([n0, n1, n2])
ans = Solution().cloneGraph(n0)
