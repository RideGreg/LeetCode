# Time:  O(n)
# Space: O(1)
#
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#

class Solution(object): # double scan, maintain counter
    def longestValidParentheses(self, s): # USE THIS: double scan
        """
        :type s: str
        :rtype: int
        """
        def length(start, openChar, reverse):
            it = range(len(s))
            if reverse: it = reversed(it)
            depth, ans = 0, 0
            for i in it:
                if s[i] == openChar:
                    depth += 1
                else:
                    depth -= 1
                    if depth < 0:
                        start, depth = i, 0 # reset
                    elif depth == 0:
                        longest = max(ans, abs(i - start))
            return ans

        return max(length(-1, '(', False), length(len(s), ')', True))


    def longestValidParentheses_doubleScan2(self, s):
        ans = 0
        # forward scan
        open = close = 0
        for c in s:
            if c == '(':
                open += 1
            else:
                close += 1
                if close == open:
                    ans = max(ans, 2 * open)
                elif close > open:
                    open = close = 0

        # backward scan
        open = close = 0
        for c in reversed(s):
            if c == '(':
                open += 1
                if close == open:
                    ans = max(ans, 2 * open)
                elif open > close:
                    open = close = 0
            else:
                close += 1
        return ans

# Time:  O(n)
# Space: O(n), store the indices of opening char
class Solution2: # stack
    def longestValidParentheses(self, s):
        ans, stack = 0, [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop() # pop a '('
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    stack.append(i)
        return ans

# solution 3: O(n^2) DP also works

if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()")) # 2
    print(Solution().longestValidParentheses("(()))")) # 4
    print(Solution().longestValidParentheses(")()())")) # 4
