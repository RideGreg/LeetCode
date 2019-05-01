# Time:  O(n)
# Space: O(h)

# 1028
# We run a preorder depth first search on the root of a binary tree.
#
# At each node in this traversal, we output D dashes (where D is the depth of this node),
# then we output the value of this node.  (If the depth of a node is D, the depth of its
# immediate child is D+1.  The depth of the root node is 0.)
#
# If a node has only one child, that child is guaranteed to be the left child.
#
# Given the output S of this traversal, recover the tree and return its root.

# - The number of nodes in the original tree is between 1 and 1000.
# - Each node will have a value between 1 and 10^9.

# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]

# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative stack solution
class Solution(object):
    def recoverFromPreorder(self, S): # USE THIS
        """
        :type S: str
        :rtype: TreeNode
        """
        i, lookup = 0, {}
        while i < len(S):
            j = i
            while j < len(S) and S[j] == '-':
                j += 1
            k = j
            while k < len(S) and S[k].isdigit():
                k += 1
            dep = j - i
            node = TreeNode(int(S[j:k]))
            lookup[dep] = node
            if dep:
                p = lookup[dep-1]
                if not p.left:
                    p.left = node
                else:
                    p.right = node
            i = k
        return lookup[0]

    # save the construction path in a stack.
    # In each loop,  we get the number level of '-', and the value val of node to add.
    #
    # If the size of stack is bigger than the level of node,
    # we pop the stack until it's not.
    #
    # Finally we return the first element in the stack, as it's root of our tree.
    def recoverFromPreorder_lee215(self, S):
        stack, i = [], 0
        while i < len(S):
            level, val = 0, []
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val.append(S[i])
                i += 1
            while len(stack) > level:   # pop until return to the parent level
                stack.pop()
            node = TreeNode(int("".join(val)))
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]


# Time:  O(n)
# Space: O(h)
# recursive solution
class Solution2(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        def recoverFromPreorderHelper(S, level, i):
            j = i[0]
            while j < len(S) and S[j] == '-':
                j += 1 
            if level != j - i[0]:
                return None
            i[0] = j
            while j < len(S) and S[j] != '-':
                j += 1
            node = TreeNode(int(S[i[0]:j]))
            i[0] = j
            node.left = recoverFromPreorderHelper(S, level+1, i)
            node.right = recoverFromPreorderHelper(S, level+1, i)
            return node

        return recoverFromPreorderHelper(S, 0, [0])
