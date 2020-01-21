# Time:  O(n^2)
# Space: O(n)

# 1190 weekly contest 154 9/14/2020

# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.

class Solution(object):
    def reverseParentheses(self, s): # USE THIS: awice
        """
        :type s: str
        :rtype: str
        """
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


    def reverseParentheses_ming(self, s: str) -> str:
        stk, tmp, ans = [], [], []
        for c in s:
            if c == ')': # process the last pair of ()
                while stk:
                    x = stk.pop()
                    if x == '(': break
                    else: tmp.append(x)
                if stk:
                    stk.extend(tmp)
                else:
                    ans.extend(tmp)
                tmp = []
            elif c == '(' or stk:
                stk.append(c)
            else:
                ans.append(c)
        return ''.join(ans)

    # recursion: wrong, some inputs are not recursive
    def reverseParentheses_wrong(self, s: str) -> str:
        # doesn't work for (ab)(cd)
        def foo(start, end):
            if start >= end: return ''
            i, j = start, end-1
            while i < j and s[i] != '(':
                i += 1
            if i == j: return s[start:end]
            while i < j and s[j] != ')':
                j -= 1
            return s[start:i] + foo(i+1, j)[::-1] + s[j+1:end]

        return foo(0, len(s))

print(Solution().reverseParentheses("(abcd)")) # "dcba'
print(Solution().reverseParentheses("(ab)(cd)")) # "badc'
print(Solution().reverseParentheses("(ua(love)ib)")) # "biloveau"
print(Solution().reverseParentheses("(ed(et(oc))el)")) # "leetcode"
print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q")) # "apmnolkjihgfedcbq"
print(Solution().reverseParentheses("ta()usw((((a))))")) # 'tauswa'
print(Solution().reverseParentheses("vdgzyj()")) # 'vdgzyj'
