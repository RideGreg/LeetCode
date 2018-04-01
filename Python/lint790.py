import collections
class Solution:
    def canBeGenerated(self, generator, startSymbol, symbolString):
        lookup = collections.defaultdict(list)
        for r in generator:
            lookup[r[0]].append(r[5:])
        print lookup
        q = collections.deque([startSymbol])
        used = {}
        while q:
            cur = q.popleft()
            if cur == symbolString:
                return True
            used[cur] = True
            if len(cur) > symbolString: continue
            for i, c in enumerate(cur):
                if c in lookup:
                    for s in lookup[c]:
                        mod = cur[:i]+s+cur[i+1:]
                        if mod not in used:
                            q.append(mod)
        return False

print Solution().canBeGenerated(["S -> abc", "S -> aA", "A -> b", "A -> c"], 'S', 'ac')