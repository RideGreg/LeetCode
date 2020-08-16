# Time:  O(n)
# Space: O(n)
# 224
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
#

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

# Why stack?
# No matter left to right or right to left, need to get previous operand, so stack is perfect.

# Why backward scan?
# If forward scan the input, we end up calculate from right to left, not easy to handle subtraction '(A-B)-C'.
# so we scan from right to left, and calculate starting from left.

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        def compress():
            left, right = operands.pop(), operands.pop()
            op = operators.pop()
            operands.append(left + right if op == '+' else left - right)


        if s.lstrip()[0] == '-':     # edge case: start with '-'
            s = '0' + s

        operands, operators = [], [] # use 1 stack doesn't work '(3+1)', need to
                                     # change code to pop ')' before storing the sum.
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] in ')+-':
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    compress()
                operators.pop()         # pop out ')'
            #else: skip for empty space ' '

        while operators:
            compress()

        return operands[-1]


print(Solution().calculate("7 + 1")) # 8
print(Solution().calculate("3-1 + 2")) # 4
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)")) # 23
print(Solution().calculate("- 1")) # -1
print(Solution().calculate("-(1 + 2)")) # -3


