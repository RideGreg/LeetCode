# Time:  O(n)
# Space: O(1)

# 567
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

import collections


class Solution(object):
    def checkInclusion(self, s1, s2): # USE THIS 滑动窗口
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnt = collections.Counter(s1)
        left = 0
        for right, c in enumerate(s2):
            cnt[c] -= 1
            # 此字符出现太多，缩小窗口直到多余字符被去掉
            while cnt[c] < 0 and left <= right:
                cnt[s2[left]] += 1
                left += 1

            if right-left+1 == len(s1):
                return True
        return False

    # maintain the # of chars matched 'l' is a little complex and not needed in first solution
    def checkInclusion_kamyu(self, s1, s2):
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

    # 其它解法：1 暴力：生成短字符串的所有排列，并检查生成的排列是否是较长字符串的子字符串 Time O(l1!) l1 is length of s1
    # 2 排序：对短字符串s1和 s2的所有子串进行排序，并比较 Time O(l1logl1 + (l2-l1)l1log(l1))
    # 3 hash：对短字符串s1和 s2的所有子串比较字符出现频率 Time O(l1 + (l2-l1)*26*l1) l1 time used to get char frequency
    # 4 array: similar to 3, use array rather than hash to store char frequencies. Time same as 3