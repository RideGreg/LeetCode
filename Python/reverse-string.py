# Time:  O(n)
# Space: O(n)

# 344
# Write a function that takes a string as input and
# returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".

# Two common errors for string:
# 1. reverse method is for list only: s.reverse() => AttributeError: 'str' object has no attribute 'reverse'
# 2. s[0] = s[-1] => TypeError: 'str' object does not support item assignment
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i, j = 0, len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
ukjk3cp2