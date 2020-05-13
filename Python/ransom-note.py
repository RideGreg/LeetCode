# Time:  O(n)
# Space: O(1)

# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if
# the ransom  note can be constructed from the magazines ;
# otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

# 考察重复元素集合的关系
# 所以set不能用，那就使用collection.Counter，它也有一部分集合运算功能
# 判断标准：在ransomNote中不存在比magazine多的元素

import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        avail = collections.Counter(magazine)
        for c in ransomNote:
            if avail[c] < 1:
                return False
            avail[c] -= 1
        return True

    def canConstruct2(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        # >>> cr=collections.Counter(‘aa')
        # Counter({'a': 2})
        # >>> cm=collections.Counter('ab')
        # Counter({'a': 1, 'b': 1})
        # >>> cm+cr
        # Counter({'a': 3, 'b': 1})
        # >>> cr-cm
        # Counter({'a': 1}) subtract keeping only positive counts
        # >>> cm-cr
        # Counter({'b': 1}) subtract keeping only positive counts
        # >>> cm&cr
        # Counter({'a': 1}) intersection:  min(c[x], d[x])
        # >>> cm|cr
        # Counter({'a': 2, 'b': 1}) union:  max(c[x], d[x])

    def canConstruct_list(self, ransomNote, magazine):
        # 对于key明确且有限的情况，可以使用list代替dict统计字符数。代码冗长
        counts = [0] * 26
        letters = 0

        for c in ransomNote:
            if counts[ord(c) - ord('a')] == 0:
                letters += 1
            counts[ord(c) - ord('a')] += 1

        for c in magazine:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] == 0:
                letters -= 1
                if letters == 0:
                    break

        return letters == 0

print(Solution().canConstruct('a', 'b')) # False
print(Solution().canConstruct('aa', 'ab')) # False
print(Solution().canConstruct('aa', 'aab')) # True