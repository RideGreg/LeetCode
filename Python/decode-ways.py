# Time:  O(n)
# Space: O(1)
#
# 91
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre = 1
        for i in range(len(s)):
            cur = 0
            if '1' <= s[i] <= '9':
                cur += pre
            if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
                cur += ppre
            if cur == 0:
                return 0

            ppre, pre = pre, cur
        return cur

if __name__ == "__main__":
    for i in ["0", "10", "10", "103", "1032", "10323"]:
        print(Solution().numDecodings(i)) # 0 1 1 1 1 2
