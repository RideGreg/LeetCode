# Time:  O(n)
# Space: O(logn)
#
# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# USE THIS: build by in-order. cleaner code to use left/rigth index.
class Solution(object):
    def sortedArrayToBST(self, nums):
        def build(l, r):
            if l > r: return None
            m = (l+r+1) // 2  # left subtree may have 1 more node. (l+r)//2 is okay too where right tree has more.
            node = TreeNode(nums[m])
            node.left = build(l, m-1)
            node.right = build(m+1, r)
            return node
        return build(0, len(nums)-1)

    # space not good. Allocate extra list as params.
    def sortedArrayToBST_extraSpace(self, nums):
        if not nums: return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# For reference only: use Iterator and build tree in pre-order.
# Time:  O(n)
# Space: O(logn)
class Solution2(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.iterator = iter(nums)
        return self.helper(0, len(nums))
    
    def helper(self, start, end):
        if start == end:
            return None
        
        mid = (start + end) // 2
        left = self.helper(start, mid)
        current = TreeNode(next(self.iterator))
        current.left = left
        current.right = self.helper(mid+1, end)
        return current

if __name__ == "__main__":
    num = [1, 2, 3]
    result = Solution().sortedArrayToBST(num)
    print result.val
    print result.left.val
    print result.right.val
