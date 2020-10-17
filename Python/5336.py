import collections, bisect
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


    # 5435
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        import heapq
        g = collections.defaultdict(list)
        in_deg, out_deg = [0]*n, [0]*n
        for x, y in dependencies:
            g[x-1].append(y-1)
            out_deg[x-1] += 1
            in_deg[y-1] += 1
        pq = [(-out_deg[i], i) for i in range(n) if not in_deg[i]] # minHeap of (out_degree, node)

        level, cnt, seen = 0, 0, 0
        while pq:
            npq = []
            level += 1
            while pq:
                if cnt != k:
                    _, u = heapq.heappop(pq)
                    seen += 1
                    cnt += 1
                    for v in g[u]:
                        in_deg[v] -= 1
                        if not in_deg[v]:
                            heapq.heappush(npq, (-out_deg[v], v))
                else:
                    npq.extend(pq)
                    break

            pq = npq
            cnt = 0

        return level if seen == n else -1

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            if x*2 > target: break
            j = bisect.bisect(nums, target-x) - 1
            ans += 2**(j-i)
            ans %= (10**9+7)
        return ans
    def findMaxValueOfEquation_ming(self, points: List[List[int]], k: int) -> int:
        xs = [x for x, _ in points]
        ans = float('-inf')
        x1 = y1 = x2 = y2 = oldx2 = oldy2 = idx = None
        if points[1][0]- points[0][0] <= k:
            x1, y1 = points[0]
            x2, y2 = points[1]
            ans = y2+y1+x2-x1
        for i, (nx, ny) in enumerate(points):
            if i < 2: continue
            if x2 is not None:
                oldx2, oldy2 = x2, y2
                if ny+nx-y2-x2 > 0:
                    if nx-x1 <= k:
                        x2, y2 = nx, ny
                        ans = y2+y1+x2-x1
                    else:
                        pos = bisect.bisect_left(xs, nx-k)
                        for j in range(pos, i):
                            if nx+ny+points[j][1]-points[j][0] > ans:
                                x1, y1, x2, y2, idx = points[j][0], points[j][1], nx, ny, j
                                ans = y2 + y1 + x2 - x1

            if oldx2 is not None and nx-oldx2 <= k and nx+ny+oldy2-oldx2 > ans:
                x1, y1, x2, y2 = oldx2, oldy2, nx, ny
                ans = y2 + y1 + x2 - x1
            if nx-points[i-1][0] <= k and nx+ny+points[i-1][1]-points[i-1][0] > ans:
                x1, y1, x2, y2, idx = points[i-1][0], points[i-1][1], nx, ny, i-1
                ans = y2 + y1 + x2 - x1
        return ans

    def findMaxValueOfEquation(self, A, K):
        N = len(A)
        i = 0
        mq = Monoqueue()
        ans = float('-inf')
        for j in range(N):
            while i <= j and A[j][0] - A[i][0] > K:
                mq.dequeue()
                i += 1

            M = mq.max()
            if M is not None:
                cand = M + A[j][0] + A[j][1]
                if cand > ans: ans = cand

            mq.enqueue(A[j][1] - A[j][0])
        return ans

    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n, ans = len(mat), len(mat[0]), 0
        dp = [[(0,0)]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if mat[i-1][j-1] == 1:
                    dp[i][j] = (1+dp[i][j-1][0], 1+dp[i-1][j][1])
                    vmin = float('inf')
                    for k in range(dp[i][j][0]):
                        vmin = min(vmin, dp[i][j-k][1])
                        ans += vmin
        return ans


class Monoqueue(collections.deque):
    def enqueue(self, val):
        count = 1
        while self and self[-1][0] < val:
            count += self.pop()[1]
        self.append([val, count])

    def dequeue(self):
        ans = self.max()
        self[0][1] -= 1
        if self[0][1] <= 0:
            self.popleft()
        return ans

    def max(self):
        return self[0][0] if self else None

print(Solution().numSubmat([[1,0,1],[0,1,0],[1,0,1]])) # 5
print(Solution().numSubmat([
              [1,0,1],
              [1,1,0],
              [1,1,0]])) # 13
print(Solution().numSubmat(
    [[0,1,1,0],
     [0,1,1,1],
     [1,1,1,0]]
)) # 24
print(Solution().numSubmat([[1,1,1,1,1,1]])) # 21


'''
print(Solution().findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1))  # 4
print(Solution().findMaxValueOfEquation([[0, 0], [3, 0], [9, 2]], 3))  # 3
print(Solution().findMaxValueOfEquation(
    [[-19, 1], [-18, -13], [-17, -12], [-14, -14], [-8, -9], [-6, 16], [-2, -4], [2, 15], [4, 19], [5, -9], [6, 20],
     [7, -17], [16, 3]],
    5
))  # 41 not 39
print(Solution().findMaxValueOfEquation(
[[-999,-512],[-984,-1878],[-976,-4786],[-962,-1885],[-958,-1057],[-927,-644],[-922,-369],[-898,-2415],[-896,-745],
 [-892,-147],[-891,-1846],[-890,-2903],[-877,-4357],[-860,-3171],[-855,-3055],[-842,-3601],[-825,-1776],[-823,-1603],
 [-780,-1316],[-770,-2291],[-758,-2010],[-754,-186],[-748,-1416],[-744,-2042],[-739,-501],[-731,-4516],[-702,-1822],
 [-678,-3800],[-672,-1363],[-666,-3885],[-656,-1028],[-646,-1791],[-625,-572],[-624,-3218],[-611,-3702],[-605,-107],
 [-576,-3075],[-575,-828],[-568,-4066],[-565,-298],[-562,-1934],[-551,-977],[-515,-1690],[-504,-2379],[-500,-2104],
 [-487,-2545],[-481,-4604],[-472,-1488],[-456,-3193],[-442,-281],[-429,-4995],[-417,-2971],[-411,-4584],[-389,-4499],
 [-383,-3819],[-363,-2329],[-344,-3446],[-333,-4270],[-324,-3643],[-320,-2793],[-288,-4402],[-286,-1351],[-285,-2489],[-278,-4085],[-277,-4512],[-259,-635],[-256,-2960],[-252,-118],[-245,-1090],[-229,-2382],[-227,-3100],[-223,-998],[-213,-4012],[-199,-4091],[-185,-4632],[-167,-1076],[-162,-2197],[-121,-325],[-92,-296],[-3,-961],[13,-4254],[16,-1148],[38,-3389],[43,-2479],[59,-2326],[66,-4932],[73,-4348],[75,-1025],[77,-3724],[78,-952],[88,-3093],[93,-3441],[99,-637],[104,-754],[115,-4831],[116,-3988],[124,-4377],[129,-1009],[132,-1910],[141,-2438],[166,-3251],[167,-3355],[170,-2057],[199,-1791],[204,-2187],[206,-1358],[210,-3857],[214,-1443],[219,-4110],[229,-3757],[232,-4861],[258,-2231],[260,-4276],[264,-4665],[278,-4101],[282,-1718],[300,-2891],[310,-2637],[313,-2351],[314,-3310],[331,-940],[333,-448],[336,-2352],[349,-1389],[355,-4334],[370,-1501],[383,-2934],[387,-3989],[402,-3617],[407,-1384],[416,-1725],[423,-1976],[425,-4131],[426,-84],[429,-2196],[434,-4910],[438,-1975],[474,-677],[476,-2652],[482,-256],[558,-4159],[574,-473],[595,-4098],[634,-2687],[645,-3809],[647,-4200],[649,-2103],[667,-4876],[683,-1993],[685,-850],[690,-3344],[696,-3970],[751,-2163],[757,-810],[760,-1518],[773,-2607],[788,-3246],[789,-1354],[804,-3890],[813,-1408],[820,-2329],[854,-1861],[863,-1832],[891,-222],[909,-4181],[956,-4494],[966,-2012],[991,-1011]],
18
)) # -672 not -746



print(Solution().numSubseq([3,5,6,7], 9)) # 4
print(Solution().numSubseq([3,3,6,8], 10)) # 6
print(Solution().numSubseq([2,3,3,4,6,7], 12)) # 61
print(Solution().numSubseq([5,2,4,1,7,6,8], 16)) # 127

print(Solution().minNumberOfSemesters(11, [], 2)) # 6
print(Solution().minNumberOfSemesters(3, [[1,3], [2,3]], 1)) # 3
print(Solution().minNumberOfSemesters(3, [[1,3], [2,3]], 2)) # 2
print(Solution().minNumberOfSemesters(3, [[1,3], [2,3]], 3)) # 2
print(Solution().minNumberOfSemesters(3, [[1,2], [2,3], [3,1]], 2)) # -1
print(Solution().minNumberOfSemesters(4, [[2,1],[3,1],[1,4]], 2)) # 3
print(Solution().minNumberOfSemesters(5, [[2,1],[3,1],[4,1],[1,5]], 2)) # 4

print(Solution().maxPerformance(3, [2,8,2], [2,7,1], 2))
print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))
print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3))
print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4))

print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))

print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7))

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