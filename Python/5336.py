import collections
from typing import List

class Solution:
    # 5336
    def sortString(self, s: str) -> str:
        freq, ans, forw = [0] * 26, [], True
        for c in s:
            freq[ord(c) - ord('a')] += 1

        while sum(freq):
            seq = range(26) if forw else range(25,-1,-1)
            for i in seq:
                if freq[i]:
                    ans.append(chr(ord('a')+i))
                    freq[i] -= 1
            forw = 1 - forw
        return ''.join(ans)

    # 5337
    def findTheLongestSubstring(self, S):
        vowels, state = 'aeiou', 0
        first, last = {0: -1}, {0: -1}
        for i, c in enumerate(S):
            if c in vowels:
                k = vowels.index(c)
                mask = 1 << k
                state ^= mask
            if state not in first:
                first[state] = i
            last[state] = i
        return max(last[k] - first[k] for k in first)



    def findTheLongestSubstring_awice(self, S): # awice
        vowels = 'aeiou'

        P = [0]
        for c in S:
            if c in vowels:
                i = vowels.index(c)
                mask = 1 << i
                P.append(P[-1] ^ mask)
            else:
                P.append(P[-1])

        first = [None] * 32
        last = [None] * 32
        for i, x in enumerate(P):
            if first[x] is None:
                first[x] = i
            last[x] = i

        ans = 0
        for i in range(32):
            if first[i] is not None:
                ans = max(ans, last[i] - first[i])
        return ans

    def findTheLongestSubstring_ming(self, s: str) -> int: # wrong
        first = collections.defaultdict(lambda : -1)
        cnt = collections.defaultdict(int)
        ans = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                if c not in first:
                    first[c] = i
                cnt[c] += 1
            start = -1
            for k, v in cnt.items():
                if v & 1:
                    start = max(first[k], start) # wrong, all vowels before start are reduced by 1 count
            ans = max(ans, i-start)
        return ans

    def numTimesAllBlue(self, light: List[int]) -> int:
        # status 0,1,2. After change to 1, check left to see if change to 2. After change to 2, check right
        # to see if pass around. Maintain rightmost to see if the moment counts
        n = len(light)
        status, top, ans = [0]*n, -1, 0
        for b in light:
            b = b-1
            status[b] = 1
            if b == 0 or status[b-1] == 2:
                status[b] = 2
                while b+1 < n and status[b+1] == 1:
                    status[b+1] = 2
                    b += 1
            top = max(top, b)
            if status[top] == 2:
                ans += 1
        return ans

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub = collections.defaultdict(list)
        for i in range(len(manager)):
            sub[manager[i]].append(i)
        ans = 0
        stk = [(headID, 0)]
        while stk:
            cur, t = stk.pop()
            if cur not in sub:
                ans = max(ans, t)
                continue
            for i in sub[cur]:
                stk.append((i, t+informTime[cur]))
        return ans

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        conn = collections.defaultdict(list)
        for x, y in edges:
            conn[x].append(y)
            conn[y].append(x)
        dp, seen = {1:1.0}, set([1])
        while t:
            ndp = {}
            for i, p in dp.items():
                nxt = [j for j in conn[i] if j not in seen]
                if not nxt:
                    ndp[i] = p
                else:
                    for j in nxt:
                        ndp[j] = p * (1.0/len(nxt))
                        seen.add(j)
            t -= 1
            dp = ndp
        return dp.get(target, 0.0)


    def a1(self, marix):

        ans, m, n = [], len(matrix), len(matrix[0])
        cols = [0] * n
        for j in range(n):
            cols[j] = max(matrix[i][j] for i in range(m))

        for i in range(m):
            cand = min(matrix[i])
            for j in range(n):
                if matrix[i][j] == cand and cols[j] == cand:
                    ans.append(cand)
        return ans

    def maxPerformance(self, n, speed, efficiency, k):
        import heapq
        MOD = 10**9 + 7
        es = zip(efficiency, speed)
        es = sorted(es, reverse=True)
        slist = [es[0][1]]
        heapq.heapify(slist)
        stotal = sum(slist)
        ans = stotal * es[0][0]
        for e,s in es[1:]: #range(k-1, len(es)):
            heapq.heappush(slist, s)
            stotal += s
            if len(slist) > k:
                stotal -= heapq.heappop(slist)
            ans = max(ans, stotal* e)
        return ans % MOD

print(Solution().maxPerformance(3, [2,8,2], [2,7,1], 2))
print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))
print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3))
print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4))

print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))

print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7))

'''
print(Solution().numOfMinutes(1, 0, [-1], [0]))
print(Solution().numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
print(Solution().numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]))
print(Solution().numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
print(Solution().numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914]))

print(Solution().numTimesAllBlue( [2,1,3,5,4]))
print(Solution().numTimesAllBlue([3,2,4,1,5]))
print(Solution().numTimesAllBlue([4,1,2,3]))
print(Solution().numTimesAllBlue([2,1,4,3,6,5]))
print(Solution().numTimesAllBlue( [1,2,3,4,5,6]))

print(Solution().findTheLongestSubstring('bcbcbc')) # 6
print(Solution().findTheLongestSubstring('eleetminicoworoep')) # 13
print(Solution().findTheLongestSubstring('leetcodeisgreat')) # 5
print(Solution().findTheLongestSubstring("jszhctibantjpnnzcfgyvbuynnllqefzhhzblcokghiewwqmdpvxztapjiyzwjgzewumvbzymoraehpudjwtngqkdhhpsdfplwututnmrnyaumenebjmtnudgtiptniqydkzerwrzivvarvxdyloiydjezcnwmapsxeyyrmpzyhqamzbntchvbocjtblybccbsjljcrptlkyfulqhkthhuywgjjrkwjsavpivzhehfcim"))
# 194

print(Solution().sortString('aaaabbbbcccc'))
print(Solution().sortString('rat'))
print(Solution().sortString('leetcode'))
print(Solution().sortString('ggggggg'))
#print(Solution().sortString())
'''