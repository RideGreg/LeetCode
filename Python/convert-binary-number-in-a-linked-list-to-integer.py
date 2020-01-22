# Time:  O(n)
# Space: O(1)

# 1290 weekly contest 167 12/14/2019

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either
# 0 or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = 0
        while head: 
            result = result*2 + head.val 
            head = head.next 
        return result

print(Solution().getDecimalValue([1,0,1])) # 5
print(Solution().getDecimalValue([0])) # 0
print(Solution().getDecimalValue([1])) # 1
print(Solution().getDecimalValue([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])) # 18880
print(Solution().getDecimalValue([0,0])) # 0