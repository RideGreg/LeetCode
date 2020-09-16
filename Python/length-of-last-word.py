# Time:  O(n)
# Space: O(1)

# 58
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
#

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s: str) -> int: # USE THIS
        r = len(s) - 1
        while r >= 0 and s[r] == ' ':
            r -= 1
        l = r
        while l >= 0 and s[l] != ' ':
            l -= 1
        return r - l


    def lengthOfLastWord(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length

# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])

print(Solution().lengthOfLastWord("Hello World")) # 5
print(Solution2().lengthOfLastWord("")) # 0
