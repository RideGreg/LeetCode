# Time:  O(n)
# Space: O(1)

# Given two strings s1 and s2, write a function to return true
# if s2 contains the permutation of s1. In other words,
# one of the first string's permutations is the substring of the second string.
#
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counts = collections.Counter(s1)
        l = len(s1)
        for i in xrange(len(s2)):
            if counts[s2[i]] > 0:
                l -= 1
            counts[s2[i]] -= 1
            if l == 0:
                return True
            start = i + 1 - len(s1)
            if start >= 0:
                counts[s2[start]] += 1
                if counts[s2[start]] > 0:
                    l += 1
        return False

    def checkInclusion_bookshadow(self, s1, s2):
        import collections
        c1, c2 = collections.Counter(s1), collections.Counter()
        p = 0
        for q in xrange(len(s2)): #evey valid q needs to be added
            c2[s2[q]] += 1
            if q-p+1 < len(s1):
                continue
            elif q-p+1 > len(s1):
                c2[s2[p]] -= 1
                if c2[s2[p]] == 0: del c2[s2[p]]
                p += 1
            if c1 == c2: return True
        return False

print Solution().checkInclusion_bookshadow("ab", "eidbaooo")
print Solution().checkInclusion_bookshadow("adc", "dcda")