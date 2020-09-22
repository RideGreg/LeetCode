# Time:  O(n)
# Space: O(h)

# 385
# Given a nested list of integers represented as a string, implement a parser to deserialize it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Note: You may assume that the string is well-formed:
#
# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].
# Example 1:
#
# Given s = "324",
#
# You should return a NestedInteger object which contains a single integer 324.
# Example 2:
#
# Given s = "[123,[456,[789]]]",
#
# Return a NestedInteger object containing a nested list with 2 elements:
#
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789.
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value. (A NestedInteger obj wrapping an int)
#        """
        self.x = [] if value == None else value

#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
        self.x.append(elem)

#    def setInteger(self, value): # NOT USED IN SOLUTION
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# 维护一个栈stack用于存储嵌套列表
# 第一个字符不是'['，说明遇到了数字，直接返回
# 第一个字符是'['，是列表，maintain a current working NestedInteger as a list, 分情况讨论:
# - 数字和负号：update digit
# - 左括号：push stack: push current working obj to stack, init a new working obj
# - 逗号：前面如果为数字，把数字append to current obj
# - 右括号：pop stack. 前面如果为数字，把数字append to current obj。另外pop stack,
#   把current obj 压缩到栈顶弹出来的列表

class Solution(object):
    def deserialize(self, s: str) -> NestedInteger: # USE THIS
        # edge case
        if not s: return NestedInteger()
        if s[0] != '[': return NestedInteger(int(s))

        stk, cur, num, sign = [], None, 0, 1
        for i, c in enumerate(s):
            if c == '-':
                sign = -1
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                if cur is not None:
                    stk.append(cur)
                cur = NestedInteger()  # an empty list
            elif c in ',]':
                if s[i-1].isdigit():
                    cur.add(NestedInteger(sign*num))
                    num, sign = 0, 1
                if c == ']' and stk:
                    pre = stk.pop()
                    pre.add(cur)
                    cur = pre
        return cur


    def deserialize_kamyu(self, s): # easy to make mistake by using start/end pointers.
        if not s:
            return NestedInteger()

        if s[0] != '[':
            return NestedInteger(int(s))

        stk = []

        i = 0 # start of integer, move after seeing ",[]", not move seeing "-0..9"
        for j in range(len(s)):
            if s[j] == '[':               # a new entry in stack
                stk.append(NestedInteger())
                i = j+1
            elif s[j] in ',]':
                if s[j-1].isdigit():
                    stk[-1].add(NestedInteger(int(s[i:j]))) # int must wrap in obj
                if s[j] == ']' and len(stk) > 1:
                    cur = stk.pop()
                    stk[-1].add(cur)
                    #stk[-1].add(stk.pop()) # WRONG!! '[[]]' returns a 1-layer []
                i = j+1

        return stk[-1]

print(Solution().deserialize("[[]]")) # NestedInteger([NestedInteger([])])
print(Solution().deserialize("[12,-34,[56,[78,9],10]]"))
# NestedInteger([
#     NestedInteger(12),
#     NestedInteger(-34),
#     NestedInteger([
#         NestedInteger(56),
#         NestedInteger([
#             NestedInteger(78),
#             NestedInteger(9),
#         ]),
#         NestedInteger(10),
#     ]),
# ])