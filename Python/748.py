class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        target, need, ans = {}, 0, ''
        for c in licensePlate:
            if c >= 'A' and c<= 'z':
                if c.lower() not in target:
                    target[c.lower()] = 0
                target[c.lower()] += 1
                need += 1
        for w in words:
            if not ans or len(w) < len(ans):
                source, found = {}, 0
                for d in w:
                    if d in target and (d not in source or source[d]<target[d]):
                        found += 1
                        if found == need:
                            ans = w
                            break

                        if d not in source:
                            source[d] = 1
                        else:
                            source[d] += 1
        return ans

print Solution().shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])
print Solution().shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])