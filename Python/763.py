class Solution(object):
    def partitionLabels(self, S):
        letterSet, ans = {}, []
        for i, c in enumerate(S):
            if c not in letterSet:
                letterSet[c] = [i, i]
            else:
                letterSet[c][1] = i
        print letterSet
        origStart, start = 0, 0
        cont = False
        while start < len(S):
            if not cont:
                end = letterSet[S[start]][1]
                endNew = end
            for i in xrange(start, end+1):
                endNew = max(endNew, letterSet[S[i]][1])
            if endNew <= end:
                cont = False
                ans.append(end-origStart+1)
                origStart, start = end+1, end+1
            else:
                start = end+1
                end = endNew
                cont = True
        return ans


print Solution().partitionLabels("ababcbacadefegdehijhklij")
print Solution().partitionLabels("acabcbadefgdehijiiklij")
