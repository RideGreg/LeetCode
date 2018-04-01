class Solution(object):
    def expressiveWords(self, S, words):
        def foo(a, b):
            sa = sb = 0
            ea = eb = 1
            while sa < len(a) and sb < len(b):
                if a[sa] != b[sb]: return False

                while ea < len(a) and a[ea] == a[sa]:
                    ea += 1
                while eb < len(b) and b[eb] == b[sb]:
                    eb += 1
                c, d = a[sa:ea], b[sb: eb]
                if c[0] == d[0] and \
                    (len(c)==len(d) or (len(c)>len(d) and len(c)>=3)):
                    sa, sb = ea, eb
                    ea, eb = sa+1, sb+1
                else:
                    return False

            return True if sa==len(a) and sb==len(b) else False

        return sum([foo(S, w) for w in words])

print Solution().expressiveWords('heeeellooo', ["hello", "hi", "helo", "helllo", "helloooo"])
