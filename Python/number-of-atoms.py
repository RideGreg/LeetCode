# Time:  O(n)
# Space: O(n)

# 726
# Given a chemical formula (given as a string), return the count of each atom.
#
# An atomic element always starts with an uppercase character,
# then zero or more lowercase letters, representing the name.
#
# 1 or more digits representing the count of that element may follow if the count is greater than 1.
# If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
#
# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a formula.
# For example, (H2O2) and (H2O2)3 are formulas.
#
# Given a formula, output the count of all elements as a string in the following form:
# the first name (in sorted order), followed by its count (if that count is more than 1),
# followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
#
# Example 1:
# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.
#
# Example 2:
# Input:
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation:
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
#
# Example 3:
# Input:
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation:
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# Note:
#
# All atom names consist of lowercase letters, except for the first character which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses,
# and is a valid formula as defined in the problem.

import collections
import re


class Solution(object):
    # refer to decode-string.py: same pattern: use for loop, isdigit -> update curNum, islower -> update curString.
    # Stack stores counter, see (: push stack, see ): pop stack. Maintain curString, curNum, curDict.
    def countOfAtoms(self, formula): # USE THIS
        """
        :type formula: str
        :rtype: str
        """
        stack = [collections.Counter()]
        curString, curNum, curDict = '', 0, {}
        formula += '#'
        for c in formula:
            if c.islower():
                curString += c
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else: # ()#A-Z
                # first process curDict or curString
                if curDict:
                    for k, v in curDict.items():
                        stack[-1][k] += v * (curNum or 1)
                    curDict, curNum = {}, 0
                elif curString:
                    stack[-1][curString] += curNum or 1
                    curString, curNum = '', 0

                if c == '(':
                    stack.append(collections.Counter())
                elif c == ')':
                    curDict = stack.pop()
                else:
                    curString = c

        ans = []
        for name in sorted(stack[-1]):
            if stack[-1][name] > 1:
                name += str(stack[-1][name])
            ans.append(name)
        return ''.join(ans)

    # similar to solution 1, but use while loop
    def countOfAtoms2(self, formula):
        N = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))

    # 无论何时涉及文本解析，都可使用正则表达式
    # ([A-Z][a-z]*) 代表匹配一个大写字符，后跟任意数量的小写字符，然后 (\d*) 代表匹配任意数量的数字。
    # (\() 匹配左括号， (\)) 匹配右括号，(\d*) 匹配任意数量的数字。
    # 解析到一个原子名称 ([A-Z][a-z]*)(\d*)，我们将添加相印的数量。
    # 遇到了左括号，向堆中添加一个数 count 表示括号的系数。
    # 遇到了右括号，乘以 count,top = stack.pop()，并添加相印的计数中。
    def countOfAtoms3(self, formula):
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stk = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
              stk[-1][name] += int(m1 or 1)
            if left_open:
              stk.append(collections.Counter())
            if right_open:
                top = stk.pop()
                for k, v in top.items():
                  stk[-1][k] += v * int(m2 or 1)

        return "".join(name + (str(stk[-1][name]) if stk[-1][name] > 1 else '') \
                       for name in sorted(stk[-1]))


print(Solution().countOfAtoms("H2O")) # "H2O"
print(Solution().countOfAtoms("Mg(OH2)2")) # "H4MgO2"
print(Solution().countOfAtoms("Mg((OH2))2")) # "H4MgO2"
print(Solution().countOfAtoms("Mg((OH2)2A)")) # "AH4MgO2"
print(Solution().countOfAtoms("K4(ON(SO3)2)2")) # "K4N2O14S4"