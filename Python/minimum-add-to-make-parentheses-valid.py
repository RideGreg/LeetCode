# Time:  O(n)
# Space: O(1)

# 921
# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        open, ans = 0, 0
        for c in S:
            if c == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    ans += 1
        return ans + open

    # Keep track of the balance of the string: # of '(''s minus # of ')''s. A string is valid if its balance is 0,
    # plus every prefix has non-negative balance.
    #
    # The above idea is very useful with matching brackets problems.
    #
    # Now, consider the balance of every prefix of S. If it is ever negative (say, -1), we must add a '(' bracket.
    # Also, if the balance of S is positive (say, +B), we must add B ')' brackets at the end.
    def minAddToMakeValid_LeetCodeOfficial(self, S):
        add, bal, = 0, 0
        for c in S:
            bal += 1 if c == '(' else -1
            if bal == -1:
                add += 1
                bal = 0
        return add + bal

'''
'())' => 1
'(((' => 3
'()' => 0
'()))((' => 4
'''