# Time:  O(n)
# Space: O(1)

# 1541 also check 921 minimum-add-to-make-parentheses-valid.py

# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
# - Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# - Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
#
# In other words, we treat '(' as openning parenthesis and '))' as closing parenthesis.
#
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
#
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
#
# Return the minimum number of insertions needed to make s balanced.

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        add, bal = 0, 0
        for c in s:
            if c == '(':
                if bal > 0 and bal%2: # insert a )
                    add += 1
                    bal -= 1
                bal += 2   # need two ) to balance
            else:
                bal -= 1
                if bal < 0: # insert a (
                    add += 1
                    bal += 2
        return add + bal

print(Solution().minInsertions("(()))")) # 1
print(Solution().minInsertions("())")) # 0
print(Solution().minInsertions("))())(")) # 3
print(Solution().minInsertions("((((((")) # 12
print(Solution().minInsertions(")))))))")) # 5
