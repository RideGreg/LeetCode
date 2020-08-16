# Time:  O(C(n, c)), try out all possible substrings with the minimum c deletion.
# Space: O(c), the depth is at most c, and it costs n at each depth
# 301
# Remove the minimum number of invalid parentheses in order to
# make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the
# parentheses ( and ).
#
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
#

# DFS solution.
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Calculate the minimum left and right parantheses to remove
        def findMinRemove(s):
            left_remove = right_remove = 0
            for c in s:
                if c == '(':
                    left_remove += 1
                elif c == ')':
                    if not left_remove:
                        right_remove += 1
                    else:
                        left_remove -= 1
            return (left_remove, right_remove)

        # Check whether s is valid or not.
        def isValid(s):
            sum = 0
            for c in s:
                if c == '(':
                    sum += 1
                elif c == ')':
                    sum -= 1
                if sum < 0:
                    return False
            return sum == 0

        # start is current index, left_remove/right_remove track status
        def dfs(start, left_remove, right_remove):
            if left_remove == right_remove == 0:
                tmp = [c for i, c in enumerate(s) if i not in removed]
                tmp = ''.join(tmp)
                if isValid(tmp):    # KENG!! possibly deletion is not in correct place ")()" => ")("
                    res.append(tmp)
                return

            for i in range(start, len(s)):
                if i == start or s[i] != s[i - 1]:  # Skip duplicated, because it produces a same result.
                                                    # NOTE: not i == 0!!!
                    # Trimming: only remove ')' when right_remove==0, otherwise if right_remove > 0,
                    # there always')' later to match this ')'
                    if right_remove == 0 and left_remove > 0 and s[i] == '(':
                        removed.add(i)
                        dfs(i + 1, left_remove - 1, right_remove)
                        removed.discard(i)
                    elif right_remove > 0 and s[i] == ')':
                        removed.add(i)
                        dfs(i + 1, left_remove, right_remove - 1)
                        removed.discard(i)

        res, removed = [], set() # set is faster to query than list
        (left_remove, right_remove) = findMinRemove(s)
        dfs(0, left_remove, right_remove)
        return res

print(Solution().removeInvalidParentheses("))")) # [""]
print(Solution().removeInvalidParentheses("())(")) # ["()"]
print(Solution().removeInvalidParentheses("(a)(b))()")) # ["(a)(b)()", "(a(b))()"]
print(Solution().removeInvalidParentheses(")()")) # ["()"]
print(Solution().removeInvalidParentheses(")(")) # [""]
