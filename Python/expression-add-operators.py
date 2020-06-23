# Time:  O(4^n), each of the n chars, explore 4 possibilities: +, - * and "extend digits, no op"
# Space: O(n), variable expr
# 282
# Given a string that contains only digits 0-9
# and a target value, return all possibilities
# to add operators +, -, or * between the digits
# so they evaluate to the target value.
#
# Examples:
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
#

from typing import List

class Solution(object):
    # dfs: operate on 3 values: num1 + num2 +/-/* val
    def addOperators(self, num: str, target: int) -> List[str]: # USE THIS: initial value is also handled in recursive function
        def dfs(start, num1, num2):
            if start == len(num):
                if num1 + num2 == target:
                    ans.append(''.join(expr))
                return

            val, val_str = 0, ''
            i = start
            while i < len(num):
                val = val * 10 + int(num[i])
                val_str += num[i]
                if str(val) != val_str: break  # prune '0....'

                if start == 0:
                    expr.append(val_str)
                    dfs(i+1, num1+num2, val)
                    expr.pop()
                else:
                    expr.append('+' + val_str)
                    dfs(i+1, num1+num2, val)
                    expr.pop()

                    expr.append('-' + val_str)
                    dfs(i+1, num1+num2, -val)
                    expr.pop()

                    expr.append('*' + val_str)
                    dfs(i+1, num1, num2*val)
                    expr.pop()

                i += 1

        expr, ans = [], []
        dfs(0, 0, 0)
        return ans

    # Follow up: for a simpler version, if only allow + and -. Expression: cur +/- val
    def addOperators_noMultiply(self, num: str, target: int) -> List[str]:
        def dfs(start, cur):
            if start == len(num):
                if cur == target:
                    ans.append(''.join(expr))
                return

            val, val_str = 0, ''
            i = start
            while i < len(num):
                val = val * 10 + int(num[i])
                val_str += num[i]
                if str(val) != val_str: break  # prune '0....'

                if start == 0:
                    expr.append(val_str)
                    dfs(i+1, val)
                    expr.pop()
                else:
                    expr.append('+' + val_str)
                    dfs(i+1, cur+val)
                    expr.pop()

                    expr.append('-' + val_str)
                    dfs(i+1, cur-val)
                    expr.pop()

                i += 1

        expr, ans = [], []
        dfs(0, 0)
        return ans


    def addOperators_kamyu(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result, expr = [], []
        val, val_str, i = 0, "", 0
        while i < len(num):
            val = val * 10 + ord(num[i]) - ord('0')
            val_str += num[i]
            # Avoid "0...".
            if str(val) != val_str:
                break
            expr.append(val_str)
            self.addOperatorsDFS(num, target, i + 1, 0, val, expr, result)
            expr.pop()
            i += 1
        return result

    def addOperatorsDFS(self, num, target, pos, operand1, operand2, expr, result):
        if pos == len(num) and operand1 + operand2 == target:
            result.append("".join(expr))
        else:
            val, i = 0, pos
            val_str = ""
            while i < len(num):
                val = val * 10 + ord(num[i]) - ord('0')
                val_str += num[i]
                # Avoid "0...".
                if str(val) != val_str:
                    break

                # Case '+':
                expr.append("+" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, val, expr, result)
                expr.pop()

                # Case '-':
                expr.append("-" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, -val, expr, result)
                expr.pop()

                # Case '*':
                expr.append("*" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1, operand2 * val, expr, result)
                expr.pop()

                i += 1


print(Solution().addOperators("123", 6)) # ["1+2+3", "1*2*3"]
print(Solution().addOperators("232", 8)) # ["2*3+2", "2+3*2"]
print(Solution().addOperators("105", 5)) # ["1*0+5","10-5"]
print(Solution().addOperators("00", 0)) # ["0+0", "0-0", "0*0"]
print(Solution().addOperators("3456237490", 9191)) # []
print(len(Solution().addOperators("123456789", 100))) # 78; if only allow +/-, return 11
# ['1+2+3+4+5+6+7+8*9', '1+2+3-4+5+6+78+9', '1+2+3-4*5+6*7+8*9', '1+2+3*4-5-6+7+89',
# '1+2+3-45+67+8*9', '1+2-3*4+5*6+7+8*9', '1+2-3*4-5+6*7+8*9', '1+2*3+4+5+67+8+9',
# '1+2*3+4*5-6+7+8*9', '1+2*3-4-5+6+7+89', '1+2+34-5+67-8+9', '1+2+34*5+6-7-8*9',
# '1+2*34-56+78+9', '1-2+3*4+5+67+8+9', '1-2+3*4*5+6*7+8-9', '1-2+3*4*5-6+7*8-9',
#
# '1-2+3+45+6+7*8-9', '1-2-3+4*5+67+8+9', '1-2-3+45+6*7+8+9' ...]