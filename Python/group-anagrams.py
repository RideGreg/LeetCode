# Time:  O(n * glogg), g is the max length of a string in input.
# Space: O(n * g)
#
# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#

import collections


class Solution(object):
    def groupAnagrams_noSort(self, strs): # USE THIS: better O(n * g)
        ans = collections.defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            ans[tuple(cnt)].append(s)
        return list(ans.values())

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = collections.defaultdict(list)
        for s in strs:
            sorted_str = ("").join(sorted(s))
            anagrams_map[sorted_str].append(s)
        return list(anagrams_map.values())


print(Solution().groupAnagrams(["cat", "dog", "act", "mac"]))
# [['cat', 'act'], ['dog'], ['mac']]
