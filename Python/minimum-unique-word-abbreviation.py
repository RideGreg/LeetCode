# Time:  O(n * 2^n)
# Space: O(n)

# 411
# A string such as "word" contains the following abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, find an abbreviation
# of this target string with the smallest possible length such that it does not
# conflict with abbreviations of the strings in the dictionary.
#
# Each number or letter in the abbreviation is considered length = 1. For example,
# the abbreviation "a32bc" has length = 4.
#
# Note:
# In the case of multiple answers as shown in the second example below, you may return any one of them.
# Assume length of target string = m, and dictionary size = n. You may assume
# that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.

# Example
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include
# "ap3", "a3e", "2p2", "3le", "3l1").

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def bits_to_abbr(targets, bits):
            abbr = []
            pre = 0
            for i in xrange(len(target)):
                if bits & 1:
                    if i - pre > 0:
                        abbr.append(str(i - pre))
                    pre = i + 1
                    abbr.append(str(target[i]))
                elif i == len(target) - 1:
                    abbr.append(str(i - pre + 1))
                bits >>= 1
            return abbr
  
        diffs = []
        for word in dictionary:
            if len(word) != len(target):
                continue
            diffs.append(sum(2**i for i, c in enumerate(word) if target[i] != c))

        if not diffs:
            return str(len(target))

        result = list(target)
        for mask in xrange(2**len(target)):
            abbr = bits_to_abbr(target, mask)
            if all(d & mask for d in diffs) and len(abbr) < len(result):
                result = abbr
        return "".join(result)
