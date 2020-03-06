# Time:  O(n)
# Space: O(1)

# 1328 biweekly contest 18 1/25/2020

# Given a palindromic string palindrome, replace exactly one character by any lowercase English letter
# so that the string becomes the lexicographically smallest possible string that isn't a palindrome.
#
# After doing so, return the final string.  If there is no way to do so, return the empty string.

# 1 <= palindrome.length <= 1000

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        s = palindrome
        l = len(s)
        if l == 1: return ''
        # use the fact it is palindrome, so first half same as second half
        if all(c == 'a' for c in s[:l // 2]):
            return s[:-1] + 'b'

        for i in range(l//2):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i + 1:]

    def breakPalindrome_kamyu(self, palindrome):
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b' if len(palindrome) >= 2 else ""

print(Solution().breakPalindrome("abccba")) # "aaccba"
print(Solution().breakPalindrome("abba")) # 'aaba'
print(Solution().breakPalindrome("a")) # ""
print(Solution().breakPalindrome("aa")) # 'ab'
print(Solution().breakPalindrome("aaa")) # 'aab'
print(Solution().breakPalindrome("aaaa")) # 'aaab'
print(Solution().breakPalindrome("bb")) # 'ab'