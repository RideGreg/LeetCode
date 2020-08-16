# Time:  O(n)
# Space: O(1)

# One way to serialize a binary tree is to use pre-oder traversal.
# When we encounter a non-null node, we record the node's value.
# If it is a null node, we record using a sentinel value such as #.
#
#      _9_
#     /   \
#   3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a
# correct preorder traversal serialization of a binary tree.
# Find an algorithm without reconstructing the tree.
#
# Each comma separated value in the string must be either an integer
# or a character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example
# it could never contain two consecutive commas such as "1,,3".
#
# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true
#
# Example 2:
# "1,#"
# Return false
#
# Example 3:
# "9,#,#,1"
# Return false

class Solution(object):
    # Leaf nodes should be 1 more than non-leaf nodes. Difference of non-leaf node minus
    # leaf node should be -1 only after finishing the serialization.
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        '''
        def split_iter(s, tok): # no need to call this iter, if doesn't need to save space
            start = 0
            for i in range(len(s)):
                if s[i] == tok:
                    yield s[start:i]
                    start = i + 1
            yield s[start:]
        '''
        if not preorder:
            return False

        realNode_leafNode, totalNode = 0, preorder.count(',') + 1
        #for tok in split_iter(preorder, ','): # iter for better space usage
        for tok in preorder.split(','):
            totalNode -= 1
            realNode_leafNode += 1 if tok != '#' else -1
            if realNode_leafNode < 0:
                break
        return totalNode == 0 and realNode_leafNode < 0

    # 定义一个概念叫做槽位，二叉树中任意一个节点或者空孩子节点都要占据一个槽位。二叉树的建立也伴随着槽位数量的变化。
    # 开始时只有一个槽位，如果根节点是空节点，就消耗掉一个槽位，如果根节点不是空节点，除了消耗一个槽位，
    # 还要为孩子节点增加两个新的槽位。如果最后可以将所有的槽位消耗完，那么这个前序序列化就是合法的。
    # Time O(n) Space O(n)
    def isValidSerialization2(self, preorder: str) -> bool:
        slots = 1  # number of available slots
        for node in preorder.split(','):
            slots -= 1     # one node takes one slot
            if slots < 0:  # no more slots available
                return False

            if node != '#':  # non-empty node creates two children slots
                slots += 2

        # all slots should be used up
        return slots == 0


print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")) # True
print(Solution().isValidSerialization("1,#")) # False
print(Solution().isValidSerialization("9,#,#,1")) # False