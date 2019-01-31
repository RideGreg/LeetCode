# Time:  O(n), n is the length of 'typed'
# Space: O(1)

# 925
# Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
#
# You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true

# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

# Example 3:
# Input: name = "leelee", typed = "lleeelee"
# Output: true

# Example 4:
# Input: name = "laiden", typed = "laiden"
# Output: true

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        for c in typed:
            if i < len(name) and c == name[i]:
                i += 1
            elif i == 0 or c != name[i-1]:
                return False
        return i == len(name)

print(Solution().isLongPressedName('ac', 'abc')) # False
