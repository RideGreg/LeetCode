class Solution(object):
    def minWindow(self, S, T):
        '''
        print "\n"
        def isSubSeq(SS, T):
            lenSS, lenT = len(SS), len(T)
            i, j = 0, 0
            while i < lenSS and j < lenT:
                if SS[i] == T[j]:
                    j += 1
                i += 1
            return j == lenT

        ans, ans_len, length = '', float('inf'), len(S)
        for i in xrange(length):
            for j in xrange(i+1, length+1):
                if j-i < ans_len and isSubSeq(S[i:j], T):
                    ans_len = j-i
                    ans = S[i:j]
                    print ans
                    break
        return ans
        '''

        cur = [i if x == T[0] else None for i, x in enumerate(S)]
        print cur
        for j in xrange(1, len(T)):
            last = None
            new = [None] * len(S)
            for i, u in enumerate(S):
                if last is not None and u == T[j]:
                    new[i] = last
                if cur[i] is not None:
                    last = cur[i]
            cur = new

        ans = 0, len(S)
        print ans
        for e, s in enumerate(cur):
            if s >= 0 and e - s < ans[1] - ans[0]:
                ans = s, e
        return S[ans[0]: ans[1]+1] if ans[1] < len(S) else ""
print Solution().minWindow("abcdebdde", "bde")
print Solution().minWindow("abccdebdde", "bde")