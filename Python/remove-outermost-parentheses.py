# Time:  O(n)
# Space: O(1)

# 1021
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid
# parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and
# "(()(()))" are all valid parentheses strings.
#
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to
# split it into S = A+B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
# where P_i are primitive valid parentheses strings.
#
# Return S after removing the outermost parentheses of every primitive string in the primitive
# decomposition of S.

class Solution(object):
    # count the number of opened parenthesis.
    # Add every char to the result, unless the first left parenthesis,
    # and the last right parenthesis.
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        deep = 1   # EXTENDABLE to remove 2 or 3 ... layers of outer parentheses
        res, opened = [], 0
        for c in S:
            if c == '(' and opened >= deep:
                res.append(c)
            if c == ')' and opened > deep:
                res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)

    # add primitive as a chunk, but hard to know how many layers the substring has.
    def removeOuterParentheses_ming(self, S: str) -> str:
        s, opened, ans = 1, 0, []
        for e in range(len(S)):
            opened += 1 if S[e]=='(' else -1
            if opened == 0:
                ans.append(S[s:e])
                s = e+2
        return ''.join(ans)

print(Solution().removeOuterParentheses("(()())(())")) # "()()()"
print(Solution().removeOuterParentheses("(()())(())(()(()))")) # "()()()()(())"
print(Solution().removeOuterParentheses("()()")) # ''