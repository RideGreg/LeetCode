# Time:  O(n)
# Space: O(1)

# 392
# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from
# the original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# s = "abc", t = "ahbgdc"
# Return true.
#
# Example 2:
# s = "axc", t = "ahbgdc"
# Return false.

# Greedy solution.
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    break
        return i == len(s)

    # 如果有大量输入(10亿)的 S，你需要遍历T串10亿次检查它们是否为 T 的子序列吗？在这种情况有何优化？
    #
    # 这种对同一个长字符串做很多次匹配的 ，可以像KMP算法一样，先用一些时间将长字符串中的数据提取出来，磨刀不误砍柴功。以后就可快速匹配。
    #
    # 前期工作将长字符串研究透彻，设长字符串的长度n，建立一个n * 26 大小的矩阵，表示每个位置上26个字符下一次出现的位置。
    # 在长字符串前要插入一个空位作为初始位。
    # 对于要匹配的短字符串，不断寻找每一个字符在长字符串中的位置，然后将位置更新，寻找下一个字符，相当于在长字符串上“跳跃”。
    # 如果下一个位置为-1，表示长字符串再没有该字符了，返回false即可。
    # Time:  O(n*26), n is the length of long string t
    # Space: O(n*26)
    def isSubsequence_streamInput(self, s: str, t: str) -> bool:
        t = ' ' + t     # 长字符串t前要插入一个空位
        # dp表示每个位置上26个字符下一次出现在t中的位置, 不再出现用-1表示
        dp = [[0] * 26 for _ in range(len(t))]
        for j in range(26):
            nextPos = -1
            for i in reversed(range(len(t))):
                dp[i][j] = nextPos
                if t[i] == chr(ord('a') + j):
                    nextPos = i

        index = 0
        for x in s:
            index = dp[index][ord(x) - ord('a')]
            if index == -1:
                return False
        return True

print(Solution().isSubsequence('abc', 'adbgdc')) # True
