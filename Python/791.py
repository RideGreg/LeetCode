class Solution(object):
    def customSortString(self, S, T):
        import collections
        chars = collections.Counter(T)
        ans = ''
        for c in S:
            if c in chars:
                ans += c*chars[c]
                del chars[c]
        for c, i in chars.iteritems():
            ans += c*i
        return ans

print Solution().customSortString('cba', 'abcd')