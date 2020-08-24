# Time:  O(n)
# Space: O(1)

# 921 also check 1541 minimum-insertions-to-balance-a-parentheses-string.py
#
# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

class Solution(object):
    # add + bal: 左边没close的‘）’加上右边没close的‘（’

    # Keep track of the balance of the string: # of '(''s minus # of ')''s. A string is valid if its balance is 0,
    # plus every prefix has non-negative balance.
    #
    # The above idea is very useful with matching brackets problems.
    #
    # Now, consider the balance of every prefix of S. If it is ever negative (say, -1), we must add a '(' bracket.
    # Also, if the balance of S is positive (say, +B), we must add B ')' brackets at the end.
    def minAddToMakeValid(self, S):
        add, bal, = 0, 0
        for c in S:
            if c == '(':
                bal += 1
            else:
                bal -= 1
                if bal < 0: # insert a (
                    add += 1
                    bal += 1
        return add + bal


print(Solution().minAddToMakeValid('())')) # 1
print(Solution().minAddToMakeValid('((('))  # 3
print(Solution().minAddToMakeValid('()'))  # 0
print(Solution().minAddToMakeValid('()))(('))  # 4