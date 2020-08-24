# Time:  O(n)
# Space: O(1)

# 856
# Given a balanced parentheses string S,
# compute the score of the string based on the following rule:
#
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
# Example 1:
#
# Input: "()"
# Output: 1
# Example 2:
#
# Input: "(())"
# Output: 2
# Example 3:
#
# Input: "()()"
# Output: 2
# Example 4:
#
# Input: "(()(()))"
# Output: 6
#
# Note:
# - S is a balanced parentheses string, containing only ( and ).
# - 2 <= S.length <= 50

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


'''
Count Cores: USE THIS
Intuition
The final sum will be a sum of powers of 2, as every core (a substring (), with score 1=2**0) will have
it's score multiplied by 2 for each exterior set of parentheses that contains that core. The answer
is the sum of these multiplied core values (powers of 2).

Algorithm
Keep track of the DEPTH of the string (# of ( minus # of ) ). For every core ("()"),
the answer is 1 << depth, as depth is the number of exterior set of parentheses surrounding this core.
e.g. (()(())) equals to (())+((())); it contains 2 cores: first core then multiply 2^1, 
second core then multiply 2^2.
'''
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        result, depth = 0, 0
        for i in xrange(len(S)):
            if S[i] == '(':
                depth += 1
            else:
                depth -= 1
                if S[i-1] == '(': # find a core
                    result += 2**depth
        return result

# Time:  O(n)
# Space: O(h) size of stack
'''
Every position in the string has a depth - some number of matching parentheses surrounding it. For example,
the dot in (()(.())) has depth 2, because of these parentheses: (__(.__))

Our goal is to maintain the score at the current depth we are on. When we see an opening bracket, we increase
our depth, and our score at the new depth is 0. When we see a closing bracket, we add twice the score of
the previous deeper part - except when counting (), which has a score of 1.

For example, when counting (()(())), our stack will look like this:
[0, 0] after parsing (
[0, 0, 0] after (
[0, 1] after )
[0, 1, 0] after (
[0, 1, 0, 0] after (
[0, 1, 1] after )
[0, 3] after )
[6] after )
'''
class Solution2(object):
    def scoreOfParentheses(self, S: str) -> int: # Ming's stack
        stk = []
        for c in S:
            if c == '(':
                stk.append(c)
            else:
                # see ): pop stack, if (, push 1; if int, accumulate then multiplied by 2
                n = 0
                while stk[-1] != '(':
                    n += stk.pop()
                stk.pop()
                v = 2 * n if n > 0 else 1
                stk.append(v)
        return sum(stk)

    # another stack implementation
    def scoreOfParentheses2(self, S):
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(1, 2*last)
        return stack[0]

'''
Partition (Divide and Conquer)
Time Complexity: O(n^2), where n is the length of S. An example worst case is (((((((....))))))).
Space Complexity: O(n), the size of the implied call stack.

Intuition
Split the string into S = A + B where A and B are balanced parentheses strings, and A is the smallest possible
non-empty prefix of S.

Algorithm
Call a balanced string primitive if it cannot be partitioned into two non-empty balanced strings.

By partition whenever balance (the # of ( minus the number of ) ) is zero, we can partition S
into primitive substrings S = P_1 + P_2 + ... + P_n. Then, score(S) = score(P_1) + score(P_2) + ... + score(P_n), by definition.

For each primitive substring (S[i], S[i+1], ..., S[k]), if the string is length 2, then the score of this string
is 1. Otherwise, it's twice the score of the inner substring (S[i+1], S[i+2], ..., S[k-1]).
'''
class Solution3(object):
    def scoreOfParentheses(self, S):
        def F(i, j):
            #Score of balanced string S[i:j]
            ans = bal = 0

            #Split string into primitives
            for k in xrange(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i+1, k)
                    i = k+1

            return ans

        return F(0, len(S))

print(Solution().scoreOfParentheses("()")) #1
print(Solution().scoreOfParentheses("(())")) #2
print(Solution().scoreOfParentheses("()()")) #2
print(Solution().scoreOfParentheses("(()(()))")) #6