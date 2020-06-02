# Time:  O(n)
# Space: O(1)

# 438 找到字符串中所有字母异位词
# Given a string s and a non-empty string p, find all the start indices
# of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of
# both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

import collections
class Solution(object):
    # 滑动窗口 sliding window
    # 维持不出现多余元素，仅需检查窗口长度，快！
    def findAnagrams(self, s, p): # USE THIS
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need = collections.Counter(p)
        l, ans = 0, []
        for r in range(len(s)):
            c = s[r]
            need[c] -= 1
            #  此字符出现太多，缩小窗口直到多余字符被去掉
            while l <= r and need[c] < 0:
                need[s[l]] += 1
                l += 1

            if r-l+1 == len(p):
                ans.append(l)
        return ans

    def findAnagrams_leetcodeCNOfficial(self, s, p): # not good as above: 1. compute list index
                                                     # while loop not concise as for loop
        result = []
        cnts = [0] * 26
        for c in p:
            cnts[ord(c) - ord('a')] += 1

        left, right = 0, 0
        while right < len(s):
            rightId = ord(s[right]) - ord('a')
            cnts[rightId] -= 1
            while cnts[rightId] < 0 and left <= right:
                cnts[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1

        return result

    # 维持固定窗口长度，每次需检查窗口内元素count O(n*26)
    # 比暴力稍好。暴力是对每个窗口进行子串匹配 O(n*m) m is the length of pattern string
    def findAnagrams_hash(self, s, p):
        import collections
        cnt, ans = collections.Counter(p), []
        for i in range(len(s)):
            if s[i] in cnt:
                cnt[s[i]] -= 1
            if i >= len(p) and s[i-len(p)] in cnt:
                cnt[s[i-len(p)]] += 1

            if all(x == 0 for x in cnt.values()): # undesired, even this step is constant time
                ans.append(i-len(p)+1)
        return ans

print(Solution().findAnagrams("ababc", "ab")) # [0,1,2]