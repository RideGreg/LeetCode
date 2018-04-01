class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        def myCmp(t1, t2):
            if len(t1[0]) > len(t2[0]): return -1
            elif len(t1[0]) < len(t2[0]): return 1
            else: return 0

        re = zip(a, b)
        re.sort(cmp=myCmp)

        ans, i = '', 0
        while i < len(s):
            oldi = i
            for s1, s2 in re:
                if s[i:i+len(s1)] == s1:
                    ans += s2
                    i += len(s1)
                    break
            if oldi == i:
                ans += s[i]
                i += 1
        return ans

print Solution().stringReplace(["ab","aba"], ["cc","ccc"], 'ababa')
print Solution().stringReplace(["ab","aba"], ["cc","ccc"], 'aaaaa')

print Solution().stringReplace(["ab","aba"], ["cc","ccc"], 'dababa')