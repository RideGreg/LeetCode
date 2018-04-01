import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = (len(S)+1)//2
        d = collections.defaultdict(int)
        for c in S:
            d[c] += 1
        m = max(d.values())
        if m > l: return ''

        ans, pm = '1'*len(S), 0
        for i in reversed(xrange(1,m+1)):
            for k, v in d.iteritems():
                if v == i:
                    for _ in xrange(v):
                        while ans[pm] != '1':
                            pm += 1
                        ans = ans[:pm] + k + ans[pm+1:]
                        pm += 2
                        if pm >= len(S): pm = 0
                    print ans
        return ans

#print Solution().reorganizeString("tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao")
print Solution().reorganizeString("wawwivhwfrgontvvfggh") #brbsf
print Solution().reorganizeString("bfrbs") #brbsf
print Solution().reorganizeString("zifrfbctby") #bcbifrftyz
print Solution().reorganizeString("zhmyo") #zhmyo
print Solution().reorganizeString("abbabbaaab") #ababababab

