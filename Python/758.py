class Solution(object):
    def boldWords(self, words, S):
        words.sort(key = len, reverse = True)
        hit = [0] * (len(S)+2)
        for i in xrange(len(S)):
            for w in words:
                if S.startswith(w, i):
                    hit[i+1] += 1
                    hit[i+1+len(w)] -= 1
                    break
        for i in xrange(len(hit)-1):
            hit[i+1] += hit[i]
        ans = ''
        for i in xrange(len(hit)-1):
            if i>0:
                ans += S[i-1]
            if hit[i] == 0 and hit[i+1] > 0:
                ans += "<b>"
            elif hit[i] > 0 and hit[i+1] == 0:
                ans += "</b>"
        return ans

print Solution().boldWords(["ab", "bc"], "aabcd")
print Solution().boldWords(["ccb","b","d","cba","dc"], "eeaadadadc")