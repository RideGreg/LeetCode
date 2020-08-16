# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
#


# stack with 2 optimizations
# Have to use stack to remember order of parentheses,
# The method using counters of opening/closing parentheses doesn't work due to different parentheses types
class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) % 2: return False        # optimization #1

        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
                if len(stack) > len(s) // 2:       # optimization #2
                    return False

            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")