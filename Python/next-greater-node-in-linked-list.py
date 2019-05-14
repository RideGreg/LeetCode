# Time:  O(n)
# Space: O(n)

# 1019
# We are given a linked list with head as the first node.  Let's number the nodes in the list:
# node_1, node_2, node_3, ... etc.
#
# Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that
# j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.
#
# Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
#
# Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

# Input: [2,7,4,3,5]
# Output: [7,0,5,5,0]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        result, stk = [], []
        while head:
            while stk and stk[-1][1] < head.val:
                result[stk.pop()[0]] = head.val
            stk.append([len(result), head.val])
            result.append(0)
            head = head.next
        return result

    # same as above, just use index i for easy understanding
    def nextLargerNodes_ming(self, head):
        stk, ans, i = [], [], 0
        while head:
            while stk and stk[-1][1] < head.val:
                ans[stk.pop()[0]] = head.val
            stk.append((i, head.val))
            i += 1
            ans.append(0)
            head = head.next
        return ans