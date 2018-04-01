class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        import collections
        ks,vs = [], []
        for str in strs:
            chars = collections.Counter(str)
            k = tuple(sorted(chars.items()))
            if k not in ks:
                ks.append(k)
                vs.append([str])
            else:
                vs[ks.index(k)].append(str)
        return vs

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

