# Time:  O(n)
# Space: O(h)

# Serialization is the process of converting a data structure or
# object into a sequence of bits so that it can be stored in a file
# or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can
# be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# For example, you may serialize the following tree
#
#     1
#   / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes
# a binary tree. You do not necessarily need to follow this format, so
# please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec: # USE THIS: preorder
    def serialize(self, root):  # BEST
        if not root:
            return '#'
        return '{} {} {}'.format(root.val, self.serialize(root.left), self.serialize(root.right))

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serializeHelper(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                serializeHelper(node.left)
                serializeHelper(node.right)
        vals = []
        serializeHelper(root)
        return ' '.join(vals)
        ''' Memory Limit Exceeded if pass the array as param
    def serialize(self, root):  #MLE
        def preOrder(n, vals):
            if not n:
                vals.append('#')
            else:
                vals.append(str(n.val))
                vals = preOrder(n.left, vals)
                vals = preOrder(n.right, vals)
            return vals

        vals = preOrder(root, [])
        return ' '.join(vals)

        # iteration solution:
        vals, stk = [], [(root, False)]
        while stk:
            node, visited = stk.pop()
            if node is None:
                vals.append('#')
                continue
            if visited:
                vals.append(str(node.val))
            else:
                stk.append((node.right, False))
                stk.append((node.left, False))
                stk.append((node, True))
        return ' '.join(vals)
        '''


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserializeHelper():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = deserializeHelper()
                node.right = deserializeHelper()
                return node
        def isplit(source, sep):
            sepsize = len(sep)
            start = 0
            while True:
                idx = source.find(sep, start)
                if idx == -1:
                    yield source[start:]
                    return
                yield source[start:idx]
                start = idx + sepsize
        vals = iter(isplit(data, ' ')) # should use data.split(), otherwise MEMORY LIMIT EXCEED
        return deserializeHelper()

        ''' if not familiar with iter/next
        def helper(i): # pass the index
            i += 1
            if vals[i] == '#':
                return (None, i)
            root = TreeNode(vals[i])
            root.left, i = helper(i)
            root.right, i = helper(i)
            return (root, i)

        vals = data.split()
        return helper(-1)[0]
        '''

class Codec_levelorder: # Memory Limit Exceeded
    def serialize(self, root):
        if not root: return '[]'
        curLevel, ans = [root], []
        while curLevel:
            nextLevel = []
            for cur in curLevel:
                if cur is None:
                    ans.append('#')
                else:
                    ans.append(str(cur.val))
                    nextLevel.append(cur.left)
                    nextLevel.append(cur.right)
            curLevel = nextLevel
        return ' '.join(ans)

    def deserialize(self, data):
        import collections
        if data == '[]':
            return None
        nodes = collections.deque([TreeNode(o) if o != '#' else None
                                    for o in data.split()])
        parents = collections.deque([nodes.popleft()]) if nodes else None
        root = parents[0] if parents else None
        while parents:
            parent = parents.popleft()
            left = nodes.popleft() if nodes else None
            right = nodes.popleft() if nodes else None
            parent.left, parent.right = left, right
            if left:
                parents.append(left)
            if right:
                parents.append(right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
root.right.left, root.right.right = TreeNode(4), TreeNode(5)
root.right.right.left = TreeNode(6)

codec = Codec()
data = codec.serialize(root) #: 1 2 # # 3 4 # # 5 6 # # #
print data
codec.deserialize(data)

codec = Codec_levelorder()
data = codec.serialize(root)
print data
codec.deserialize(data)