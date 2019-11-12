# Time:  O(n)
# Space: O(k), k is the number of different characters

# 76
# Given a string S and a string T, find the minimum window in S which
# will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T,
# return the emtpy string "".
#
# If there are multiple such windows, you are guaranteed that
# there will always be only one unique minimum window in S.

class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        actual, expected = collections.defaultdict(int), collections.defaultdict(int)
        for c in t:
            expected[c] += 1
        l, total, minStart, minWid = 0, 0, 0, float('inf')
        for r, c in enumerate(s):
            actual[c] += 1
            if actual[c] <= expected[c]:
                total += 1

            if total == len(t):
                while actual[s[l]] > expected[s[l]]:
                    actual[s[l]] -= 1
                    l += 1

                if minWid > r - l + 1:
                    minStart, minWid = l, r - l + 1
        return s[minStart:minStart + minWid] if minWid != float('inf') else ''


    def minWindow_kamyu(self, s, t):
        actual = [0] * 58 # from A(65) to z(122)
        expected = [0] * 58
        for char in t:
            expected[ord(char) - ord('A')] += 1

        count, start, min_width, min_start = 0, 0, float("inf"), 0
        for i in range(len(s)):
            actual[ord(s[i]) - ord('A')] += 1
            if actual[ord(s[i]) - ord('A')] <= expected[ord(s[i]) - ord('A')]:
                count += 1

            if count == len(t):
                while actual[ord(s[start]) - ord('A')] > expected[ord(s[start]) - ord('A')]:
                    actual[ord(s[start]) - ord('A')] -= 1
                    start += 1

                if min_width > i - start + 1:
                    min_width = i - start + 1
                    min_start = start

        if min_width == float("inf"):
            return ""
        return s[min_start:min_start + min_width]

print(Solution().minWindow("azzzzbccab", 'abc')) # 'cab'
print(Solution().minWindow("AuOZEaOzEBuNC", "AA")) # ''
print(Solution().minWindow("ADOBECODEBANC", "ABC")) # 'BANC
