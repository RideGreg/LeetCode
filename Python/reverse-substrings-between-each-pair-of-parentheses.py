# Time:  O(n)
# Space: O(n)

# 1190 weekly contest 154 9/14/2020

# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.

class Solution(object):
    def reverseParentheses(self, s: str) -> str: # USE THIS. Time is O(n^2), may revert n times.
        """
        :type s: str
        :rtype: str
        """
        stk, curStr = [], ''
        for c in s:
            if c == '(':
                stk.append(curStr)
                curStr = ''
            elif c == ')':
                curStr = stk.pop() + curStr[::-1]
            else:
                curStr += c
        return curStr

    def reverseParentheses2(self, s):
        stk = [[]]
        for c in s:
            if c == '(':
                stk.append([])
            elif c == ')':
                stuff = stk.pop()
                for x in reversed(stuff):
                    stk[-1].append(x)
            else:
                stk[-1].append(c)
        return "".join(stk.pop())

    # Better time complexity O(n)
    def reverseParentheses_awice(self, s): # awice, two passes
        """
        :type s: str
        :rtype: str
        """
        stk, lookup = [], {}
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                j = stk.pop()
                lookup[i], lookup[j] = j, i
        result = []
        i, d = 0, 1
        while i < len(s):
            if i in lookup:
                i = lookup[i]
                d *= -1
            else:
                result.append(s[i])
            i += d
        return "".join(result)



print(Solution().reverseParentheses("(abcd)")) # "dcba'
print(Solution().reverseParentheses("(ab)(cd)")) # "badc'
print(Solution().reverseParentheses("(ua(love)ib)")) # "biloveau"
print(Solution().reverseParentheses("(ed(et(oc))el)")) # "leetcode"
print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q")) # "apmnolkjihgfedcbq"
print(Solution().reverseParentheses("ta()usw((((a))))")) # 'tauswa'
print(Solution().reverseParentheses("vdgzyj()")) # 'vdgzyj'
