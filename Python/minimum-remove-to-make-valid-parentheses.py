# Time:  O(n)
# Space: O(n)

# 1249 weekly contest 161 11/2/2019

# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that
# the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# - It is the empty string, contains only lowercase characters, or
# - It can be written as AB (A concatenated with B), where A and B are valid strings, or
# - It can be written as (A), where A is a valid string.

class Solution(object):
    def minRemoveToMakeValid(self, s): # USE THIS
        """
        :type s: str
        :rtype: str
        """
        result = list(s) # Excellent to reuse the string itself
        count = 0
        for i, v in enumerate(result):
            if v == '(':
                count += 1
            elif v == ')':
                if count:
                    count -= 1
                else:
                    result[i] = "" # delete ) without mapping ( before it
        if count:
            for i in reversed(range(len(result))): # delete ( without mapping ( behind it
                if result[i] == '(':
                    result[i] = ""
                    count -= 1
                    if not count:
                        break
        return "".join(result)

    # no need to store positions of (. The ( we delete are all from the behind.
    def minRemoveToMakeValid_ming(self, s: str) -> str:
        stk = [] # store the position of (
        ans = [] # store valid chars
        for c in s:
            if c == '(':
                stk.append(len(ans))
                ans.append(c)
            elif c == ')':
                if stk:       # only keep ) with mapping ( before it
                    stk.pop() # remove a (
                    ans.append(c)
            else:
                ans.append(c)
        for p in stk[::-1]:   # delete ( without mapping ( behind it
            ans.pop(p)
        return ''.join(ans)


print(Solution().minRemoveToMakeValid("lee(t(c)o)de)")) # "lee(t(c)o)de"
print(Solution().minRemoveToMakeValid("a)b(c)d")) # "ab(c)d"
print(Solution().minRemoveToMakeValid("))((")) # ""
print(Solution().minRemoveToMakeValid("(a(b(c)d)")) # "a(b(c)d)"