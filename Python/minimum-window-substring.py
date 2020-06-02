# Time:  O(n)
# Space: O(k), k is the number of different characters

# 76 最小覆盖子串
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

        count = 0 # very nice! otherwise have to compare actual vs expected to know all expected
                  # chars were found
        left, min_width, min_left = 0, float("inf"), 0
        for right in range(len(s)):
            id = ord(s[right]) - ord('A')
            actual[id] += 1
            if actual[id] <= expected[id]:
                count += 1

            if count == len(t):
                while actual[ord(s[left]) - ord('A')] > expected[ord(s[left]) - ord('A')]:
                    actual[ord(s[left]) - ord('A')] -= 1
                    left += 1

                if right - left + 1 < min_width:
                    min_width, min_left = right - left + 1, left

        return '' if min_width == float("inf") else s[min_left:min_left + min_width]

print(Solution().minWindow("azzzzbccab", 'abc')) # 'cab'
print(Solution().minWindow("AuOZEaOzEBuNC", "AA")) # ''
print(Solution().minWindow("ADOBECODEBANC", "ABC")) # 'BANC
