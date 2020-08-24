# Time:  O(n)
# Space: O(n)
# 227
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces . The integer division should truncate toward
# zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.
#

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        def compress():
            left, right = operands.pop(), operands.pop()
            op = operators.pop()
            if op == '+': v = left + right
            elif op == '-': v = left - right
            elif op == '*': v = left * right
            elif op == '/': v = left // right
            operands.append(v)

        if s.lstrip()[0] == '-':     # edge case: start with '-'
            s = '0' + s
        s = '#'+s

        operands, operators = [], []
        curNum = ""
        for c in reversed(s):
            if c.isdigit():
                curNum += c
            else:
                if curNum != '':
                    operands.append(int(curNum[::-1]))
                    curNum = ''

                if c in ')*/':
                    operators.append(c)
                elif c in '+-':
                    while operators and operators[-1] in '*/':
                        compress()
                    operators.append(c)
                elif c == '(':
                    while operators[-1] != ')':
                        compress()
                    operators.pop()

        '''
        for i in reversed(xrange(len(s))):
            c = s[i]
            if c.isdigit():
                curNum += c
                if i == 0 or not s[i-1].isdigit(): # not good checking every time
                    operands.append(int(curNum[::-1]))
                    curNum = ""
            elif c in '*/)':
                operators.append(c)
            elif c in '+-':
                while operators and operators[-1] in '*/':
                    compress()
                operators.append(c)
            elif c == '(':
                while operators[-1] != ')':
                    compress()
                operators.pop()
        '''

        while operators:
            compress()
        return operands[-1]

print(Solution().calculate("3 + 2 * 2")) # 7
print(Solution().calculate("(3 + 2) * 2")) # 10
print(Solution().calculate("3- 5 / 2")) # 1
print(Solution().calculate("(1*(4+5+2)-3)+(6+8)")) # 22
print(Solution().calculate("-1 * 2")) # -2
