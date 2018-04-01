#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root: return []
        ans, level = [], []
        import collections
        q = collections.deque([root, '#'])
        while q:
            cur = q.popleft()
            if cur != '#':
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            else:
                ans.append(level)
                level = []
                if q:
                    q.append('#')
        return ans

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print Solution().levelOrder(root)