# Time:  O(n)
# Space: O(logn)
# 109
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 利用升序链表是树的中序遍历left->cur->right
class Solution:
    head = None
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        current, length = head, 0
        while current:
            current = current.next
            length += 1
        self.head = head
        return self.sortedListToBSTRecu(0, length) # length not included

    def sortedListToBSTRecu(self, start, end):
        if start == end:
            return None
        mid = start + (end - start) // 2
        left = self.sortedListToBSTRecu(start, mid) # mid not included

        node = TreeNode(self.head.val)
        self.head = self.head.next # 每建一个节点就前挪一位
        node.left = left

        node.right = self.sortedListToBSTRecu(mid + 1, end)
        return node


# 分治，每次用快慢节点寻找链表中间节点
# 递归函数参数为左闭右开，因为没法从mid节点得到mid.prev节点。
# Time O(nlogn), Space O(logn) 递归栈使用空间
class Solution2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    result = Solution().sortedListToBST(head)
    print(result.val)
    print(result.left.val)
    print(result.right.val)