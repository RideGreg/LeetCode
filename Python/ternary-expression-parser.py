# Time:  O(n)
# Space: O(1)

# 439
# Given a string representing arbitrarily nested ternary expressions, calculate the result
# of the expression. You can always assume that the given expression is valid and only
# consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).
#
# Note:
# The length of the given string is ≤ 10000.
# Each number will contain only one digit.
# The conditional expressions group right-to-left (as usual in most languages).
# The condition will always be either T or F. That is, the condition will never be a digit.
# The result of the expression will always evaluate to either a digit 0-9, T or F.

class Solution(object):
    def parseTernary(self, expression): # USE THIS: push everything except the last char is ?
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ""

        stack = []
        for c in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()  # pop '?'
                first = stack.pop()
                second = stack.pop()
                stack.append(first if c == 'T' else second)
            elif c != ':':
                stack.append(c)
        return str(stack[-1])

    def parseTernary2(self, expression): # not push ?, use ? to update a flag
        if not expression: return ''

        stk, toJudge = [], False
        for c in reversed(expression):
            if toJudge:
                x, y = stk.pop(), stk.pop()
                stk.append(x if c == 'T' else y)
                toJudge = False
            elif c == '?':
                toJudge = True
            elif c.isdigit() or c in 'TF':
                stk.append(c)
        return stk[-1]


print(Solution().parseTernary("T?2:3")) # "2"
print(Solution().parseTernary("F?1:T?4:5")) # "4"
print(Solution().parseTernary("T?T?F:5:3")) # "F"
