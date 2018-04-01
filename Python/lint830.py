class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, str):
        import collections
        cnt = collections.Counter(str)
        slist = list(str)
        slist.sort(key=lambda c: (-cnt[c], c))
        return ''.join(slist)

print Solution().stringSort('bloomberg')
print Solution().stringSort('lintcode')
print Solution().stringSort('')