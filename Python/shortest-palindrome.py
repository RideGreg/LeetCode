# Time:  O(n)
# Space: O(n)

# 214
# Given a string S, you are allowed to convert it to a palindrome
# by adding characters in front of it. Find and return the shortest
# palindrome you can find by performing this transformation.
#
# For example:
#
# Given "aacecaaa", return "aaacecaaa".
#
# Given "abcd", return "dcbabcd".
#

# KMP Algorithm
# optimized from Solution2
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j > -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        if not s:
            return s

        A = s + '#' + s[::-1]
        return s[getPrefix(A)[-1]+1:][::-1] + s


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j > -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        if not s:
            return s

        A = s + s[::-1]
        prefix = getPrefix(A)
        i = prefix[-1]
        while i >= len(s):
            i = prefix[i]
        return s[i+1:][::-1] + s


# Time:  O(n)
# Space: O(n)
# Manacher's Algorithm
class Solution3(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preProcess(s):
            if not s:
                return ['^', '$']
            string = ['^']
            for c in s:
                string +=  ['#', c]
            string += ['#', '$']
            return string

        string = preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        for i in range(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len = 0
        for i in range(1, len(string) - 1):
            if i - palindrome[i] == 1:
                max_len = palindrome[i]
        return s[len(s)-1:max_len-1:-1] + s

# Brute force: Time O(n^2), Space O(n) for reverse string
#
# Find the longest palindrome from the beginning, then reverse the remaining segment and append to the beginning.
# This must be the required answer as no shorter palindrome could be found than this by just appending at the beginning.
class Solution4(object):
    def shortestPalindrome(self, s):
        rev = s[::-1]
        for i in range(len(s)):
            if s[:len(s)-i] == rev[i:]:
                return rev[:i] + s
        return ''

    # each iteration has to make a new substring
    def shortestPalindrome_TLE(self, s):
        def isPalindrome(s):
            if len(s) < 2:
                return True
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for i in range(len(s)):
            if isPalindrome(s[:len(s) - i]):
                return s[len(s) - i:][::-1] + s
        return ''

print(Solution().shortestPalindrome("abcd")) # "dcbabcd"
print(Solution().shortestPalindrome("aacecaaa")) # "aaacecaaa"
