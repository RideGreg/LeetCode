# Time:  O(n^2), KMP O(n)
# Space: O(1), KMP O(n)

# 459
# Given a non-empty string check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
# You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

# KMP solution.


class Solution(object):
    # KMP思想:当出现字符串不匹配时，可以记录一部分之前已经匹配的文本内容，利用这些信息避免从头再去做匹配。
    # 在一个字符串中查询另一个字符串是否出现，可以直接套用 KMP 算法。这里是调用KMP预处理，找到每一位对应的最长公共前后缀。

    # 学习 KMP 算法时，一定要理解其本质。如果放弃阅读晦涩难懂的材料（即使大部分讲解KMP算法的材料都包含大量的图，
    # 但图毕竟只能描述特殊而非一般情况）而是直接去阅读代码，是永远无法学会 KMP 算法的。读者甚至无法理解 KMP 
    # 算法关键代码中的任意一行。
    def repeatedSubstringPattern(self, str):  # USE THIS
        """
        :type str: str
        :rtype: bool
        """
        # prefix[i] = j means pattern[:j+1] prefix (first j chars) is also suffix of pattern[:i+1] (last j chars)
        def preKmp(s):
            prefix = [-1] * len(s)
            j = -1
            for i in range(1, len(s)):
                while j > -1 and s[i] != s[j + 1]:
                    j = prefix[j]
                if s[i] == s[j + 1]:
                    j += 1
                prefix[i] = j
            return prefix

        prefix = preKmp(str)
        # prefix[-1] + 1 最长公共前后缀长度（就是字符串里的前缀子串和后缀子串相同的最长长度）
        # len(str) - prefix[-1] - 1 重复子串长度
        print(prefix)
        return prefix[-1] != -1 and \
               len(str) % (len(str) - prefix[-1] - 1) == 0

    # Enumerate possible substring: Time O(n^2) Space O(1)
    # length of original string n must be divisible by length of substring m, and
    # all remaining chars after 1st substring must match by m difference.
    def repeatedSubstringPattern1(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1): # possible substring length
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False

    # hard to analyze time complexity, since we use library function.
    def repeatedSubstringPattern2(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = str + str
        return ss.find(str, 1, -1) != -1 # find(sub[, star[, end]])

print(Solution().repeatedSubstringPattern("asdfasdfasdf")) # True
# prefix = [-1,-1,-1,-1,0,1,2,3,4,5,6,7]

print(Solution().repeatedSubstringPattern("abcdabxa")) # False
# prefix = [-1,-1,-1,-1,0,1,-1,0]

print(Solution().repeatedSubstringPattern("abcdaxab")) # False
# prefix = [-1,-1,-1,-1,0,-1,0,1]

print(Solution().repeatedSubstringPattern("ABC ABCDAB ABCDABCDABDE")) # False
# prefix = [-1,-1,-1,-1,0,1,2,-1,0,1,-1,0,1,2,-1,0,1,2,-1,0,1,-1,-1]