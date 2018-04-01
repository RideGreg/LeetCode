class Solution:
    """
    @param a: The a tuple
    @param b: The b tuple
    @param c: the c tuple
    @param d: the d tuple
    @return: The answer
    """
    def withinThreeJumps(self, a, b, c, d):
        import collections
        fri = collections.defaultdict(set)
        for i in xrange(len(a)):
            fri[a[i]].add(b[i])
            fri[b[i]].add(a[i])
        ans = []
        for i in xrange(len(c)):
            q = collections.deque([c[i]])
            visited = [c[i]]
            q.append('#')
            jump = 0
            toAdd = 0
            while q and jump <= 3:
                cur = q.popleft()
                if cur == d[i]:
                    toAdd = 1
                    break
                if cur == '#' and q:
                    jump += 1
                    q.append('#')
                    continue
                for f in fri[cur]:
                    if f not in visited:
                        q.append(f)
                        visited.append(f)
            ans.append(toAdd)
        return ans

print Solution().withinThreeJumps([1,2,3,4],[2,3,4,5],[1,1],[4,5])
print Solution().withinThreeJumps([1,2],[2,3],[1],[3])
