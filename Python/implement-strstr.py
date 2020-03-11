# Time:  O(n + k)
# Space: O(k)

# 28
# Implement strStr().
#
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
#

# Wiki of KMP algorithm:
# http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        return self.KMP(haystack, needle)

    # https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
    # whenever we detect a mismatch (after some matches), we know some chars match for sure and skip compare them.
    # the above prefix array store number of chars. Code below stores index of prefix.
    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        for i in range(len(text)):
            while j > -1 and pattern[j + 1] != text[i]: # mismatch, back to use prefix which guaranteed skipable
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1

    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern) # prefix[i] = j means pattern[:j+1] prefix is also suffix of pattern[:i+1]
        j = -1
        for i in range(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]: # cannot extend
                j = prefix[j]
            if pattern[j + 1] == pattern[i]: # extend number of chars which are both prefix and suffix
                j += 1
            prefix[i] = j
        return prefix


# Time:  O(n * k)
# Space: O(k)
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    # debug KMP algorithm
    print(Solution().strStr("AAAAABAAABA", "AAAA")) # prefix [-1,0,1,2]
    print(Solution().strStr("abababcdab", "ababab")) # prefix [-1,-1,0,1,2,3]
    print(Solution().strStr("abababcdab", "abcd")) # prefix [-1,-1,-1,-1]
    print(Solution().strStr("abababcdab", "abab"))  # prefix [-1,-1,0,1]
    print(Solution().strStr("abababcdab", "abcdabc")) # prefix [-1,-1,-1,-1,0,1,2]
    print(Solution().strStr("a", ""))
    print(Solution().strStr("abababcdab", "abcacba")) # prefix [-1,-1,-1,0,-1,-1,0]
    print(Solution().strStr("abababcdab", "abcaac")) # prefix [-1,-1,-1,0,0,-1]
    print(Solution().strStr("abababcdab", "abbcc")) # prefix [-1,-1,-1,-1,-1]
    print(Solution().strStr("abababcdab", "ababcdx")) # prefix [-1,-1,0,1,-1,-1,-1]
