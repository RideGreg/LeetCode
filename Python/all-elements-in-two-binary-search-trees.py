# Time:  O(m+n)
# Space: O(h), stack space to store nodes.

# 1305
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getAllElements(self, root1, root2): # USE THIS: generator version
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder_gen(root):
            stack = [(root, False)]
            while stack:
                root, is_visited = stack.pop()
                if root:
                    if is_visited:
                        yield root.val
                    else:
                        stack.append((root.right, False))
                        stack.append((root, True))
                        stack.append((root.left, False))
            yield None
        
        result = []
        left_gen, right_gen = inorder_gen(root1), inorder_gen(root2)
        left, right = next(left_gen), next(right_gen)
        while left is not None or right is not None: # must compare to None, because value can be 0
            if left is not None and (right is None or left < right):
                result.append(left)
                left = next(left_gen)
            else:
                result.append(right)
                right = next(right_gen)
        return result

    # Time O(m+n), Space O(m+n). m and n are the number of nodes in two trees.
    def getAllElements2(self, root1, root2): # use more space, iterator version
        def inorder(root):
            result, stack = [], [(root, False)]
            while stack:
                root, is_visited = stack.pop()
                if root:
                    if is_visited:
                        result += root.val,
                    else:
                        stack.append((root.right, False))
                        stack.append((root, True))
                        stack.append((root.left, False))
            return result

        ans = []
        l1, l2 = inorder(root1), inorder(root2)
        i = j = 0
        while i < len(l1) or j < len(l2):
            if i < len(l1) and (j == len(l2) or l1[i] <= l2[j]):
                ans.append(l1[i])
                i += 1
            else:
                ans.append(l2[j])
                j += 1
        return ans

rt1 = TreeNode(2)
rt1.left, rt1.right = TreeNode(1), TreeNode(4)
rt2 = TreeNode(1)
rt2.left, rt2.right = TreeNode(0), TreeNode(3)
print(Solution().getAllElements(rt1, rt2)) #[0,1,1,2,3,4]