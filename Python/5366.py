from typing import List
import bisect, collections
import functools, operator
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        conn = {
            (1,0,1): (1,3,5), (1,0,-1): (1,4,6),
            (2,1,0): (2,5,6), (2,-1,0): (2,3,4),
            (3,1,0): (2,5,6), (3,0,-1): (1,4,6),
            (4,1,0): (2,5,6), (4,0,1): (1,3,5),
            (5,-1,0): (2,3,4), (5,0,-1): (1,4,6),
            (6,-1,0): (2,3,4), (6,0,1): (1,3,5)
        }
        stk = [(0,0,grid[0][0])]
        seen = set([(0,0)])
        while stk:
            x,y,v = stk.pop()
            if x == m-1 and y == n-1:
                return True
            for dx,dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen and grid[nx][ny] in conn.get((grid[x][y],dx,dy), []):
                    stk.append((nx,ny,grid[nx][ny]))
                    seen.add((nx,ny))
        return False

    def longestPrefix(self, s: str) -> str:
        pattern = s
        prefix = [-1] * len(pattern) # prefix[i] = j means pattern[:j+1] prefix is also suffix of pattern[:i+1]
        j = -1
        for i in range(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]: # cannot extend
                j = prefix[j]
            if pattern[j + 1] == pattern[i]: # extend number of chars which are both prefix and suffix
                j += 1
            prefix[i] = j
        return s[:prefix[-1]+1] if prefix[-1] != -1 else ''

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        def getV(s):
            return sum((ord(s[i])-ord('a'))*(26**(n-1-i)) for i in range(n))
        MOD = 10**9+7
        ans = getV(s2) - getV(s1) + 1
        if ans <= 0: return 0
        if ans == 1: return int(evil not in s1)
        return

    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 3 * k - 1: return False
        n, lookup = 0, set()
        for i in range(k - 1):
            n = n * 2 + int(s[i] == '1')
        for i in range(k - 1, len(s)):
            if i >= k and s[i - k] == '1':
                n = n - 2 ** (k - 1)
            n *= 2
            n += int(s[i] == '1')
            if n not in lookup and 0 <= n and n < 2 ** k:
                lookup.add(n)

        return 2 ** k == len(lookup)
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        import collections
        def dfs(s, t):
            if t in graph[s]: return True
            if t in fail[s]: return False
            for nei in graph[s]:
                ans = dfs(nei, t)
                if ans:
                    graph[nei].add(t)
                    graph[s].add(t)
                    return True
                else:
                    fail[nei].add(t)
            fail[s].add(t)
            return False

        graph = collections.defaultdict(set)
        fail = collections.defaultdict(set)
        for x, y in prerequisites:
            graph[x].add(y)

        return [dfs(x, y) for x, y in queries]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        dp = {(0, n-1): grid[0][0]+grid[0][-1]}
        for r in range(1, m):
            ndp = {}
            for c1, c2 in dp:
                for nc1 in (c1-1, c1, c1+1):
                    if not (0<=nc1<n): continue
                    for nc2 in (c2-1, c2, c2+1):
                        if not (0<=nc2<n): continue
                        ndp[nc1, nc2] = max(dp[c1, c2] + grid[r][nc1] + (grid[r][nc2] if nc2 != nc1 else 0),
                                            ndp.get((nc1, nc2), float('-inf')))
            dp = ndp
        return max(dp.values())


    from typing import List
    # 5397. Simplified Fractions
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a

        prime = set([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        ans = []
        for k in range(2, n+1):
            ans.extend("{}/{}".format(m, k) for m in range(1, k) if k in prime or gcd(m, k) == 1)
        return ans

    # 5413
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        a = text.split()
        lookup = collections.defaultdict(list)

        for i in range(len(a)):
            lookup[len(a[i])].append(i)
        b = []
        for k in sorted(lookup):
            for i in lookup[k]:
                b.append(a[i])
        b = ' '.join(b)
        return b[0].upper() + b[1:]

    # 5414
    def peopleIndexes2(self, favoriteCompanies: List[List[str]]) -> List[int]:
        i, com = 0, {}
        nfc = []
        st2idx = {}
        for k, f in enumerate(favoriteCompanies):
            st = set()
            for c in f:
                if c not in com:
                    com[c] = i
                    i += 1
                st.add(com[c])
            nfc.append(st)
            st2idx[tuple(st)] = k

        nfc.sort(key=len, reverse=True)
        ans = [st2idx[tuple(nfc[0])]]
        for i in range(1, len(nfc)):
            if any(nfc[i] <= nfc[j] for j in range(i)): continue
            ans.append(st2idx[tuple(nfc[i])])
        return list(sorted(ans))

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        comSet = {com for favor in favoriteCompanies for com in favor}
        comList = list(comSet)
        comLookup = {v:i for i, v in enumerate(comList)}
        fvCom = []
        getidx = {}
        for i, fv in enumerate(favoriteCompanies):
            trans = set([comLookup[c] for c in fv])
            getidx[tuple(trans)] = i
            fvCom.append(trans)

        fvCom.sort(key=len, reverse=True)
        ret = []
        for i in range(0, len(fvCom)):
            if any(fvCom[i] <= fvCom[j] for j in range(i)): continue
            ret.append(getidx[tuple(fvCom[i])])
        return list(sorted(ret))
#Output: [0,1,4]

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)
        freq = sorted(cnt.values())
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
        pos = bisect.bisect(freq, k)
        return len(freq) - pos

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def valid(mid):
            count, made = 0, 0
            for x in bloomDay:
                if x <= mid:
                    count += 1
                else:
                    made += count // k
                    if made >= m: return True
                    count = 0
            made += count // k
            return made >= m

        if len(bloomDay) < m * k: return -1
        if len(bloomDay) == m * k: return max(bloomDay)
        if k == 1:
            bloomDay.sort()
            return bloomDay[m-1]
        l, r = 1, max(bloomDay)
        while l < r:
            mid = (r-l) // 2 + l
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return l

    def getFolderNames(self, names: List[str]) -> List[str]:
        ans, seen = [], {}
        for name in names:
            if name not in seen:
                ans.append(name)
                seen[name] = 1
            else:
                avaiInt = seen[name]
                cand = "{}({})".format(name, avaiInt)
                while cand in seen:
                    avaiInt += 1
                    cand = "{}({})".format(name, avaiInt)
                ans.append(cand)
                seen[cand] = 1
                seen[name] = avaiInt + 1
        return ans

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans, empty, water = [], [], {}
        for id, r in enumerate(rains):
            if not r:
                empty.append(id)
                ans.append(1)
            else:
                if r in water:
                    k = bisect.bisect(empty, water[r])
                    if k == len(empty):
                        return []

                    ans[empty.pop(k)] = r
                water[r] = id
                ans.append(-1)
        return ans

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        import heapq
        heap, ans = [], []
        for i in range(n):
            heapq.heappush(heap, (nums[i], i, i))
        while len(ans) < right:
            v, s, e = heapq.heappop(heap)
            ans.append(v)
            if e < n - 1:
                heapq.heappush(heap, (v + nums[e + 1], s, e + 1))
        heapq.heapify(ans)
        for _ in range(1, left):
            heapq.heappop(ans)
        return sum(ans)

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        import heapq
        graph = collections.defaultdict(dict)
        for i, (u, v) in enumerate(edges):
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]

        prob = [float('-inf')] * n
        prob[start] = 1.0
        pq = []
        for v, w in graph[start].items():
            heapq.heappush(pq, (-w, v))
        while pq:
            w, v = heapq.heappop(pq)
            w = -w
            if w > prob[v]:
                prob[v] = w
                for vv, ww in graph[v].items():
                    heapq.heappush(pq, (-w*ww, vv))
        return prob[end] if prob[end] != float('-inf') else 0.0
    # 5465
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node):
            freq = [0] * 26
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    ar = dfs(nei)
                    if ar:
                        freq = [ar[i]+freq[i] for i in range(len(freq))]
            idx = ord(labels[node]) - ord('a')
            freq[idx] += 1
            ans[node] = freq[idx]
            return freq

        ans = [1] * n
        visited = {0}
        dfs(0)
        return ans
    # 5466
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        b, e = [float('inf')]*26, [-1]*26
        for i, ch in enumerate(s):
            idx = ord(ch)-ord('a')
            b[idx] = min(b[idx], i)
            e[idx] = max(e[idx], i)
        interval = []
        for i in range(len(b)):
            if b[i] != float('inf'):
                interval.append([b[i], e[i]])
        interval.sort()

        def getLen(a):
            return sum(e-b for b,e in a)

        def dfs(start, cur):
            if start == len(interval):
                if len(cur) > len(ans[0]) or (len(cur) == len(ans[0]) and getLen(cur) < getLen(ans[0])):
                    ans[0]= list(cur)
                return
            # use start
            cur.append(list(interval[start]))
            for i in range(start+1, len(interval)+1):
                if i == len(interval):
                    dfs(i, cur)
                else:
                    if interval[i][0] > cur[-1][1]:
                        dfs(i, cur)
                    else:
                        cur[-1][1] = max(cur[-1][1], interval[i][1])

            cur.pop()
            # not use start
            dfs(start+1, cur)

        ans = [[]]
        dfs(0, [])
        return [(s[b:(e+1)]) for b,e in ans[0]]

    # Lintcode contest 7/24/2020 306
    def ProductList(self, offset, n, len1, len2):
        if offset < len1:
            if len1 - offset >= n:
                return [offset, offset + n, 0, 0]
            else:
                return [offset, len1, 0, min(len2, n-(len1-offset))]
        elif offset < len1 + len2:
            return [0, 0, offset - len1, min(len2, offset-len1+n)]
        else:
            return [0, 0, 0, 0]

    # Lintcode contest 7/24/2020 300
    def maxValue(self, meeting, value):
        def dfs(i, path, curValue):
            if i == len(meeting):
                if curValue > self.ans:
                    self.ans = max(self.ans, curValue)
                    self.p = path[:]
                return

            # dont use this
            dfs(i + 1, path, curValue)

            # use this
            if not path or meeting[i][0][0] >= path[-1][0][1]:
                path.append(meeting[i])
                dfs(i + 1, path, curValue + meeting[i][1])
                path.pop()

        meeting = sorted(zip(meeting, value))
        self.ans = float('-inf')
        self.p = None
        dfs(0, [], 0)
        print(self.p)
        return self.ans

    # Lintcode contest 7/31/2020 308
    # You're given a string of length nn.
    # We call a substring which is of length kk, and only contains 11 repeated character a special substring.
    # Please calculate the number of special substrings of the given string.
    def specialSubstringCount(self, str, k):
        #ans, pre, repeat, n = 0, None, 0, len(str)
        cnt = collections.Counter(str[:k])
        repeat = sum(x > 1 for x in cnt.values())
        ans = int(repeat == 1)
        for i in range(k, len(str)):
            if str[i] != str[i-k]:
                x = str[i]
                if cnt[x] == 1: repeat += 1
                cnt[x] += 1
                x = str[i-k]
                if cnt[x] == 2: repeat -= 1
                cnt[x] -= 1
            ans += int(repeat == 1)
        return ans

    # Lintcode contest 7/31/2020 307
    # Given two strings A and B, the task is to convert A to B if possible. The only operation allowed is to
    # put any character from A and insert it at front. Find if it’s possible to convert the string. If yes,
    # then output minimum number of operations required for transformation.If no, then output -1.
    # Hint:0 ≤ the length of A, the length of B ≤ 100000
    # https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/
    def transform(self, A, B):
        cA, cB = collections.Counter(A), collections.Counter(B)
        if cA-cB or cB-cA:
            return -1

        i = j = len(A)-1
        res = 0
        while i >= 0:
            while i >= 0 and A[i] != B[j]:
                i -= 1
                res += 1

            if i >= 0:
                i -= 1
                j -= 1

        return res
    # 5477
    def minSwaps(self, grid: List[List[int]]) -> int:
        n, ans = len(grid), 0
        rightzero = [0]*n
        for i in range(n):
            cnt, j = 0, n-1
            while j>=0 and grid[i][j] == 0:
                cnt, j = cnt+1, j-1
            rightzero[i] = cnt
        for i in range(n-1):
            need = n-1-i
            for k in range(n):
                if rightzero[k] >= need:
                    ans += k-i
                    for j in range(k, i, -1):
                        rightzero[j] = rightzero[j-1]
                    rightzero[i] = 0
                    break
            else:
                return -1
        return ans
    # lintcode contest 8/7/2020 314
    def minimumMessages(self, m, record):
        if len(record) <= 2: return -1
        #bk = list(record)
        change = collections.defaultdict(int)
        ans = 0
        for i in range(2, len(record)):
            s, lost = 0, 0
            for j in range(3):
                s += max(0, record[i-j])
                lost += int(record[i-j] == -1)
            if s >= m: continue
            if lost == 0:
                return -1
            for j in range(3):
                if record[i-j] == -1:
                    change[i-j] = max(m - s, change[i-j])
        return sum(max(x, change[i]) for i, x in enumerate(record))
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, ans = 0, 0
        while k > 0 and i < len(arr):
            ans += 1
            if arr[i] == ans:
                i += 1
            else:
                k -= 1
        return ans + k
    def MaxPeopleNumber(self, height):
        def divide(m):
            ans = 0
            for x in groups:
                ans += x // m
                if ans >= m:
                    return True
            return ans >= m
        height.sort()
        groups = [1]
        for i in range(1, len(height)):
            if height[i] - height[i-1] <= 2:
                groups[-1] += 1
            else:
                groups.append(1)
        l, r = 1, max(groups)
        while l < r:
            m = (l+r+1) // 2
            if divide(m):
                l = m
            else:
                r = m - 1
        return l**2

    def fact(self, n):
        return functools.reduce(operator.mul, range(1, n+1), 1)
    # 5489
    def maxDistance(self, position: List[int], m: int) -> int:
        def ok(mid):
            last = position[0]
            for i in range(1, m):
                nxt = last + mid
                p = bisect.bisect_left(position, nxt)
                if p >= len(position): return False
                last = position[p]
            return True

        if m == 2: return max(position) - min(position)
        position.sort()
        l, r = 1, position[-1] - position[0]
        while l < r:
            mid = (l + r + 1) // 2
            if ok(mid):
                l = mid
            else:
                r = mid - 1
        return l

    # lintcode contest 8/21/2020 327
    def getDistanceMetrics(self, a):
        ans = [0] * len(a)
        mapping = collections.defaultdict(list)
        for i, v in enumerate(a):
            mapping[v].append(i)
        for _, lst in mapping.items():
            for x in lst:
                ans[x] = sum(abs(x-y) for y in lst)
        return ans

    # lintcode prob 342 contest 9/18/2020
    def valley(self, num):
        n = len(num)
        down, up = [0] * n, [0] * n
        for i in range(1, n):
            for j in range(i):
                if num[j] > num[i]:
                    down[i] = max(down[i], 1 + down[j])

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if num[i] < num[j]:
                    up[i] = max(up[i], 1 + up[j])

        ans = 0
        for i, x in enumerate(num):
            for j in range(i + 1, n):
                if num[j] == x:
                    ans = max(ans, 2 * (1 + min(down[i], up[j])))
        return ans
    # lintcode contest 9/4/2020
    def suffixQuery(self, s):
        n, ans = len(s), 1
        dp = [0]*n
        dp[-1] = 1
        for i in reversed(range(n-1)):
            for j in reversed(range(i, n)):
                dp[j] = 0
                if s[i] == s[j]:
                    if j<=i+1:
                        dp[j] = j-i+1
                    else:
                        dp[j] = dp[j-1] + (2 if dp[j-1] == j-i-1 else 1)
                    ans += dp[j]
        return ans
    def numSpecial(self, mat: List[List[int]]) -> int:
        singleRows = [r for r in mat if sum(r) == 1]
        singleCols = [c for c in zip(*mat) if sum(c) == 1]
        return sum(mat[i][j] == 1 and i in singleRows and j in singleCols for i in range(len(mat)) for j in range(len(mat[0])))

    # leetcode 1589 contest 9/19/2020
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        events = collections.defaultdict(int)
        for x, y in requests:
            for t, delta in [(x, 1), (y+1, -1)]:
                events[t] += delta
        times = [t for t in events if events[t] != 0]
        times.sort()
        counter = collections.defaultdict(int)
        last, bal = times[0], events[times[0]]
        for t in times[1:]:
            counter[bal] += t - last
            last, bal = t, bal + events[t]

        start, ans, nums = 0, 0, sorted(nums, reverse=True)
        for mult in sorted(counter, reverse=True):
            cnt = counter[mult]
            ans += mult * sum(nums[start:start+cnt])
            start += cnt
        return ans

    # leetcode 344 contest 10/9/2020
    def LongestSongTime(self, song, M):
        song.sort()
        mx = song[-1]
        song.pop()
        dp = [0] * M
        for x in reversed(song):
            for i in range(len(dp)-1, x-1, -1):
                dp[i] = max(dp[i], x + dp[i-x])
        return dp[-1] + mx

print(Solution().LongestSongTime([1,2,3,4,5], 14))

print(Solution().maxSumRangeQuery([1,2,3,4,5], [[1,3],[0,1]])) # 19
print(Solution().valley([0,0,4,4,6,0,2,5,0,0,4,10,7,1,6,5,6,0,2,8,2,7,10,0,4,7,6,9,1,9,4,5,0,6,5,1,5,3,3,6,5,10,1,1,10,0,9,6,6,4])) # 10
print(Solution().valley([5,4,3,2,1,2,3,4,5])) # 8
print(Solution().valley([1,2,3,4,5])) # 0
'''
print(Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]])) # 1
print(Solution().suffixQuery("bacbdab")) # 12
print(Solution().suffixQuery("babcxyba")) # 15
print(Solution().getDistanceMetrics([1, 2, 1, 1, 2, 3])) # [5, 3, 3, 4, 3, 0]
'''
def perfectSubstring_wrong(s, k): # cannot solve in O(n)
    cnt = [0] * 10
    l, ans = 0, 0
    for r, c in enumerate(s):
        c = int(c)
        cnt[c] += 1
        if cnt[c] == k:
            j = l
            cnt2 = list(cnt)
            while j < r:
                if all(x in (k, 0) for x in cnt2):
                    ans += 1
                y = int(s[j])
                cnt2[y] -= ge
                j += 1
        elif cnt[c] > k:
            while cnt[c] > k:
                y = int(s[l])
                cnt[y] -= 1
                l += 1
            if all(x in (k, 0) for x in cnt):
                ans += 1
    while l < r:
        y = int(s[l])
        cnt[y] -= 1
        l += 1
        if all(x in (k, 0) for x in cnt):
            ans += 1
    return ans
def perfectSubstring(s, k): # O(n^2)
    ans = 0
    for l in range(len(s)):
        cnt = [0] * 10
        for r in range(l, len(s)):
            x = int(s[r])
            cnt[x] += 1
            if cnt[x] > k:
                break
            if cnt[x] == k and all(v == 0 or v == k for v in cnt):
                ans += 1
    return ans


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain", "oathtao"]
import collections
class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.child = collections.defaultdict(TrieNode)

def findWords(board, words):
    def dfs(s, node, i, j): # node should match s
        if node.is_string:
            ans.append(s)
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                c = board[ni][nj]
                if c in node.child:
                    visited.add((ni, nj))
                    dfs(s + c, node.child[c], ni, nj)
                    visited.discard((ni, nj))
    if not board: return []
    root = TrieNode()
    for w in words:
        cur = root
        for c in w:
            cur = cur.child[c]
        cur.is_string = True

    ans = []
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            c = board[i][j]
            if c in root.child:
                visited = {(i, j)}
                dfs(c, root.child[c], i, j)
    return ans


print(findWords(board, words))# Output: ["eat","oath"]
print(perfectSubstring('12221122', 2)) # 7
print(perfectSubstring('1020122', 2)) # 2
'''
print(Solution().fact(12)//(Solution().fact(4)*3)//(Solution().fact(2)*2))
print(Solution().fact(5))
print(Solution().fact(6))
print(Solution().MaxPeopleNumber( [1,4,5,6,7,7,7,10,11,12])) # 9
print(Solution().findKthPositive([2,3,4,7,11], 5))
print(Solution().findKthPositive([1,2,3,4], 2))
print(Solution().minimumMessages(3, [2,-1,0,1])) # 5
print(Solution().minimumMessages(3, [2,0,1,1])) # -1
print(Solution().minSwaps([[0,0,1],[1,1,0],[1,0,0]])) # 3
print(Solution().minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])) # -1
print(Solution().minSwaps([[1,0,0],[1,1,0],[1,1,1]])) # 0

print(Solution().transform('EACBD', 'EABCD')) # 3

print(Solution().specialSubstringCount("reversestring", 5)) # 4
print(Solution().specialSubstringCount("helloo", 4)) # 2
print(Solution().specialSubstringCount("helloo", 2)) # 2
print(Solution().specialSubstringCount("helloo", 3)) # 3
print(Solution().maxValue(
[[27014,49093],[8576,20531],[1341,31801],[18937,36945],[20261,35359],[26941,45624],[19040,38937],[17432,32978],[22402,32295],[13792,37955],[25703,39861],[11915,29179],[15151,43716],[15668,25671],[36775,38365],[17854,20907],[4056,49958],[34597,39415],[34710,44773],[34800,47626],[3415,48101],[15805,42835],[2432,12186],[20636,22326],[24713,41150],[8511,17056],[2554,40505],[29073,38540],[12746,16807],[6485,6579],[14052,46237],[9129,48169],[20962,29803],[23101,36018],[16457,31780],[18710,22249],[3190,33750],[7029,46376],[43979,45389],[24167,47718],[14548,17083],[7146,20611],[20279,46052],[8543,30186],[16123,29542],[20437,44924],[5078,47706],[1858,4540],[14371,36064],[8417,46028]],
[1328,1641,4457,1494,9167,8647,4974,3365,9727,6947,1881,6976,405,9915,1025,6963,6989,972,1162,9280,2039,958,1816,3776,2626,3483,773,2041,776,4965,2261,1488,923,1911,2008,5455,7358,9402,8544,122,631,3787,4612,333,2036,9868,7604,5144,1132,9257]
)) # 39851 not 47231
print(Solution().maxValue([[10,40],[20,50],[30,45],[40,60]], [3,6,2,4])) # 7
print(Solution().maxValue([[10,20],[20,30]], [2,4])) # 6
print(Solution().ProductList(4,1,3,3)) # [2,4,0,2]
print(Solution().ProductList(2,4,4,4)) # [2,4,0,2]
print(Solution().ProductList(1,2,4,4)) # [1,3,0,0]


# 调整数组的顺序使奇数位于偶数的前面，并保持原有的相对顺序   空间复杂度O(1)

def reorder(arr: List[int]) -> List[int]: # Time O(n^2) Space O(1)
    pos = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            tmp = arr[i]
            for j in range(i, pos, -1):
                arr[j] = arr[j-1]
            arr[pos] = tmp
            pos += 1
    return arr

def reorder2(arr: List[int]) -> List[int]:
    pos = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            for j in range(i, pos, -1):
                arr[j-1], arr[j] = arr[j], arr[j-1]
            pos += 1
    return arr

def reorder_sort(array):
    return sorted(array, key=lambda x:x&1==0) # odd->False/0, even->True/1


print(reorder([1, 3, 4, 5, 6, 7, 8]))
print(reorder([22, 1, 3, 2, 4, 5, 6, 20, 12, 7, 8]))
print(reorder([]))
print(reorder([1, 3]))
print(reorder([4, 8]))

print(Solution().maxNumOfSubstrings("abab")) # ["abab"] # my solution fail for this
print(Solution().maxNumOfSubstrings("abbaccd")) # ["d","bb","cc"]
print(Solution().maxNumOfSubstrings("adefaddaccc")) # ["e","f","ccc"]
print(Solution().countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd")) # [2,1,1,1,1,1,1]
print(Solution().countSubTrees(4, [[0,1],[1,2],[0,3]], "bbbb")) # [4,2,1,1]
print(Solution().countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], "aabab")) # [3,2,1,1,1]
print(Solution().countSubTrees(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], "cbabaa")) # [1,2,1,1,2,1]
print(Solution().countSubTrees(7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa")) # [6,5,4,1,3,2,1]

print(Solution().maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)) # 0.25
print(Solution().maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2)) # 0.3
print(Solution().maxProbability(3, [[0,1]], [0.5], 0, 2)) # 0.0
print(Solution().rangeSum([1,2,3,4], 4, 1, 5)) # 13
print(Solution().rangeSum([1,2,3,4], 4, 3, 4)) # 6
print(Solution().rangeSum([1,2,3,4], 4, 1, 10)) # 50
print(Solution().avoidFlood([0,1,1])) # []
print(Solution().avoidFlood( [1,2,0,0,2,1])) #[-1,-1,2,1,-1,-1]
print(Solution().avoidFlood([1,2,0,1,2])) # []
print(Solution().avoidFlood( [69,0,0,0,69])) # [-1,69,1,1,-1]
print(Solution().avoidFlood([2,10,10])) # []
print(Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]))
# ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
print(Solution().getFolderNames(["gta","gta(1)","gta","avalon","gta(6)", "gta"]))
# ["gta","gta(1)","gta(2)","avalon", "gta(6)", "gta(3)"]
'''

# awice
class TreeAncestor(object):
    def __init__(self, n, parent):
        self.pars = [parent]
        self.n = n
        for k in range(17):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        i = 0
        while k:
            if node == -1: break
            if (k & 1):
                node = self.pars[i][node]
            i += 1
            k >>= 1
        return node
class TreeAncestor_ming:

    def __init__(self, n: int, parent: List[int]):
        self.p = collections.defaultdict(dict)
        self.c = collections.defaultdict(list)
        self.dep = {}
        for i, p in enumerate(parent):
            self.p[i][1] = p
            self.c[p].append(i)
        '''
        def dfs(node, extra):
            self.p[node].extend(extra)
            for cc in self.c[node]:
                dfs(cc, self.p[node])
        for c in self.c[0]:
            dfs(c, [])      '''
        def dfs(node, d):
            self.dep[node] = d
            for c in self.c[node]:
                dfs(c, d+1)
        dfs(0, 0)

    def getKthAncestor(self, node: int, k: int) -> int:
        r, oldk = node, k
        if k > self.dep[node]: return -1
        if k == 1: return self.p[node][1]
        if len(self.p[node]) > 1:
            keys = list(self.p[node].keys())
            i = bisect.bisect(keys, k)
            k -= keys[i-1]
            node = self.p[node][keys[i-1]]
        while k:
            node = self.p[node][1]
            k -= 1
        self.p[r][oldk] = node
        return node
    #        return self.p[node][k-1] if len(self.p[node]) >= k else -1





    '''
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(obj.getKthAncestor(3, 1)) # 1
print(obj.getKthAncestor(5, 2)) # 0
print(obj.getKthAncestor(6, 3)) # -1
obj = TreeAncestor(10,[-1,0,1,2,0,1,0,4,7,1])
print(obj.getKthAncestor(3, 3)) # 0
print(obj.getKthAncestor(2,9)) # -1
print(obj.getKthAncestor(2,7)) # -1
print(obj.getKthAncestor(3, 2)) # 1
print(obj.getKthAncestor(2,10)) # -1
print(obj.getKthAncestor(4,9)) # -1
print(obj.getKthAncestor(0,2)) # -1
print(obj.getKthAncestor(6,4)) # -1
print(obj.getKthAncestor(4,2)) # -1
print(obj.getKthAncestor(4,7)) # -1

["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[],[3,3],[2,9],[2,7],[3,2],[2,10],[4,9],[0,2],[6,4],[4,2],[4,7]]
print(Solution().minDays([1,10,2,9,3,8,4,7,5,6], 4, 2)) # 9
print(Solution().minDays([7,7,7,7,12,7,7], 2, 3)) # 12
print(Solution().minDays([1000000000,1000000000], 1, 1)) # 1000000000
print(Solution().minDays([1,10,3,10,2], 3, 1)) # 3
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 1)) # 3
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 2)) # 2
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3)) # 2
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 4)) # 1
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 5)) # 1

print(Solution().peopleIndexes(
[["arrtztkotazhufrsfczr","knzgidixqgtnahamebxf","zibvccaoayyihidztflj"],["cffiqfviuwjowkppdajm","owqvnrhuzwqohquamvsz"],["knzgidixqgtnahamebxf","owqvnrhuzwqohquamvsz","qzeqyrgnbplsrgqnplnl"],["arrtztkotazhufrsfczr","cffiqfviuwjowkppdajm"],["arrtztkotazhufrsfczr","knzgidixqgtnahamebxf","owqvnrhuzwqohquamvsz","qzeqyrgnbplsrgqnplnl","zibvccaoayyihidztflj"]]

))
print(Solution().peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
print(Solution().peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
print(Solution().peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))

print(Solution().simplifiedFractions(1))
print(Solution().simplifiedFractions(2))
print(Solution().simplifiedFractions(3))
print(Solution().simplifiedFractions(4))
print(Solution().simplifiedFractions(5))
print(Solution().simplifiedFractions(6))

print(Solution().cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])) # 24
print(Solution().cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])) # 28
print(Solution().cherryPickup( [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]])) # 22
print(Solution().cherryPickup([[1,1],[1,1]])) # 4

print(Solution().checkIfPrerequisite(5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]])) # [true,false,true,false]
print(Solution().checkIfPrerequisite(3, [[1,0],[2,0]], [[0,1],[2,0]])) # [false,true]
print(Solution().checkIfPrerequisite(2,  [[1,2],[1,0],[2,0]], [[1,0],[1,2]])) # [true, true]
print(Solution().checkIfPrerequisite(2, [], [[1,0],[0,1]])) # [false, false]

print(Solution().hasAllCodes("0101", 13)) # False
print(Solution().hasAllCodes("10010011", 2)) # True

print(Solution().hasAllCodes("00110110", 2)) # True
print(Solution().hasAllCodes("110101011011000011011111000000", 5)) # False
print(Solution().longestPrefix("aacbbacacbbbcacbccccabbbcbbaacacbcbcababbcbabcbaababbacbbbacacccabcbaaaaacaaaaacaabcbcccccbabcacacccbbacbaaacaccacbaababacbcaabaaabbbacabbcacbbaacacbccaabbcbbbacaaaacbbbccabaacabbbaabbacabccbaabacbcbacacabbacaaababcbabcccbcbacbcbaccaababacccbcabcabbaabbcbccbbbbabacbcbbbabbbcaccccbbcbabbabcbaaababbcaabbcbbcaacacaabccbbabcbbcaaacbcbabaaccaaaaaabbaaaaccbbbcacbcacbaccacacccaabcbacabababbcbccbbaacbaaabaabcccbabbcbabcaaccbbacbccbacbacbbcccaacabbbcaacbaacbcccacabbbbaccaaacbaacaabaabccbcaacbaccacaaababbcabccabbacacabbaccaabaacbcacbaabcacabbabbcbcccacaacaaaaababbcbaabacaabbbcaabacacbabbcacbcbbbacaacaaaacbaaababcabccacabbcbbbbcaabaaabacbbcccaacacbabbcaaabbcbabbbcccbcbccbabcbaabcbcbbccaabaabbbacabbcbbbabaaaaabaccaacaabbaaabbcbcbcaccbbcccaaccbaabcacbabcccbabaccccabbbcaaaababaacbaabcaabcaabacccbcbbbbaaccaaabcbcacacaccbccbbcccbccbaaacabaacaccbcbacbcabaaacacbbbcbaabbbbcbcaaabcbbcaaccbcbbbabcbabcbabccbcaacaaabacacbabaababbbbabaccacbcaccabbaccbbbbaacaabaabacbcbbccabacaacaccabbcacbbcacaacccccbabbabbcaccbbbbbacbacaaabbbccbbbcbbbaaccaabacccacababbbbbcabbcccbacabaabcbbbcaccaaccbbaacbaccbabbbaaccbbbcbcaccbbbabbacacbbbacccccacccccbaacbccaacaaabccbabbbcbbbbacbcbcabbbbacbbbbacabbbaaccacaabcacabaaaccabcccccaaaccacabccbabbccccbbcccabbcabbaacbabacbcbaaccaccaaabbacaacacbacccaaccccbaaacacaccabccabcaaaccbbbcaacaaabbbccaccbabcaabacbacbbcbbababbaabbbaabccccccabbcccaabbabcacccccacacbaabababbaacacbacbabbbbaaaaabcbccabaccbabacccbbbbbcbccbbcbcacaccbbccabccacccbaaacacbccaaccabbccaaabacaabcaaacacaaccbcbbbbcabbabcccbacaaaabbcbbccccabbbbcbccaaaaccaacaccaabccbaabbcbaccbaaacccaabbbbcacaccaacabbaaaaacaaccabacbbcbccabbcabbbbababaaabbcbaabbabbbacbbcaabcbacaccbbbbbbbcaabbbcbbbaabccbaabbacbcaabacaccabacabbabacabbacccbabcbcaaabbbcaababbaaaaacacccbccccbbcabbabacacbabcbcabbcccacbbcabacbaccbcbaaacbaaacbacbabccabacbcabcccabccbacabbaccccccaabcbbcaccabbcbbabbbbaacccccacbbbabbacacccbaaabcccbaacaabbbccaccbaaabcbacabbacccabcacccbacbcabcccabbbbbaaaacbacacbcbabaabbbbcaaaaacbbaccaaaabcaaccaccbcabcacbaaabcbacaacaaabbcbccacababbcbaaabcacbccaccacbcccbbacbcbacbbabacccaaaabaccbbacaacacaccccacbaaaccacaacccbbbbbcaabbcacbacccbcbcbbacccabccbcaababaccbbabaaabbabcaaacacaccaccaabbccbcbbcacaaabababbcbbaacbcbcabbccbaacbcabcbabaabbabcbcabacabccabcaabcbabaaabbcbacbaacaabacaccacaaabbbacbcbaaccabbbbaccaaabbcbbbbaacaccacbcacabbacaabccbbccbbcbccccacaacabacaababaccabbbccbbbcccbabbccbaccaacbccbcaacacacbbacbbcbbbaaaacbccacacabbcccababcacbccbaacabcbaaccbbabccabbabbccbbaaccbbaacccaaabbcbbaccbacababcbccbabbcaacaacbcaacbaaacaaabbcbacabcaaabbcaacbaaaaacaabccccbcabacabbabbabaacbbbcaaaabbccbbaacaacbbcbcccacaacbccabbcaccabbabcaccacacbbccbccccabcabcabccabaaabcbaaccacacbabbcbccaaacbbcccbabaababcbabccabacbcbccccaaacacaaccbacbccbbbcbccbcbaacbbabbbbcababccbcaaccccbcbbccbbcbccacbcbbbacbbcababcccbbacaabaabcbacbbcaaaaccccccccabbcbcaccbbbaababccaacbabbabbcbcccaccbbbabacabbbabcacbbbbbbcccbaacaccbbaabbaccccbcbcaaaaabbcaacbaacacbbaabaabacaccbbaabacaccaccccacbacaabbbccaccbccaacabcababbcbaacccbbaaccaacbaabbabcbbbcabbcaacacacbcaccaaaacacbcaaabbbcabbbbbaaccaaabbabbcccbbbccaaabaaaababacaabcabcbbbbcbcccaaacacbaacbcbabaabbabaaaaacacabbcccabacccacaaccacaacbccbbccccbcaccaacaacabbcaccaababaacbbbaaccababccbbcabcccbabbbcbccacababbaaababbbccbacabacbaaaabbcabaaacbcbcaccccabcacbaaaccacbacbcbcabbccabcacccccccbbbbbbaaccabccbacaccbcabacbbccacaabaacacaabccacababbacabbcacacbbaccacbbbacbbccbccabbccacabcbaacbbccaccbbbccbccbcabacbcacbbaabbabbbcaacabcccbbbbabcaaababacababcaccbcbbcabbbbcabbaccaaacabcacbbbcbacccbacbbbcababaccbcaabccaabccaccaaabbccaacacccccbaacabcccaaabccbacbbccbaabbacbcaccbaabcacaacaaaacbccabaccacbbaacbbbbababacabbabcaaaabccbcbabababbcccbcbbbcaccccbabbbaabacabbbbabacacabcabcbacabbccbcccbabaacababaabbaabacbcbbcbccaccccbacacababaaaaacaccccacbcaaaccccaccbcbacccbbacbbcbcbccbaccccaabbcbcbaaccccaabcccccbbbabacbbbcaaaaaabcacaaacabaccacacbaccbcbccacaaaacabccbcccbbaaaaaabbaabacbbaccbbaaabbccbabcbcabcbccacaacaaccccbccacabbccaaabacabcbbaccabbacccaacabcaaacbccbbcacbaaccaccccabbaaababaccacbbabcabbccccbaabcbcbbbacbbcacbacacaaacbbbcbbacbaccbbbbaabccbcbacbacbbaaabbbccbbcbbacabacabaccbabbcabccabcbaacbcabacaaaacbbccccaababcabcabcbbaacbccaaccbcaccaabaaabacaccabababccbbcccccccabcbbbbbccbcbbcacbaaaabbbcbbcccbbbcccbccacbacacaccabccbacababbbacaabbabacbabccaaabcacaababcbabcaabcbcaaabcbbbbabaaacaacabcaaabaccbabbcaaccbbbaabcccabcacaaccbcabaccbcaaabbbaabcbaacaacacacaaccbbcaccbbcccbccaaccaaaaccccacbcbababccaaacaaacaccaabbbbbbcbbaabbabbcabbabaacbaaababccabaaccbababbcbabababcccaacbcaacaaababcbccaabacbbbacabaabaabbbaaacbabaaaccbaccbaaacbbcbcbaaabaaaabbbbccacbcacababcbccbbbbacbccbacccbccaccaacbcabbcccbabcccbcbbbcabcabacabcabccbcaaabbbcbacbcbbbabcccaaaacbcbaacaaabbbaaaabccaacccababcacbbacccabaccaaabbccbbaabcabcbaaabccccabaccbcbcaccbbbccabccababcbaaacabbabcabbbaacbbaacbbcabcabcccbcaaaacbbcbacacbccbaabaaaabbbcbaabcccbcaccccaaaacbcccacbcacabababcbbabccbcccccbaabbccabacbabbcccbbbbcaaabcbbaccbcacabaabaaacacbaaccaccbaaccaacbccbabaaccccccccaccbaaabbcaabababccacaccbaaccbcccbbabbccababaaccccccabaccaababcaaacbacbcbcacbcbacaabacacabaabcaabcaaccacacbcaccbcaccaacaababbcbbccbccccccbcccbbcbaabcaaaabaabaaacbababccbaaabbccbbcabcbcbbacabbbcbaacccaabcacbabccbbcbcbbacaaabacccbaaacbccacaacacbcbbcabbaccaaababcbcaacbababccacccccacbccbcabbbacabbcbabbcabbaacccaabccbbabbbabcabbcabbbcacbaaaccaccabacacbacbccabacaacbabbccbbbcbcacbaaaabcaacbcabcabcbccacacbcababcbbaccacbaabaaccacaccbccacacbaacbbaaaaababaacbbcaabbcccbaabcabaaabcbbbbabacbbababbbbabaaababcccccccbbabcbbabababbcacbbbabbbaaaabacbaacaaacccbabacbbbaccbaabbbbbccabbccacbbabbbacabccaaabbcccabaccbacabbaabacccaccbabccbbbacabccabbbcbccccbaabcaaccabcaaacaaacaccaabbaaabbbbcccabbcabccbccabbbbcbcbcbcccabaaaaabbbbcacabacccccacbbbcbbaccbcbcacccabaaccacbcacabcabbccbababababcccbbbbabaaaaacbbcbcaacbaccccbbbcacbabaaabbbcaacaccbaabaaccabacccbbbcbccbacabcbababcbaaaacbbaaaabaacbbbcaacbcbbbccccbcaccbcbaccacbbbcbbcacbacaacababcaacacbcabbcabccbbcbcabbaabaabbbcbbaabaccabbacbccbaccacbbcababbccaabaaaababacaabaacbacbbccbbcbacaaababcaaccbcbcaabaaccbcaccbccabcbabbaabbcaacccabbcbbbabccaacbbbbcbaabaacccabaabbcccbbaabbbcbbcabbcaaaacacbbcaccccbacbacbcbaacbaabaccaacccccabacbabbcbbacbcbbabacacbaacbbbbacabccbbabaabbaaaaabaccaaababcabaacbbcbbccabacabbcabcbcbaaacaabcabcababbacacbacbccbcbbccacbcabcbbababacbccbbcabbbabaaccbbabcbbcbcccbcccabcabbcaaabcbcaaabcaaccbcbbbacabcbbbbccbbcbcaaabcbcabaaacabcababbabbcabbbcabbabccacbacacabacbbbaaaacbbcbacabaccabcccbabccaabccbbbabaabbcbbcacaccbabbabaaacbbcaacbaaababaacbccbabbbabbcaabbbcbccbaaababcabbaccbaacccacaabacaabbcabbcacbabbcacabbbccccbbaaccaaaccbcaabcbcaabbcbccbcbbcccbababaaacaccbcacaccccabcbaccbcabababcbcbcbbbbabbbbcabccacabcaaacababaaccbabaabbacbacbbabccacbbcbabacabcbbbcaaaaaccacacbacbcbcacacabacccccccacaacabbaacaabbaabaacabcabaacccbbaabbbbbbcbbbbbccbcbcabccbcbcabbcaaabbcbacbccccaabcbaaabbaacacbbccbbabcccaaababaacccaababccacaacbcabbabaaababbcaaccbccaccaabccbbccbaacabbcaccbcacabbcbcbbabbbccbabaaabcabcbaabacaacbcabbbbabcaabaacbbcaabaccaacbabcacccacbcaacababaabccaaccabbaabcabcacbcaabacabccbbbbbbaabcaccbcbaabaaccbcbabbbcbccabbaabcaacbcaaababbabaabcbbbccabcccccabcccaaaaccbbaaccaccaaaaccbcbabbaccbcbbbabbbacbaccbcbbcbbacacccacabbbccaaccaccacbcbbcacccacbcbccababbccaabcccccbcccbcaaaccbcacbcabacaabcccbaccabacaaacbabbaababcaaabacbbbcccbcbaacbccaccaaccaabacbaccccaaaacabcccbbbccaacbaaacaacbabbbbabccbaabbbaacccbbcbcbccaccbccbbcbcbabcaacabcbbaaaacccbcbaabccbabacacbcbbbacbbbabbbbcbbaccaabcccaccbaacbaabaaccaabcaaacaccaccbccacbcbaabccacacbccbabaaccacabcaaabbaccccbabbaabaccbcccaaaabbaabcaabacbacbbbbaaabbbaaabccabaabbcbabcbaccbcabacaaacaaaccabbabbcabaabcbcacbaaaaabbaaacbcaaacaabbbacabacaacabcabbabbbbcaccaaacabccbcbbcbbcbbbccabcababbabbcbbaacbacccccbbbcbabccaabcabbbccbabcccbbbcbcacccccbbbbcacbababbaacccbabcababcacacccbbabacccabcaaacaabaaabccacccaacaacbcaaababacaaabaaacaccacabcbcaaccabbbcacbbcacaaaccbcaacbbbacaaacabbccaaababcaabcacbbabbccabcbbbbccbbcbcbabaaabccacbcbcaaccccccabaabcabacabbbabbaaabbcccabbcaabaaaaccbabbbabccaaacaaaacacacccbaaabacbcaaabaabccacabccaaabccccacbbbbccacabcbbcaaababcbbbbbabbcaabacccaacbaabbcacbcbbccccaccaacccbbbcbbaaccabccbcabcabbcbbcccbcccacbcbacabbabaacabbbccabcabacaababccbcccaacacaabbcbbaaabcccccabaabbcaaccacabbcccbbcccacacacacaaccaacabcacbabbaccbaccbbacabacacbbacabaabbbbbbabacacabbbbbbabaaacacbabaaaacacabcabbbbcccacbacccbacaaccbbbabacaaacababaaacbcbacbccbcaacacacaabbaacacaabcaccaaabccaabacacabbbccbcbccacccabccbaaccbababababccbacbbaaccbabbcccccabbbbaabaabbbcbbcbbcbcacbabaaabaacacccacaababbbcacaaacccabccaacccabcacbbbbbacbbcaabbacabccccbabaccccaccbababbacbcabbaacaaaaccaacbabbcbaaaacbbcbcbcccbcbbaaaabbacaaaababbbaabacbbbbbcbccbcaaababccacbabaacabbbbcbcabacbbcaaaacaabccbabbcccbbccacbbcccabcbbbcabcacbababcbbbbccbaaabcababbbacccbbbcccbaccbaccbacabcbcbbbacacbbacbcbbcbbacbbaabccbabbacbacbaabccbabbbbccbabccbbaaabacacaacbcccbbbbabababcabbbbcbaaabaccbacbabaabaccbabacaabbccacbcaaccaaacacbccbcccbcccaabbbcbccacbcabccacabbabbcabbabccabacbacaaccabbcacbbbaacccbbacbacabcccbcbbbabccacabcbcbabccbbbcaaabcaaaabaabaacbbabbcaccaaaaacbcaabbbcbbaabcbbccccbacabaacbacbcbbcbcbbcabccbbccbabababccbcabacbcbcccbbcacbbbababccbabbbbbcbcbbccbbbcbbccbcbcacaaccbcbabbaacaccccaaacabcaccbcbbacacccacacbabbcacbbcbcbabbacbcacbcaaacbbbaaccccabbccaacababcbabacccbcbabbcacabccccaabcacaabbcbaacbbcbbabaabcbcbbcacaaacbacacaababbabaabcbaccbcccbbaacbcacbaaacbbcaaabaabaaacbbabccacccbbabcaaabbbccbaaabccbcaacccaaacacaaaaacbaaababaacbcccbbcacccaacacccabaabccacaababbabcacbabcbbbbbacbabcccacabcacaccbcbbbacbacbaaababacabcabbcaabcccabccacabacbaabcbcbacacccacbabacabbcacbbaabababacabcabcbabbaaabbccbccacccbbbcbaabcaacabbabbbbccacbbbcbbaaacbcbccbbcacbacacaccababcbaacacabbcaabaaccacbcaccccbcbabbabcaccccbaacbcabcaabbccbcbaabcbbbbcaaabcccbbbbaccbcbababccccbaaaaccaabcacbcccbbbbccababaacbcbcbbaabbaccacccbcbaacbaacabcacabccaccccbbbaaabcaababbcbbcabababcacbcccacbbaaaaaabacaaaabcbcbacbccbcaccccaacababbcbaaaaaccbabacabbcbcbbccaaabcacbaacbcacaacbcbaacbcabcbaacbaacacaaaaaacccbcaacacbbbcacaccbbcaacccabcbabacccaaacbacccbacccaacbbaabbbbbcbcacacbbaaabbccccaabacbcccbcbcabcacaabacbacbcbaaabaccbccccccaabaabbccbacbaccccababcbcabaacbababcbacabbbbcaacccababbaaccbaccaabaccabababcabccacabcaaacbcbbcccacacbcbacacaaaacccbcaacaacbaacababcacbaccacbccabbcaaaaccacbaaaaabababbaabcbccbbcbaabcaababaaaccbcabcbcabacacbaaabacbaaaabcbbcaaaabacbbaabcbbacaabccbcbabcaaabacbbaabbcacabcaabcaccbbaccacbaaabbbbbacbbbaaaaacbcbbabcabccaccacbaabbaccbbaaabaabcbccabaccbcabbbabcaaaabbaccababbaacccaaaaabbcbaabccbaccaccbbbaabacbaababaccaccacbacabbabcacbccabaacccbccabcacacaacbcaacaccbbaacbcbbbaaccbacbaaacaacbcbbaabbacaabcbccccbbabaaccabaabacccbaaacbbbaabacbcacabaaaaccaabcbacacbccbabacbbcccccababcbbbbcbcccbcbcbcbbbaaacaaaaacacaaaaccbabbbccbbbacbcacbbbcbabcbbbcbacbaacccabbbaaaccabbcababccabbcccbcbabcabacaacbacccacacabaabbcaabaabcaaaaaabbbcbbbababccccabaabbaacaabbaaccbbcccccbbccacbccacaccbcbcacbbcacabcbccabababbcacbcaaacaacccbaaabaccbaaaabcacabcbbcacbabcbacacacaccccaababbbbaabbbacbbaabcacaacaaccccaaaabcccccbcccbabbacaacaacbababcccbaccaacbbbcababbccccaabbaaacabbcbabccaacccabcaccaccaabcccccabbacbccbbbaacbbcbaacaccacbabcacababacaabcaccaaccbcaabcbabbccabacaccbacbccacbcbaabcbabbccabbabccbbcabccaacbbcccaabbaabbbcabcccaaabaabbbacaabacabcbbacbabbcaaababbbbccbacacabbababcaacbbcbccbaabbcbcaabacbcbccbaaaaccaabaaaccacaaabcbcbcbbcbbbacbccabbbbbacccbccaabcaccacbabacccacbacabaaabcaaccacababcaccaaaaacbcbacbbabaacabcbcaacbccccaabbacbcbbaacccacbaccaabbbababcbbacabbbbccaacaacbcabcacabbcaaccaccbacbaacacabcbccabcaccbbabacbcaacccabccbaabbcabbbccaccbcaaccabacaabccacccbcabcabbbbbacccacaaacacccbcacbbcaccabaaccaabbabbabcbccbacaaabccacbbcacacabbccacbccacbccabcccbaccaacbbcbaaaaccbaccbabbbbabacabbcbcbbbabcccbbbbaccbabbbcaccbbaccacaababccabcaaaacaababbcbaaabacacbcabbbccbbacbcbacacabbbbcbbbacabccacbbbaacababbcbbbcbcbacaacbababcacbcacbbbbaccbcabbababcabcbbababaabbabbcccaccccabacaababccaaaaacaaccbacaccbbbaaaacaacbbaaaccaababccbbbacbcacccabccbabababbabacbcbcbbcaabcccacccaacbbaccbbbaabcbccccaaabcbaccbcaccccaacbaabccccccbccbccbabbcacabccabcccabacbbcacaccbabbcccbcabaacaaccbabaccaccbbcababcacabcbbccbbbbccabbccccbaabbbcbcbccbbcbcbcaaabcabcabcabbaccbabcbcbabbababbbbbbacbbcaabcbababcbacbabaacaabbaabccaccbcbbccabcaaabaccabcbabaaaccaacbaacaaccaacbbacbaccbcbccbacaabcbcbacbbbacabbcbaacbaacacbbcbbabbcbbcbcabbbcbccbababcaacacbccbcaabbcccababcaabbbaabcbbbbbabcbbcaacababaabbccaaacbcacbabcbcbabbcbbbbcacacaccaccabbaccbbccbbaabaaaccbbcabccbaaacabcacabaaaabbcaacacaaacbbacaaaccbcbaaabaaaaaaaabccbbcacbabaabbcaaacccacacbcacbabbcaaccacaabcccabcaabcabbabcaababaabbaacaacbcccacbbababbabaaaccbcaabaaaacbacaccacbbbcacccbababcacaacaccbccbabbcabccabcababbbcaccacbbbbccbbaacaccbacabbbaabbacbcbcbcbccbcbaabaaabbabcababbaabbcaabaacccabacaccbbccbabaaacaaccacbaccaabacabbaaabcaababaccaaabbacbbccbcbabababaaabcccabbacbacbcbabaababaababacaaaccabbaacacaacacaabbcbabaacbccbccbcbbccbbaccbaaaccabbcaacbccacbcbcaacbabaaaaaccaaabbcccbbccbcacaaacaabcacbaccabaacbbbaabcababcaaaabaaaacbccccbcccbacbcabcababacccbbbcccacacbaabcabbbcbbbbbaccabaaaaaacbabcacaccbababcbbbacbbbbaabaabcabbababbcacccccbcbbccccaaaccacaccccaabbbcbbbcccacbbaaaaaabbaccccbbabbbcacacbccbbacacbbbcbabbbacbbaabccacbabbbbbacaccbbbacccccccacbcbabaaaaaabbaccacbcbcacbbcacbacaacccbcbcbbabacaccbabcabcbbabaaccaacbacbbbbbccbcbcaccbbbaacabcababaaaacbacacbcccbcbaaaacbcacbbbcacbbccccbbabbcaaaaabaaabcbccbabacabcabcabbcccabacaaacbbaccbbccbbacbabacaacabcbbbabaccbacbbbcacabaacabacbabbbccbbcabcabacbccaaaaabbbabcbcbaccaabccccacabaacacabbbaacbacbcababacaabbbabbaccaccaaccaaacbcbaacabaaccaccabaccaccababbccbcbcacbaccabaacccababaabcbabcbbacccbcabbabcabbcbabaabaaaaabbbbbaabcaaacbcaccbbbccaaabccaccabcbaccaabcaacabcacabccbcaacaaccacabbbacbccbaabbabbbbacbbcbbacbbcbbabbbcbbcbbaccbcaacacaaabcbcccabbacabbcbacbaacbacbbbbabccaabbcbbabcaaabcacaacabccbcbccacbaaaacbabbacbcabaacbbbacbabcacaccbcbcbcbcacacacbcabcbbaabcbabcbcbabcacbabcaabcbababcacccaaccacabaacaabbacbbaccbabbbacbccbcbaaaaaccaaccabbacaaacbacacccaacbcbabacbcbaccabbacaaaabbbcbabaaaaabbbbaaabcabcbcbbcabbacbabbaaacabcbaacbcaaaabaaaaccbcabcccbbaaaaccccbabbaabbbbbabcacbabccbccaacabbcababbaabaacacccbabccaaacbaaabbacacbcaccccbcabacaaacbaccabbaaccbbbbcbacccbcccbacbbaabbababaacbacbbbababcbcaabcbcbcaacccaacbbbabacaccbcbbabbccccbbcbbbabccaaacbccaacaaababaccabaaaaacabbbccaacbabacbaacaaaacbcacbcbbbcaabcaaaababaaababcccbcabcaabbcbcaabaaaccabaaacbacccaabbccbabbbacaaaacaaabbacbbaaaacbccccbabcabbaabcabcbcabacaabbcbbcccbbcacbbcbbcbaababaabbbacbabccaaabacaabcbbbabcccaaaccabaaaacabacbacaabbccbccccbbaabbaccacbabcababccbccaababcbccbcbbcbabcbabbacbabacacbcacaacccbacabbccccacabbacaacacbacaacccccbaacbbbcacacbcbabbcbaababaababbacbcacacbbabbbbbacbbbbaacababbcbbbccbbcbbbabccbbbaabbbbaccabbabcccabbbbbcbcacababbabcbcabacbaaccabcbcbcbbcbcccbabacccaaccbbccbbaabcbcbbbcabbabcbacabcbaababcabcacccacacaacbabbcacababbccaccbcbccbaccbacbcccbcbcacabccaccaaccabaaccccabbccccccaabcbacbacbcccaacacbbcabcabbaabcacbcacbcaccccacaabcbabbbbbcabcaaaccacbbccbbccbcccbabacabbcabbbccccbbbbcacbcabbbcaabbaaabaacaccacbcccaaccacbcabbaaabcaaccccbbbbaacbbabcbaaaacabcbcbcaaacabcacaabaacbcaaacabbcccaabbcccabacabbbaacabacbcacaccaacaaccbbaabaaaacbcccbacbbbbacbcbaccaaabcbccababcbcacccabbbbbbbaaaccacbbacaaabbbcccababcbbbaccbacbaabaacaccabacbcabaabaccbcbcbababacbccabaaacbbbbbbababaacbcbacccaacacaabbbaaaabcababcbcbbaacaabcbacacacacaaabbaaabcabcacbcbacbcaacccaccbbaaccabcabbaccbcbbbbccaccacabccbccaccbccbbcbccbbcbaccbabaabcacaababbacacccbccacbaccabacabcbcbcabcbacbcbcabaabcbbbbbcccbcbaabcccaacaacbbaaccaacaaaaaccabbacabccacabbcabbaaaaabcabcacbbaabbbabbbabaaababbccccbcbcccabccaabbbabacbabcbaabababacbacabcbabcbacaacaabcaabbccacccbbccbabcbbcabcbcabbbacbbccacacacaaacacacccbaaccaaaabbcccbaabcccccaccccacccbabcabcbcbaabaaaacbabccbabccaababcccaabcbbaaaabccbacacbbbaacabccaacacaacbababcaccccabcbcacbaabcbcaabcacabcccaaabcbbbaaccaccaccccaacbbabacccbbbbacaabcaaabccbcabcccccbbcbbcbcbcbabaccbbcccbcbccbbbacacbcbccbbccbaacbbcaabbbcaabcbbacbbababbbaabbcaacccbacbabbabcbbbbacaacacabbcabbbbbbbbabcccaabaaabcaccbbbcacbaaabcaabbaccacccacbaaaaccacbabbbcbacbbcbbbbbbcbbbccbabcaaccbbacaacabaabcbabcaacccbbbaaccacccacabaaacaacacaabcacacaccbbbbcbabcaaccacaaccbcaabccbaabbcbbbaabaacbcbccccabbacbccbbacabbbaccabcacacabccabbcaccabbbbacbcabcacaaabbccbbcbabbacacaaccbabacbacacbbcababccaccaabaccacbcbbbbaaaabacbcacacbaaacabbacaacbbccabbacbacacbaacacbbbccabbbbbaabaabccacacacbcabcacccbcabccccbaabbbaaabbccccaccacbcccbaabccacacacaacabacbbbbbbbcccaaabbabaaacaaabbcaaccccaccbcccbabbacaabbbcccabcbbccacbcaccbcbbacbabbaabaaccaccbabccbbacbbaccaacacbbcaabababbccbbaccccbbaaabaaccacbacbacbcccacbcaccbbbcbcaaaacaaabccabcbcccbaababcabbccbbbcccacabcbcccbabbcaaacbcbcbcacacbabbbbbbacbbccbbaccabaacccbaaabbaccccacbcbbaabbcaacbacabcbccabcabcbabcacabaccaacbacacbabbcaaccbcbbbbaccbcaacbccaacbcbaccccccacbaabcccbcccbbcccacbbaaccbbbacbbcababbcbbaabbaaccbcccbbaabbcccbacaccbbaaababcaacbbcbbabacacccbbbcbbcababcaacbcccbcbbabaababaabbcbaaacccaacccaaccbcbbaacaccbbbbbcbbbbbabcccbaaaaccaacccbbccaacbbccacabaaacabcbbcbcbbbaccaacccaacaaaabbbbbbcaabcaabacacabccbbccabacaccaabccabcccabccbcbbacaacabbbcbaabcbacaaabaacabcaaaacbbcbabbcccaabacabcaabacbbcbbbabccabbacbccccbbccaaacccccaccabcabbacccbbaabcbccbabcbbcbabcbbaacbbcbcccbacbcbbbaaccbbbaaacccabcaaabbbaccacabcaacacaabccabbbaabbcbbcaaaacbcccbccaabbbbbbbbcabacbbbbcbbbbacacbbcbabcbbbaccabbcccabccbacacbcaabcbcaaccabaabacbaccbcaaccbbaaabcacccccaccaabaabccbcaaabcbbbacccabbbccacaabcabcacbaaabbbcabcbaccbbacaaaaacaaccaacabacacaabbbcabbccbbacbaacbaaabbcbabcabbbabbbcbabcabbccabbbbbababbaaabaabccccbbccbbcabcbbacbacbcaaaaacbcaccbaccbabbcacccbcbaccbbbcbbabbaaabbbbabccabccbaaabcbccbcbbbaccababbccccaacabbbcbcacbacbaabbbaaacccbbacbbbcababbccababaaaacccbbaabcbccaaaacbcacaaccbcbbbaccccccaabbbbacbacacaccacaccacabbbacacbcabcbcabccabccacbacbbccacbccaaacbaababbacbcbabbccaabaaabcbabbaacabbbcaccacbbcacabccccacacccaaccbbacabbbaccbaababccacccbcccabcbbaaacbbababcabacbabbbcbabcbbbbbacbbaabacaabbcbabcacacacababcbcbcabbaacaaccbababaaaabbacaaabcaacaccbcbbcbcacbccaaaaabbcbabbabcbbcbbabaabcbbbbababaabcacbbbaabccaabcbcaaaabbaabcbcbccaacaabcaaababcacbcaccaccaaccbacbcaccacaabbbcccabcbcaccaabcbaaaaaacbacbaccacabccaccbbbacbaccbccbcbcaababcacabcbaaaaccbcbaababbccccccaabbbcbcacbaabacbcbabbbabbacaacccacbacbcbbaababaabaaaabbaacbaacabbcbaaaabaabacbbabacbabaabacbacacaccbbabbababccccaaaacaabcabbaacabcabaaaaaccaccbbbbabbccbbabcbcbaccbacaabbbbcaaccccabcaaabacbabcaccccbbcabaccabccbacacacbcbaaaccacaababcaabbcabccacacbcbaacbaccacbaaccaacbccabcaabbaaabaaaabcacbabacbbcacbaaabaacbaaaaaabccaccaaaaabaabcbbcaabbccbaccabaccbcccacacaaabcccbaacaccababccaacabbacaabacccacbcbaacaaabccccbbabbbcbababbbaccccbaabcbbcbaaccabcbaacbcbbccabbabbbabcbbcbccaacaaacbcacacbbcbbccbccaabbcacaaacaccbbcbcabbbabbccaccccbacbbbbabbaabcaaccababbcccabbccacaabcbcbabaaaacacaccbccccaccabbbcbbcbcbccccbcababacccababaaaaaaccaaccaacbacbcbcbaccacbbccacbbcbccccbcccbbccbacacacabccbacaacccbcacbaacabcbcbaccbbbcaacccccacbbaaaaaaabcbaaccaaabababcbacbcbcacbbccbaacabbacabaabaacbbbabcabcccaaaaaabacabaaabcbcacccccbaacbbbbccaaccaabccaccccabbcacabbbbabbbabacccbbaabbcacbcbaccabcaccacbbbabbbabcbccabcacbccbbcbccacaabaabcbaccbbabacabcbbcaaababcbabacaabaaccaaacbbcccaaccaabbbbbbcbbccaacbbaabccacbacccbcabbccaccaccbaababbbcbbcabcbccabccacbaacbcaabcaaacabcbbabbabacabccbcbccbacccbbcbcbccacabbbcccbcbbaabaaababcabcacaabbacbcbbcabccbcccabbcbabcccccaccabcaaabacbcabcbbaaabbbabcaacbccaababcbbbbbacbbcbcacaabcaacacabcacbccccaabacaccbbaaabbbbaaaabbabbacbbacbcacabbbcbacaaabbbbacbaaaacaacbbabcbcaaacaaccaccbcaabcbbbabcaacaaaccccbccabcbacabcaccbbbabaaabaacaccbcaacabaabacccacababcabbbaabacacbaabcaacccccccbacbabcabbcaccacbbacaaaababcbabacbbbabbbabcbabcaaaaaaaccaabbbccabcbaababaccabaaabccacccbbccaccbbbacbbccbacbcabcacacbbacaacabcccacbcbbbcbbbcaccaacbcacababbcabacaabcacacabcaccabcacbbbaaacaaccbbcaacbacaaccbcbcccabababbbcbcbaabbbacbccbbababaccbbaacbbbcaacbcaacaacbccbcbbabcbacabccaaccbbbacabccbbaaacbaabacaccbbccbaacabacabbcbcbacbbbababcaaabcaaaacbbccbbbccbcacabbabbccbacacccbcaacacbbabbbaacabaccccaacacccbaaabbcbabacbacbbbbbaacaaccbbcbbcacaaaabbaccbcaccabacbcbbcaabacccababbccccabbaabcaabaccabbabcaaabccccbbbaccbabcbbbbbbcaaacbbcccaabbcbbccbacaccbbcababaabbcaccbcabbcaacacbcacccaccbccbcbbccacaaccacaaaacbacacacaaaacbcbbbcbabbbcbbacaacaccbcccbbccbcccbcbbaacacaacbcabababbcacacacaaabaabcbaaccaaabbaacbbabbaacabbaaabbcbcabbbbbababbabbcbcccabbabbbaaaabcaaacaabbcccabbacabaacbcbbaaabbbbcaacbcbccacbbcbcbacabbaacbaabccbabacabcaacbbabacccabcabbcbbabcbcaabccbcccacaabccbabcaccbaaabbbcbbbbcbabacccccbcaccabbbbcaabcaaaabaaccabcaaccccccccbabcabccccacabacbbcaccabbccccccabccbcaaaaacaccabbccacabbbabcbcbbcaabcacaabbccbcccabbcbbbbcaabbaababacaaaccbbbcbccbccbacbcaacabbcababacbccbcccbacbcabbabcacabaabcacbbacacabaccbaaabacbccccbcaabcccaabccbacccaacbabccabbbbbbcccccccbccacbabbbabbcccaabcccccbcbbaabaacaaabcabaacababaacbccacbacacccabbcaaabccbbccccbaccaccbbbbabbaaaaaabcbaabacabcbbbaaabcacaaabaccccbcbcabacacabaaaaababcbbbcbbabcaaabbaaabcbbbaccaacaaacaacbababccbbbccbbcabcbcbbbccbcacabbcacacbbbbccabcbaaaabaacbbbbababbcabaaacbccbcaabbcbcbbbacbbaaccacaaabacbacacbbbaaccaccbbbcbbbcbaccccbabaabbbbcaabcccccacaaccbcabacacacacabbccaabbaabbbbabbbbbcaccacaacaccbbbbbaacbbcaaacababaacacbbcacabbcccbbbcbbacaaccbbcacbaccaacabcbabcccaccacabcbcccbbbcccccbcababbabaabcbbbababbacccbcaccbbaabcaacabbaabcccbcbbacbcabcbbcabcccaccabacabcaaacbabcbbcabababccbbabcabbbcbbcacacccbccaacaababccacbbcaaabaccccaccaacaccccbcccaaccaabbcccacccabccacaabcacaaabbccaacbacabbcbabccbcaaacaabccacbccbcbcaaccbccbbbbcccccbabacbccccbbbbbbacacacbbbacbaaccbaaabccacbbaaacccaabaabbccaaaabcabacbaaaccbbaacbcccabaccbcbcccaaacccabccbccaababcbaccabacacbaccbabcabcaabcccbcbacaacbbcbbcbabaaabbbbbbabacacbbccabbcabababccccbbabcccaccaacbbcccbbaababcaacaaaaacbbcccbbabacacaacbcbaabcccababbcabababbabbcbbacaabbbbcaabaacbabcacabcbacbacbcccabacccccbbbacbcabbaabcabbcccaabcaaccabaacacacababcaabcabbbbbaaaaaacccbbccaaabbaaaabccbccabbccbaabbaaabbaacbcacbcabbcabcccacabacababbabcbcaaabccbbaacacabcbacacabcaccccbacccabacbcbcbacabbbbaaabcacccccbcacabbcaabcbcabcaccbbccccbcabcbabcacccccbaaacbcbabccaccbacbcbccbcaccaaaaccabcabababaabcccacabbabccbbbcccbbababcabbacbccbbcacaabababcbbbbabbbcaacbbacbcabbaaaccaaccbccacabacabbbcaaaabbbcbbcbbbcbacaccaccbcabaabaabaabcccbbabcccbaacbccbcbbaaacbbbabbcbcccacacbbbacabacbccbabbaabcacabccaacaccabaacabbcbaaaabcbbbbabcacaaccccbaaccbbbabbbcacabaccbcabbabaacaaababaacccbbcccbabbbaccabcbcacaaababccabaacababbbaacaaababaaabbcaacbacccbcccbbbbcaaababcbcbbacccaaacabcbbaccbacbcacccbacbcacbccaaababbaccbabcbabcccaacacbabbaaccbacaaacbcabbcbababccccbcbcacacaabcacbbaabbccbcbcccabbcbcbbcaaccbcccababbabacaaaccbcabccacccaaaaabcaccbcbccaaaacbcbcbcaccaaaccacccccacbbccabbcabcabacbbabbabbaacababcbacbbbcccccabcccbccabcbbbccaacbccacbcacbcabbcbccaaabbbbccbbabbcaaaccbacabccbababaacabacaacbbacaacabbcabaabaccababaacabbabababcababbbbbaaaabaaccbabacacaaccbbaccbcbcaaaaabcbbbcabcbabbcaccbbbbacccaacbbcbacbaccccbbccaccccaaabaabcbcabaaacbcccaaabbacbabaabaaacbbcaabaacaacbabbcbbbbbbbaabaacbbbaccaaacccaccaccaaabbcbaacbabaacbbbbbbcbacbaaabcbbccaabcbcababbbacbcaccbaabcbccccbaacbccacacbabaacccbbbbbabcabcbbbbcaacccbaccacbbaaabbcbbbacaabcbaaabacbaacbacacbabaaabaabbacbbccacccabcccaccbaccbaabacccbabcabcaccbccbcbaaccaabbacbacbaacabbcaaabcabcccbacbaacabccababbbbcaacccaacbaaacbaaaacbbcbabbcacbabacbaacccbcbaabcabaaccbacbbcbaaccaaaaaaabbaaabbcbcaccbbaaacccbbaccbcabbcabaacaaccbcccccaaacacaabaaacabcbcbbbcabcbccabccbbcccaccaacabaccbbabaacabbcbcbabbbcbbaabbaaabacabcaaaacacccaabbabaccaccbcbacbcbacacabcccbcacbbbcaabbbccccacbbabbabbabaccabcacabaaaccabbbabbcbcbccaaaabaccbaacccabbabbbcbccaaaabcccbabcaabbaacbbbccbbbbcbacabcccbacbcbaabcaabaaacaccacabaabacbbbbaabccbcaaabccccbacbaacaaabccccaccaacbbaabccacbcccabcbaabbbaaabacaaccbabaabccbbbcacbcbabbbbbbbbaccbccbbbcaccbcbcaacccabcabaabbacbbcbacababcbbcbcacacacbbacccbabbbbccbcaabccaccbbabacbabaacccccacbaacaabaccabacbccbbcccbacacaccbbaaacacbcbcbcabacbaccbccbacaaaacbbcbacacbbbbccbcabaaaccabcccccbabbaaccbacabbbcabbabacbcccccbaaacbcbcbbacabccaaabaabccbacccabcaaabbbccbabcbbbbacbbbabaacccbabbcccabacababcaaaaacbbcabbaacaacacbcccbbaccacbbabacbbccccabbbccbbbcbccaabbcabbcbcbbcbbbabbbbabccbaaaacaaaaccaaaaaaababbbccbbaaabbcabbbbacaababbacbbcbbabacacbbaaaacabcbbaabababbbacaacbacaabbabcbbccccbabcbbaaccccabcbccabbbcbbcaabbcbcbbabbaacabcaccacbbbaccccbacccbcaacaabaccaabababaabaacbcbcaccaccccaacbaabcacbbaababbabaabbaccaaacabcbccabbacaaabcbbbcbbaaaabcccacabcbbbcbcbcacaaabaccacababababaaaaabaacbbaacabacaaccabccbacbbcbccbaaabcccabbacabacacacbcabaabbcabcbcacacaacbabcaacaaaaccaacbaabbbbbbbcaabcbcccccabcbcacaaababaaccbbbbbaabaabcbccbabbaabacbabababbaaccbababbacbacabaacbcaaaccaaabbcbcaccccbcaacbcbabcbbccacbccaaabaaccaabbbbbbcccccabbcacbcbabbbcacccbaaabbcbacacbccbacbbbabcbbabcacaaabcaabcbbbaaabcacbbacbbaccbcacbccbabbccbaaabaccacabaacbcbaaaaccbcaabaccbccccabcaacabccaacacbcaaacabbcccbaaacbbccaabacbcbacccaabaabaaccbaaabbccbabcbaaccaacacabbcccbccccabaabcacbcccaabccaaccbcccaaacbbbabbbbcbbcaacccaccbcaaccbccbaacacacaaabbcababbbaccbacbbbcbabcaaacaabbbbbabaccbcaabaccacacababbbaacccabbbbabbaccaccbcbcaaacbbabbbaccbbbcacaaccbcabcaabbacbbcabababaacabcaabcbbabcaccbccbabcbcacbbbbcbcacbcacabaaabcaabababcabaaabacacbabcaacccbabbbaabacbbabcccacccabbabcabcaabbccbabbababbcaccbabcaacbbbaaacacccabcbcabcaaabacbcabcaccbbbccaccbcbabbacbaccbaaaaaaacbcbbaccbcaaabbaacaabacccbbcccaacaaaaaaaaaabacbcabababbbbbbacbbcccbacbbcaabbbbccbaaccbacababacacbcaabbabcccaaabbbbbccaabcbcccabbabcabacaccabbabcbcccbacaaccbbbcaaaabbaacabaccbcbccbccccabacccbcbbccccbaaacbaacacbcbcccaacabbbacbabbcaccabbaabcccaccaccacbcabacbcbabbcbbabbccbccabacbbbacccbbaaaabcccccbabcbcccbccbbbccccabaabcacaacaacaaabacbccababccacacabaabaaaccacccaababcacbcaaaccbacbaaaacccacabbacccaaabbbcacacccbacbcbabacbcabaacccbbccaabbbbcbcacaabcabbccabccacbabcaabbbcbabccaccaccaaabbaaaababccaaaabcacaccabccccbcbacabaabcbcbbcbabcacbcabaacaabbbbbccaabaccacbbbaccacaaaacbccbbccaaaabaaacccbcaabcaacbbccccccaacaccccacbccbcacaabccacacabcacaaaaabaacbbabbcbbcabbbacacbbcbcbcccccabbcbabbabcaaaacabccabbbcacbbacbcbbbaccabaaacabbcbbacabbcccbbbccbbcbcaabcabcccaabcbccaacbcbbcabcbabacabaacccaaccccbbacccabaabacbacbbbcccbabcaabcbccccabaccacbcbcaabbababaaacbbbccaabbbbabcabcabacabaabcbaacaccabcaccccccbcaaacaabbaaccabaacbabcccbcacccabcabbaaaabbcacbbabbcacbcbbcaacacbaaacbacaaccbcbbcacaaccbaacbccaacaacbbbcaabaaababcbcbbbbbaaaaacccccaacbbacbaabaccbccbaabcbbabcccaaaabcccbcccaccbaccccbcbbbaabaccbcaaacacbabbacbbbccabcabacbacaaabaaaacaccbabacacacbbbbccbccbcccbbcaaabcaccacaaabccbcacbaaabbcaacbbccbccabbabbacbbcbbaaaacabbabcbaaccbbacbbbcbcacaabcbcabccacbaacbcbabcaccacaaaccabbbcacccaccbcccbcaaaacabcbbccbcabcbcaccaabbaccbabcaabaabbcaaaaaccacbaacaaaccabaaccbcbaacbcacaccccabaabbacaacccccabccbcabbacbabbacbbcababbbbcbbcbbabbbccabacbbbccbabbabbaccabbaccbaaccbbababccbbcacbacabbccaaccbbccaababccbabccaabccccaacbcabacbacabcabbcbbcccbbabbcacbaccbcaccbccbcbabbacccbabaccbaaacabcacabbccaabccacbaaccbccaabcabcaacaaaabcbbaccacaaabacacabccbbccacaabcaacccaaaabbabbbbabbcabaaacbbcaaaccccabcbacaacbbbbcccccbacababbbaabcaaccabbbbcbacbaacbabbacbbbacbbbacabcacbcabbacaaaabaccbbbaaaabccaccccacbabcbccabccbcaacccbaabbbcaccbbcbabbbacbbacccbabbacbbcaacabaabcaabbbbcbabbccacacbbcaaccbcaccacbcccbbbbbabababcbcbcbaaacaaaaacacacbcbcbcabcabcabcbabbababaacaacabbaccaaccaacbabbccaaabaccccabcccaccbcbcbcccccbcaabbbabbccaaaccbcabcacacbbbbcbaccaaacabacccbccbaacbcbcaccbbccbaabccabcccabbaccacacbaabbcacaaabcaaaabcccbbcbcbaaabaacbbcabaaaaacaccbabcbaccabaacabacbcbcacccbbaccbbacbccabccbbbabbbbabacaccacccabaaabbcccaabccbcacbbabbccbcaccabacbacbaacabaccccaccbacbcacababbacbbbababbbaacaccacaabaaaabcacbabaabbbabccbaaaabaabccbaababaabcaabbbbabbabbcbcbbcbbacaabccbacbbcaccaabccabbbbccccbabbbabbbcabaaabbbaabbbabcaabbbabaabcbcaabaacaccaaacbcbabbbcaaabbababbacbacbcacccbcbccbcaabacacbababbbbbbcabaaaccbcbbbbaaccbccbaccbabcbcccbacabbbcaaacacccaaababcbcbaacaccccccabcaccababacaaabbccccbacccacbabbbaabccacccaacbbccccbcbaaacacabbcabccbaacbacccabaacbcbcacaccbbccbaacacabccacccbbbcacaabcbacacbccaacaabaccccabcbacaabcccaccacbcabaabbaccbccbccaacacaababbcbccabaaaaaacccabbbacbbcaabbbacbcabaaccbccaaacbaccccccbbbbabacbabcabccabaabcbabcaaaacbcbcbabacbaccacbcabccbacbbaabbbccacbbaabcbacabacabbcccabacbbcbccbccababcbbccaaaaaabcbbacababaabcbcaaccbabaabbcabbccccbabaabcabbaabaaabbcbcbccacbcbccabcccbcaaabacacbbaabcabacacccbbcacbccababcbcbcaaaacacccbbaccbbbbbcaccbbcbaaaabacaaacaccbacaaaabcbacbacaccabaabcbbaccaabcbccbbccbabcbaccbaaaacacabcaaabbacaabcbcbbbbccaccabcbbcbbbacabbbbaccbcccbcbbaabcbaaabccaaabcaaabbacaccbbaccabcabacbcbaabcccaccbcaccaacbacacacccbccaabbacccbcbacbbbbabcccbcbbbacbbcbbbacaaaacaacaaccccccbabcbacbabcaacacbabcbcbccaaccaccaaccabccabcbbbcbcbaacbbbcacaababcabaaacbcbaacaabaccaabcbbccbacacacacabaabaaccbbcaaccacabbacacacacbcacaabbbaaaaabaababcbbbcacacbcaabaabaccaccbcaababaaacabacbaaabbacbbaaabbcaccbbabcbaccabbbbbabcaacacaccbbbbbbccbaccbcabccbcbabbbbcbaccbcabcbcccaccbabcaaacccaccabacabaacacabbaacbcbbcbcbacccbababcccccacbbcaaabcaaaabacbacaabacccaccacbacccbabacaccbaccbbacbaaaaabcbbbabbccabbccacbbcbcabbaababbcacacababcbaabbcababacbabababacbcbbbbccccbcacabbbaaabbaabbcacbcbcbbacbabacacacbaacaabbbcabbccabbcbccaaabaaabaaccaaaabbabccccbbbbbbabbbcababcaaacccbbcccbbaaccacaaabaaccbcbbccabbcabcacaaaaaabbbcaabababbcacbcacabacbabcbbaabaaaccbbcabbcacbcacbaacbacbcaacbcbaabaaaccabbaabbaaacababacacabbcbbcabacbbabccccbcbcacaabcacbaccabbbccbbbcabccacabcbaabcbcbaccbccaccbabaccabbacaaabbabbbbbacaabbabcaccbabcacacccbccabacaaabcabbbccbccaacbaccccbaabaccccbcaacaccaabbbabaabcbaacaccccbacaaccbcacababbccaccbbbbccbcabaaabcbaacabbccbaaabcbacabbbacbcbcabbcbacaabcabababbbcaacababbcbcacbabcbaccbcbbccacccbbcaaaabbbabaabcccbaccacaaacccbcaaccbabbaaabbbbabaabbcbababcaaaaccabbcbaabbcabbbbaacccbabcbbcbbbbbcbaccccccccbacbbaccbcccbccbaabaaaabcabccabacabbbababbbccaabcaaacbbbccaccbacbccbaabbcaabbcbabcabacbcbcbcaaacabcacbbccaccaabbbbcbcaabbbbaabbbcacabbbbccbcbcbacaacccbbccbabaaccbcbbbabbbaccbbccccaacacaaabbbaccbcbaabbccbbacabbabbcccbbacacbaaabcbcbbabccabcabcbacabaacaaacccbabbccabbccbbbacbbccaaaaaccbcccbaaacbcbcbbabbbccbcccbccbbabbaacbbbacbaaccacaccbccbbcacaabcacaaaccbbbcaabccbabcbbbbaaabbbbcccbaaabccabaccaabaacbcccccbbcbccbaabbcbbbbaaaacbbacababcabcaababacaababacabcabcbacaacaccbcbaaabcbcacacacaaaacabacacbcabacbbcbcabcbaaaaacaaaabcbcbcacbacbabaaabbaacbcabcbaacccababcaacbbcabccaccaabacabaccacacbcbaabaccccccbccbcaabcbaabbbcaaacaaabcbcbcbbcacbaacaaaabaaabcaaabcbacbcabccccbccaacbabaabbcbccacbcbbabbbbcbacccacaccccbcacbbbbbbacacacbabacbbbcbacbcccaabccbcaccbcccbcbcbabbbaabacbaacbbbcbcaccbbcbabaccbabbccabccacbbcaaccccbbcabbaacbbabaaaabbcbcbbaacaacbbcccacbcabababcaabbabcaccacaaabacabccbccbbbcacccccbccbbaaabbbaaaaccacbaacccacabccacaabababccccacccabcbccccabaaaabacabbbcaaccacccbaabbbacaabbbccbcbbbbabcaabbacaacabacbbcabbabcaababaacacaacbbbcbababcbacbaababababcbcacaaabcbcbcaabbcbbaaaacbacabbbbacccabcbbcabacccbbacbabcbabbccaabbcacbbcbababaaacbbcbbbaabbbaabbcacabcbcbbcabcaacccbaacaacabacaabbaabcbaccbccacbbbabbbbccabaaaababcccabcabcbcbabbccacccbccaacbbcccccccccbccacaacbaaccababcbccbaabaabcbccacbbaaaacbcbccbcbaaabaabaccbcbcbababcbaaccabacaaacabcaaabcaaaaacbaabacaacabbabaccabbabccacbacbbbcccaccaabbaaacaaaacccbbacbccbbbbbcccbcaacacabbaacbaabcabbaccccbaacbbcbbbbabcbcbbbbbcabbacbccbbaabbaabbbcbaccbabbabaccaaabacaccaccccbaacbbabacbbaacaaccccbbccbcbabbaabbabbaccbccaccbabccbbbbccbccaabcacaacabbcbbccccbcacbabcccaababbcaacabccabaacccabcabbbbabcacabbaabbbbbbacbacbbcaaaacabbacbcabbcbaacaaaabcaacacbbccccaaacbaaacbcccbacbabcbccccacabaabcabbaaaacaacbacccbbabbbbcbacababbaccaaccbccaabccacacaccbaaabbcaaaabcbcbababcccbbbaacaacbcaaacabbaccbcbcaacbccbacaaaccacbbcababcbbbccbcaccccccbaccaccabcbbaaacaababbbbcabbbbcccbcaccbbaccabbababbaaacccccbcacaaababccaccbbbccacacabaccccaacbaccccbcbacbcccabcbbabbbcacccbccbcaababcbbccabcbabcbbacabbccbabbbccbacbcaccbcaaabcababbabcbccbcbacccabaababccccaccbccbaacccccbbbbbaacbbacbcaababbcacbcabbccccccbbaaccbbbbaccaccbbbcbcacaccabcbbbbbabaaaccbbcccababcaaacbacaaaccaabaacaccbacabcbabacbccccbbcbbabcbcacbbaaaaacacbbccacaaccbcbccbaaaaabbbbbcabccaabcbccbcbbcaacbbcabccbabaaccaacbcacbaacaccacbbcbcbcabaaabcaabbcbaaccaccccccaacbcaabbcaaabcbbbcaaacbbaacbbbccaababaaaccbbbbaccbccabababbcbcbbccabbccaaaaaabacccbcabcbacbbcabccccccaaaccabcccbbaaaccccaaaabbccbaaabbcacbccaaaabbccbbbbcabcabbbccccccbcabbabacbbcbaaabababcbaccccccabbbbcacbcbbaccbbabccaacabbccaaccaccacbabbacaccacbbcabcabbbbababbacabcbbbabbcaccbabbbaaccaaaaccbbbbaabcbcbbcaaabcccbcbcccbbccaacccbbaaabcbabbbcbbcccaaacaaaaacbaacbcbaababbcccaabbabcabbccabaabbcaacaaacbcccbcbccaabaccbaaaaabcaccbaaccbaacacbccaaaaaccccaccbcbabcbbaaaabcabcacaaccbcaccabaacbbabbaacbcbabaccaabccbcababcaacbbccbbacbabacabbcbaabbbbbccbcccbbabbabacbccccbbaabbaccbcccbbaacaabaacbcbabcaabcacabbbbbbbcbbccabcbbbcbccccbbbbbaabccacbaacacccbcabbbcbbbbcbacbcaccabcbcbbccabbbaaaacbbaaaabbccbaacacaccabccbcbaaccbbccbaaacabbcacacbcaaaabbccbabccbaaaccbccabaacbcccabbbbaaababbbbbbbbababcbbabbabbacbccbccacbbaabbabcccabbbcacaccacbcbabcbcbcbbbbbacabbbcacbaacaabccabcccbbaaabaaabacbccacbbaaacbabcabcabbcaaacbbbaaacacbbbcaabcabcbbabcbcbcaacbabccabaaacbccaccccabbacacbbababcbacccbcaacabbbcabaabbbbbabbcccbababccbbaacbabaccbbcaacccaccaccbcbbcabccbbbaabaaccbbaaabaaabaccbccbaccbcaccaaaabcbacbbabbcccaabccbbcbabccaccacaaabcbabcbaabcbcabaaacbccaabbaacaaccbaccaabcbcbaabcbbcbbccbccbbbbaccaccbacbcbaaccabcbabbbccbbcaaabbbbbbbaaabbcbaaacbaabaaaaccbcbabaabbbbabaababacaabcaabababcbabcccaaababbcbaabbabcccaaabcbbaabbbcacaabcabbcbbbbaabcabbbbbabacbbabacacabcabccbbcacbbaacbabbabbbabcbcbcbcbacacabbbcbcabbabbaacaaaabaaccaabcbbbaaaaacacbbccbaabaabcbbacabbbabbcacbabbbbbabaccbabbcbaaaaacbabbbacbbccbabbaaabbccbabcbaccacaaabcbcccbbbbbaacacaaabaacacbaababbacccbabbcabcabcabcbbcabbaaaacbbaabbbcbbaacbaccabaaacccccccacabbbbccabbcbaabaccababccccaccaaaacbccbcbbbbcbccaabbaccccbacbabccbbababbbbcbcbcbbcbcabbbccaaccbbbccbcccccccbcbabbcaaccbbccacccbcaaaccabacbccbcbaaaabccacaabbbbbbacaacccbacbaabbaaaaccbbaabaabccbbbaaaacaabaababaacacbcaacbacabacacbccbcaacacaabaccabbcaacabbacbbabaabbccbbbabccbcccabcaaccbabccccbcbaabcacccbcbbcbaccbcbcbcccbbcbcbbbcaccaaabaacccbccbaabcbbcbacaacbacaaabccacabcaccbcbaabcbaccbaccbaaacbabbabccaccbcbcacbababbcabbcaabbbcbcbacacaabcccabbcaaacbcbacaaacbacaacbcababcccbabaacbaabcacaaabcbaacbabcbcaaaaaabbccacaaabacbaccbcbabbbbcbabbbccaaccbacbbabcbbbaccaaaacbbcacacaccabbaaccacabbaabbcaabccaaaaabcacacbaacbbacaacabacabcacacaabcbcbccbaabbccaaabbcababcbabcbbccabbabcaacaaaabccbbabaaaaccbbacacbbccabbcbccabaaccababbcabcbcaacbbcbcbacbabaaacabbcbbbbcbaabccbaaaabbaabcbacaaaacabaacaaacaacbcbcaabacbabcaccbacbbcabcaababcbbcbacbcbacbaccbbaaabcbbabbaaccbbbcbacbbccbacabaccacacacacaaccccbacbcaccaabcbbcababcacaabbcccaacbcaabcccacbaaccccbccccbbcbccabccabcccacaaacaccaccbabccbacabcbabcaccccbbccbcabaabbbccabbaabccaacbcabbcaacabcbaaaacacaccbcbcbaccccbccbcbababcbcacbcbbbbaccccbaabbabacbbcbbcbcaaacbccaaabbacacbcabcbcbacbbaaaaabcccaacbaacacabbabcacbcbccacacccabaccbcbccbaccbbbbbcbcbcbbbabbbbbcbabbaacbacbbcbcaabbbcaacbbabbbbaabbacbaabbcaabccacacbaaacaccbabcaccbbcbbcabbbabacbaabbcbbbacaaacbabcabbaaabbbccbaacabbabacaabbabaacbacccaaccccbbbbaccacacabccaaccbcacabcbbacccccaacabaaaccbcaaaccbcacbcabbcabcaaaabbcabbcbaccbbaccaaacbaaabbccbccbacbaaabccabccaccacbaaabacccbabbbcbcacaccbbccaacbababcaacabbabcbaabbcabaaabbbbabcacbcaaabbbcbaaabaccabbbacacabbbababcbccbacaabaaababbbaccaacabaaccccaaccbccacbbcaaabbcbaabcccaabcabbaccccccbbabcacbbbbbabbcacbcccbcacccaabbcabbbacabbaaabbacbacaaabbabcacabbcbaccabbabbaccacabbbacbcaaabbcabcabcccaaccbacbbccaabbcbccbaccccbbbbbaabcacacacccccbbacabaacacccbabcbbcaccababcbbbacabacbbbacaacbcacbbacabaccaacbbccabacacaaacaaababbbbacacbacbbcccbbbcbccaacccaacbaacacaccbaccbcbaabbcababcbbabcaccbcccaccbaacaabccbcabbcbcbbabaabaacababababcbccacaaabbcbbcccacabaacbbbbcbbabaaabbaababaabacbabcaacbbcbabbcbbbabccbcbbbabbccaacaccccabbcbbbbcccccccabcaacaabcbcabacbacabbccbbbcbabbbabcacbaaaacaaaaabcbabcaabacbbbbabcbcacccabbabcabccbbacaababaaaacacaacbabaaacccaabaabcacabacbacababbaaccbabaabcbcaabbcccaaaaaabcabcbaabcaabaaaacccacaccbaacabacbbaaacaaabcbcccbcbaaccabbaabbbcaaacaabaaccabcbcccaacaccccbcbaaacccbbccbccbbcbcacbbbabbacbabcccbbabcbacaccbccabccaccaaacabccccbbcaccbacaaacabbcababababbcbcccbacccaccbccacccacaabbcbaacbbacccbcbbaacacabbbccabcbbabbccaabccabccaacacbabbabbaababaacccbcbabacacccbcbacaabbcaacabbccbcaccacabacbbccbabacbccbbbcaacccabbbbcbaaabacaaacaabbbacaccaabbbbaacaaaabbbababacaaabbbbcacacbbcacbcababaabaccbaabcacbcccbbcaacbacacabbbcbbbbbabbccccbbbccabaacbacbaaaacaacbccbcaaccabaaaacccababaccbbbbccbabacbcacbbaaabbabbcbabacbcacbbabaababbbababaaacbaabccacbbabbbcbbbcccccccbbbbababcababbbaacacabbaccaabcaccacbcbbacbaaabaabcaabcbacabbacbccbabbbcbccccabcbbcbbacbccabbabcaccbacbcabbabbaabcbabcacccbbaaaabbcaccacbaabacbabbcaabbcacbcccabcbbabcbaacacbcacabbccccccaababbacbabbaaabcccbbcbbcbcbcaccaaabcacabbbbbccbabbacbccccacabbcbcaaccacbbabaaaabcbbabbbcababaabcacaaaccbacbbbaacaacabacbabacbcaccbcbbcabbcbccbbacbaaaabbcaaccbabcbbccbcbbbbbaccaabcabcacaacbbabcabacbacbbaaaaacccaaccbcaacabbabbbbbcbbabccaaaacbbcbccbbaacccccbacacacbbaacababcaabcacbabbacabbcaacaaaabbcccaaaabcabcbccacbcbaccbbaacccababbaaccbcaaabbabccabaaabbacabaccabbcbabaaacacbcccbbcbaabccaacbacaacbabccacbaacabbbacbaaccbacabaababbbcaaacccbbacacbababbcaabacccbcbcababbbbbcbbcbbabbcbbaaacbcbaaccbacccbaacccaccbcaaccbacaaaccbcaacacbaaabbcacaabbbacbaabaacacbbcacbababcaaaaabbcbbaacaccaababbacacbaaacbabacbaccccaaccacaaccaccacacaaccacaccccbcaabbaabcbbaccbcaaccbaababccbbaaabcbbbbaabbcaacbccbbcaccaacbcbacccbacaacbccabbcabcacbaabbaaabcbcbabaccbcaccabbcacbaababccacacbaabacbcaabbabbbacaaaabbabcabbcacbbbaccbacbcbcbbbabbcbcabccbacababbcababbbbbbbbbabbcbccacabbcbbabcabbbaababaabbabcaacabacbabbbabbcababacbbababcbbcccaabbbcaccabcacbabcaaccabccbcbccccacbbcaaabcacaaccbacbbccababcbbabbacacbabbcbbacabababababccacccababbcccbbcbcccbcaacbacabaccabccabacaacabcbaabbbbabcccaaacaacccbaabaaacacccbbaccbaccaaabcabbaccabbaacbababcacbbbbcccccbaaabbcbbbcbacababacaccacabbcaaacacababbcaaacccbbbabbacacbccaaaaacabbbabbbcbabaaaaaccbacbaacccbbaabbcccbabaaabbccaaccacbcbbabcbaaacbccacacbbccabaabaaaabacbaabaabbbbaccbcaacbaaabbbbbcbaacbababbcacaaabaccbcaaacbccacaacccacbbcabbabbacbbaabcaacbabacbaabccbabbaabababcabbbaaccaacbcaccbbbcbbaacccacbccaabccacbcbacacabcaabbcbcbcbbbcabcabbbbbbccccbbcabccaacacbbccbbbaacccbcabcacbaccabbbacabbaabcaaaaccbabababbbcaacbbbabacccacbcccbcbbaaacbcaaaccbacbccbccbcbbabababaabbababaabbbabccacccabbbaabcaaaacaccbabcbbcbacbcbbaccacabbcbacbcbcbaccbcbacacccbcbcabcabcaccaacbbcbcbbbabbbcabcbbaacacbccbcabcaccaccaaccccbacacbcacaaacbaccbaabcbbcbcbacbacacaaababbacbcabcabcacababcbccbcbacbcbacabaabcacacaaaacacababbbababcbcaccabbabaaaabccacaabbccccccacccccacaabbbabbbcbbccbbbabbaaccaabbcccaabbbbbbbabcaabbbbabbbcbbccabaacabcbcacccabccbbcbbcccaabbabacccccaacbccaabababbbbccaaababacaaacbabcaabbacbcbbaacabcbbaacacbbacbaaaacbaacabcbabaacabccbccbcbccbcbbbaacacacaabbabaacacaacbcaacacbaaaabaaaabcaccabbbbcaacaaaacbcaccabaccbccbccacbcbcaaabbacacbbacbcabcabcacbbaabaccbbcaaabcbbacbacaacacbabbacabcccbcbcbcacbaacbbbacbcbaabaaccacbbabaccacaaccabaabbccbcccabcbaabaaabaaabbaacbacacbabbbabbaaabbcbcaabaabcaabaccbbcbabcbcbbcccaabcabacaaacccaabcbcacbccacbbacccbbaacabaacbcbbaaaccbcccacabcaaaabaccbccbcbcabaacbbcabaaabcbcbacbcbacbccabaaabccbbbaabbbcaabbcbbcbacaabcaabbaaabcacccabcbccccbbccaacccccccacbabcbacbabcccabbaaccbabbabbacabbbbbcbabbaacaacaccbabcbabaaaccbaccaabbacbbcbaabbababbccbccbbacbabbcbbabbcabcbccaacccbacbbacaabacbcbbbaccaaccbacabbccacacbbcaccbbabbcbbbcaabaacacbabccaacaabaababbcbccacbbacbbaabbcbbabbcbabbacaaaccccaabaabbbbbcbbcbaaacacaabbacbabbbbaaaabbabcbabaacbacaaccaaaabacbcaabbbbbbcccbccaaccabacabbbaccbcbcabbcaaaacbbacacbabbabbabcbcaacacccacacbcaababbccabcbbacacbccbacbccaaaaccacaccaabaabababcbbcaacacbaabaaacbaaaabaaaaacbabcaaccccaccbcccababcabccacacbbabcbabaabaccacabbcbbabcbbcbbcccaacccaabcaaaaaabbbcabbacabbcbccacababbaaabbcbaccaaabbbcabcabcaabaababcbccbbacccbaabcccbcbabaccbccbcbabbcabbbaaabaccaccbaaaccbcccacbccbbaaaacbabcabbbcccabccbacaccbaacacaaabbbcacabcaaacabcacabcaccbcabcaccbccbbbbaaabbcaccacaacacbababbcbcbacbbbbccbacaccbaccbacaacbcbcbacbccbcababbccbcbccbacbccbbccbccabbcaabcaabbabccbaaabccaabccbbbbcbacccaccabbaabababcacbacccabacbbaaccbabaabbacabcaaacabbacaabcccaabbbbcbabbccacacaaabababcabbaabbbcbcbcbcacbbbcacaabaabbccaaaaabaacbacaababbcbbbaaabbccbcaabcbccaaabaaaacbbababaacbbcbabaaaaccbbcaabbaacabaacabaacbacbaacbcacaaccbcaccaaaaacaaacbcbbacbabacababcbcaabcaacabbabbbbaaaaacabacaccacacbaccabbcaacbbbcaabccabacccbbababbcbcabaaabbbaabacaccaaccabcaacbaaacbcaaccbcabbcccbcccacbcbbaccacacbcabcbcccaccbcccbbbaabcbacbabcaabcccbbbcabbbcbacaaaacbcbabacacacccaaaccbcacabaacbcccbbbbacacbbaccccbcbbacbabacabcbbbcbcabacbabaccaacabcabacbbbccbbbaccbcbccbabbacbcbccacbaaccaabcccaaacbabcbccabbbacbcbaababbbabbbbcbcacbacbababbaccabbaaabbcacccbabbaccaababbaacaacbcbabaacacbbaaacbbcabaababcabcaaaabbcbcbcbccaacaacbbcbaaababbbbacbabbabcbcaaacaacabacbbbaaaabaccbccbabbbaaaccabacbcacccacabcaabaccbababccacccababccbccccabaaaaccbcbbbccccaabccbaabaaabcccaaccababbbcbbabaaabcabcbcaaacaccccacaaacabbbaaaccbbbbbbcbccccbbbbacbabccaabbabcacbacacbcacbbbcbcaabbbcbbbbcbacaaabbcaaabaabccccabcacaacaacaabcabbaacbccabcbaaaabcbbcabbcbcbcccbccbbcabcacbaaabababcbaaaaaccbbcbbcbccbbaaccbacabbbcbcabcbaaabcaacbbbcaaaabcaccacbaccbbabaacabccaaabbacccbbbaaabacbbbcaccbaacbbacabaababbaccacbaaabbaabcbabbcbbaabbcacabccccaacccccbbbbccbacbbbbabbcbbbababbbccacaacacbcbaabaababaacbbbcbcaaacccccacbccacabcaaabbaabaaaabcaaaaaaaaccacacaaababcabbcabccabcbbcacabbaccabbbcacccaccabbbcbccbaccccbccbacbbbcaaacccbcbcbbbcaabaabaabcaabcbbbcacbbbccbabacccaabbcacccaacabcbcaacacbbacccababacaaaaccccccccacbaccbccccbacaccbacccabaabacacbacbccaaacacaccaaccacbbbbccacaabaaabacaacbabcacccacbabbbcbbbbabbaacbccabaaabccaaaabccbcbbbbaaacbabcbbacababbaccbaaacbbabbaccbccccccbaacbabbbaabaaacbabbaabaacabbbbaaabaabababbaaabacbacaaabcacabaaaabbacbaaabcaabacaaacbccaabacccacabcbccaaaccacbaabaaacccaabcbcccccbacccbbaaabcbcacbbcabbbbaaccbacacbcabaccaaaaaacbacabccccbbbcaacacacaaabbbacbccababbaccbbbcccbccaccabacabcaccbcccbaaacaccccbababcccbbccabbcbbacccabcabacacbccaccccbcaacbbababcabbcbaacaccaacabbbaabbbacabcaabcabbaaccbccabaccabcbcccbaababaaaaaacacaabbcabcbbbacabacccabcaacaccacccbcacaabaaccbabcccccaabbcaccacacbcbcabccabbbccabbccaacaacccbccaabcccaabaaccacbbccbabaabaababcccbcbcabbababccbbbccaacbaccacbbaabacbacbccabbccbaaccbbaabbbbcacabccbcbbbcccccacbabacaabacbbcbbcaacbbbbbcacccbcccaccaacbbabacabbbcaccccabccaaacccbbacccbbccbacacabacabcabbccabaaacaaccbccccabbabccabbacaaccccbbccaccccacaaacaccbccccaacbabcaabbbcaabcbccabcccacaacabcaaacccccbaccbbababbcababcbbcccaaaabccbcccaacacaacbbcbbbacbabbccccbaabcacbaabacacbbcababccabcbcaacaccccabaaabbaaaabacbabacbbbbcbaccccaabbbcaaccbbccbcccaaabbcabcaacbccbaacaccacbaaaaaaaaaccbacacbaabbbbaccccbaaccaaaaaacaccbabaacacbbcbaacccbcccbabbbbaaccbccaaccbcabcaccccaaacaaccacbccabbaabbbbccbcccabaacbaccabababaaacaccbbcbcbbccccccabcabababcbbccbaccacaacabbcccbabaabaaabaaccabccccbcccaacbacaacbabcccbaababacbccbccbacabcbcccccbbaaaaaabbbbbaacbbccbccaacaacabcacccacbccbbcbaccaacccaacccccabcbbcacbccabcbbcbcbacccbcabaabbabccbbcbcccabcabcbbaaabbaacabccbcaaabbcaacccbcbacaaaacaabcccbccacbbbcbccabbaaccccbabcbbbaaccabaacbbacccbaccabccbaccbccacaaccaaabcbbccccbacacabaccaacaabcacccaccacabbcccaacbcccbbbaccbbccacaacabcccccbaabbbcabaabbbacaccbbccaabaaabbaabcabbbbcbccaabcacccabbcbbbabbcaaacbcacbaccbcbcabcacccababcbbbbcaaabaabaccababacacbaaaccaabccabbcbababacabcabbbbabacaacaaacaaacccaabacbcacbacbccbcacbbccbcbabbbcabccabcbababbbabacbacaacacbaaacacababacbcbcccbbbcabacccbababbbbaccacaccbccbabbcabcaccccccaabcbbaabaacacabbbcbabcababcaacbcbbbabbbcbbbbcbcbccabacacaabcbbcabcacabaacaaabbbaabacbbccabbaacbcaacbaabcaacbbcbbcaaaaaacbccacacccacacbcbaacbabbccbbabbacbaabbaacacccabcccaacabacbbccaabccababcaacacbccabbbbacaabbccabbcccccaaaabcacaaacccbbcaacacabacbbaabccacaaabaaaaabaccbacbbabaaacbaacccbccccbcbbabbacbbbcccccacababbabbabbbbacbccccacbcccbbccaabbbcaaabaccacccaabcccbacbabcbbbabaacccacbbbbbabaabccbaaacbccabacacbabaacbccabbbcacccabbabbccbaabbababbaacacbabaabacbcbbbaaabaababcbcbbcabacbbcaacccbaabcbcbacbbbcccabcacacbcabbcbabbabbcabbbcbbcabacaccaabbacaaaccacbbabccbcaabbabcccbacbcabaaacababaabaabccacbccabbcbbbcccccbbacbcbbacaccacababbbcbbabccbcaaccaaaacbbbaababcacbbbbcbbacaacccccbbbaaaccbbcacaacbccaabccbcccbcaaabccbcaabaaababaaaaabcabaccabbcbaabccabbbabccacbaccbaaccbbbabbcccbbbbabbaccbcccbccbbacbcacbcaccbacccbcbcbbacacccbcacabcbcabaabaaabbaccacacccaaaacbacacabbaaccbbcbabcbbcccaacbbbcaabbccbbaaccaacbacbcbbacacbacabaabcbaaacaacbcabbbcbbaaabbccbbacbcccaabbcababccaaacaaabbaaabbccbbcacbccbaabcaccaccccaccbbccbaabbabccaccbaaaabbbbcccbaccaaaaacbabaabacbcbbbbacccacccaabcccabcccabccbabbcacbaaaccaacbabacbabbabcbaccabccaabccbcbcaacccbcacaaababbbbcacbbcacccabbccbacbbaababccacacaaabbbbbbcccacaacbcaaaaabbaabcbaaabababbbbbbabbaabcacaababcbcacbcacbcbcccaaabcbccbabcacababccbabcbaccbcbcaccaaabbcbabcccbbaacccaaacccbaabcabbcababacbabababcbbabbbacacabbaababbbaabccbaccbccbbcacacaacbccccabaabbbbbcbcaaaaaabacbbcabacbabaaacccccabbacacabcabaccccbabcbcabaaacbbaccccbcccacabbbcbaacbbcaaccccbbbaabaccbcacbabbbcabaacbccabbcccbacbbccaabcbacbcbbbabbbcbababcbcccccbcabacbaccbbaccbbcbaaabbcacbbccaaaabbcbacaccbbbbccbbbabbccaabaacbcaacbbcabacacabbcbcbcabaccaccabacaccabcacccccabbcbbcabaabacaabaccbbababcbaabcacbabcabcaabbabbbccccbbbabaccacabcbaccbacbbcbcbcccaacccbbbabaccbcacbbbaccbbbacbcaacabbcbcbaaacccacacbccccababccbbcbbbccbaabababcaabbabbbbabacbbcaabccabcabbcbabbacbbabaaaababbabbbcabbbccbbaaabccbbcabbcbbacbcabcccbabccabbaabcbbcbaccccbcbabccbaacaaacbcabacbbaccbaacacbcbbcaacacaabcbbcbbbbbcccabccacccaabccbcbabbaaabccbabacaabccbacbcacabbaaacaaaccbcababaccbcacbabaaaaaaccccbabbabbccbbaaaccbacccabcaabbccbaabcbccbaacaccbacabcbbaaabaaccbbaaccbabbabcbacbaaacacaaaabbbbabbaaaaccacacbcaaaabacbababacaacaabccbaacbcbbbacbbbbcbcabbabaccaccabacbbcabbbabcaaababcbbcabcccccabccacacbbccbccacabbcbcbababaacbcacbcbacabcacacaacbccacccacbbbaacacaaaaccaacbbcbcbcaacbcbbacaaaacbccbbcacabcbcbcacbccbccbaccbaaabbccccbcbabcacabbccbbcccccccaaababcabcbacacbaaacaacbacbabccbbcbcaaaacbaaabcbbcccbbacbbabbcabacaabbbabaccaaacccbccbcbbaaababcacbbbbaaaaacaababbabacbbacbcbcaccaccbccbcbbbcaccaababcacaaacbbaaaaccbaaabaacabcaacacbccbccbaccbcccbaaacccacabbcabbaacbcccaacaaccacbbbbbcbbbbcbcccabcbccbcaaacaaabacabbcabbbaaacaccabbcccccabacbcccbabaacaccabbbaaabaabcaaabbccbaacaaaabcbabbbabbbbaacaaccabbbbabbabcbbacabbcccacbabcacccbccbcaaabcbbaaabccaabacbcacababaabccacacbbacaaccbcbabacbccbbbababacaabcabbbbacacacabaabbcabaccaaacbaabaccbccbacaaabaaccaaccaabbaabccababacaaccccbbbaaacccacbabcacbbbbcbbaacabcabaaccbbbccccbcccaacbaccbcbaababbccccaccacbccaacaabbccbcbcacaabbabaccabccccbbaccccabaaccaacacaacbcaabbccabaccaccaaabcabcaccbccabaaaacbccbccbacaaacabbbabcaacbbbbccccbbbbcaacbbacaabbbbcabbaaccccaccacccbaacabccccbcaacbcaccbcaaccbbbaaabaacabccbbbabbaccbaaabaabbaabcbacaabccbcbaacabaabaaacbbbbbaabaabcccccbccccabbabacbcbcbbbccbccccccabaccbbbcaababbaaacccbcbacaacccccbbcabacacbbabaacbbbcaaabcacbbaaaacaaabcbaaacacbcaabcaabcabbbcabacbccacbacaacaabaaccbaabccacccaabbcccbacbcbbccbbcacbaaccacbaabaaabccaccacabaabcbbcaabccbaaaaabacbaaacaccaaccabcacbaacaabbabbaacacbccccbbbcaabcaaaaaacbbacbbbacbcbcbbacaccabbababacbcbbccbbcbcbaabbabcccbbbccabbaaacaabacaaacbaabcbccaabaabccbcbabcaaacbababaaaacbabacccabbccbbaabaaccabbccabccbbccabbbacbcaaacbbcccaaaabcccbbaaacaacbababbabccaacccbaaccbabacccabaccbcbbbbbbbbcccbbabbcbbbababaaaccccbbbaaacbaccabbacbcbcbcbaacabbcbaabaabacaaabcabcaacbcbaabbaabbcbaccbcbaacacacbabcbaabcacbbbaabccaaacabbcbcbccaacbbacbbccbabbccaaabaccbacbabaaabaabaaccbbbacbcbabbcaaacbcbabccccbaccabcccaaabaababbcaaccbcaacbcbbaccbbcbcbcbccababbbcbaaaaacbbaababcaaabccaacabbbaaabbbccbabcbccccbcabbaccbabbccabbacbcabaaccbaabbbcacacbbbababcbabcbcccacbcaabaccbcabcccaaabbbbacaabcbacaaaaacabacabcbabacbabbacccacbbbbbbbbbaaccccccccbccbabccacbbcaccacabbacabaacbbbbbcbbbbacaabaabbacacbccbabacbababbccccbabbaaccaaacbaaabbbabbabcaabcbcccbacabbaababcbacaaccccbbbbcbcaaacbcacaabacccbbccbbacbabbbcaccacbacbcbbaabcbccaaaccccaaaabbaababcccbacccbcbacaccabaacacabbabacbbcccacbaaabcaacbaaabbbcbaaabbbcabcaacccaaacaabccccbabbbaacabbbabbabbcabcacbcabcaaccaacabccccccabbabccabaaacbaacccacabbbbccaccbcccabbaccaaababaaabbbbabcaacabbaaabaacbcaccacbcabcbcbcaccbbbabcbbaaabbabcccbcaacaaacbaaacbcabaabccccabacbcabacbbcbacbcccbabcaacbbabccaabacccbbcaaccbbbacbabbbababcacabbccaccbbcacaacccaabccaababbbbaabaccacbccbcbbcbcbabbccbababbabcbaabacaabcbbccbbcbbabbaacbaaaacaaaaababbbccbbbbacabacaabbbaabbacaaaacaaccbbacccabbcccbacbbbcbabccabbccbbbbcabccbbacaabbabbcbaacbbcbababbcbabbccaabcbaaccabababbaccacbacbccccbccaabcbbbaabababcbccaabccbbabbabacabaaaabaabcacaccaacbcaaacccbcbaacccbabbabaabccbcabaabbacbbbbcbbbcaaccbcbbcbbacacbcbbcccbbbbaabbcacacbabcbabbacaccbabcabaccaccabcababacaaabccccabbbabbabcbcacbcabcabbcacaacccaaaaaaccbcacbcaacbaacccaacaabcacabbbaccaaacbaacaaccacabbbabbcbaabbcaccbcabbcabcbaaccaabababbcacbbaaabbcbaacabbbccccbbacaaccbcabbabaacccabbbbccbbccabbcacbcaaacaababaccaababcccabbbccacbcbabacaabccccccbabbccbabbacaacbccccbcaacbcbccaccbacaccaccbbcbbacaacbbbaaabacbaaabcabbccaabaccaabccccbbbcbcbbcbcbaaabcbccbacaaaabcbcbcbccabaaacabaaaacaaabcbcccaacacbabccbbaaccaccbbaabacaaaacbacacababbcbaaccbbaaabbaacbabbcaccbcabbbcacaaabcbcbbbbbcabaabacaacbcbaccccaabcabcaaababbaaccccbcbcabccaabbbccbabcaccbcabaaabbaacacccbccbabcaaabcaaacbbaccacaabcacccbcbccbaccabbaccacabbaccacbcbcccbcbbcababcabbacbbbbbbcaaabbbbcbcabcaabacacbabbcccbbcbcbcbcbbbccbbabaacbbacacbbbcacbccccabbbcbbaacacbcbcababbcbabcbaababbacbbbacacccabcbaaaaacaaaaacaabcbcccccbabcacacccbbacbaaacaccacbaababacbcaabaaabbbacabbcacbbaacacbccaabbcbbbacaaaacbbbccabaacabbbaabbacabccbaabacbcbacacabbacaaababcbabcccbcbacbcbaccaababacccbcabcabbaabbcbccbbbbabacbcbbbabbbcaccccbbcbabbabcbaaababbcaabbcbbcaacacaabccbbabcbbcaaacbcbabaaccaaaaaabbaaaaccbbbcacbcacbaccacacccaabcbacabababbcbccbbaacbaaabaabcccbabbcbabcaaccbbacbccbacbacbbcccaacabbbcaacbaacbcccacabbbbaccaaacbaacaabaabccbcaacbaccacaaababbcabccabbacacabbaccaabaacbcacbaabcacabbabbcbcccacaacaaaaababbcbaabacaabbbcaabacacbabbcacbcbbbacaacaaaacbaaababcabccacabbcbbbbcaabaaabacbbcccaacacbabbcaaabbcbabbbcccbcbccbabcbaabcbcbbccaabaabbbacabbcbbbabaaaaabaccaacaabbaaabbcbcbcaccbbcccaaccbaabcacbabcccbabaccccabbbcaaaababaacbaabcaabcaabacccbcbbbbaaccaaabcbcacacaccbccbbcccbccbaaacabaacaccbcbacbcabaaacacbbbcbaabbbbcbcaaabcbbcaaccbcbbbabcbabcbabccbcaacaaabacacbabaababbbbabaccacbcaccabbaccbbbbaacaabaabacbcbbccabacaacaccabbcacbbcacaacccccbabbabbcaccbbbbbacbacaaabbbccbbbcbbbaaccaabacccacababbbbbcabbcccbacabaabcbbbcaccaaccbbaacbaccbabbbaaccbbbcbcaccbbbabbacacbbbacccccacccccbaacbccaacaaabccbabbbcbbbbacbcbcabbbbacbbbbacabbbaaccacaabcacabaaaccabcccccaaaccacabccbabbccccbbcccabbcabbaacbabacbcbaaccaccaaabbacaacacbacccaaccccbaaacacaccabccabcaaaccbbbcaacaaabbbccaccbabcaabacbacbbcbbababbaabbbaabccccccabbcccaabbabcacccccacacbaabababbaacacbacbabbbbaaaaabcbccabaccbabacccbbbbbcbccbbcbcacaccbbccabccacccbaaacacbccaaccabbccaaabacaabcaaacacaaccbcbbbbcabbabcccbacaaaabbcbbccccabbbbcbccaaaaccaacaccaabccbaabbcbaccbaaacccaabbbbcacaccaacabbaaaaacaaccabacbbcbccabbcabbbbababaaabbcbaabbabbbacbbcaabcbacaccbbbbbbbcaabbbcbbbaabccbaabbacbcaabacaccabacabbabacabbacccbabcbcaaabbbcaababbaaaaacacccbccccbbcabbabacacbabcbcabbcccacbbcabacbaccbcbaaacbaaacbacbabccabacbcabcccabccbacabbaccccccaabcbbcaccabbcbbabbbbaacccccacbbbabbacacccbaaabcccbaacaabbbccaccbaaabcbacabbacccabcacccbacbcabcccabbbbbaaaacbacacbcbabaabbbbcaaaaacbbaccaaaabcaaccaccbcabcacbaaabcbacaacaaabbcbccacababbcbaaabcacbccaccacbcccbbacbcbacbbabacccaaaabaccbbacaacacaccccacbaaaccacaacccbbbbbcaabbcacbacccbcbcbbacccabccbcaababaccbbabaaabbabcaaacacaccaccaabbccbcbbcacaaabababbcbbaacbcbcabbccbaacbcabcbabaabbabcbcabacabccabcaabcbabaaabbcbacbaacaabacaccacaaabbbacbcbaaccabbbbaccaaabbcbbbbaacaccacbcacabbacaabccbbccbbcbccccacaacabacaababaccabbbccbbbcccbabbccbaccaacbccbcaacacacbbacbbcbbbaaaacbccacacabbcccababcacbccbaacabcbaaccbbabccabbabbccbbaaccbbaacccaaabbcbbaccbacababcbccbabbcaacaacbcaacbaaacaaabbcbacabcaaabbcaacbaaaaacaabccccbcabacabbabbabaacbbbcaaaabbccbbaacaacbbcbcccacaacbccabbcaccabbabcaccacacbbccbccccabcabcabccabaaabcbaaccacacbabbcbccaaacbbcccbabaababcbabccabacbcbccccaaacacaaccbacbccbbbcbccbcbaacbbabbbbcababccbcaaccccbcbbccbbcbccacbcbbbacbbcababcccbbacaabaabcbacbbcaaaaccccccccabbcbcaccbbbaababccaacbabbabbcbcccaccbbbabacabbbabcacbbbbbbcccbaacaccbbaabbaccccbcbcaaaaabbcaacbaacacbbaabaabacaccbbaabacaccaccccacbacaabbbccaccbccaacabcababbcbaacccbbaaccaacbaabbabcbbbcabbcaacacacbcaccaaaacacbcaaabbbcabbbbbaaccaaabbabbcccbbbccaaabaaaababacaabcabcbbbbcbcccaaacacbaacbcbabaabbabaaaaacacabbcccabacccacaaccacaacbccbbccccbcaccaacaacabbcaccaababaacbbbaaccababccbbcabcccbabbbcbccacababbaaababbbccbacabacbaaaabbcabaaacbcbcaccccabcacbaaaccacbacbcbcabbccabcacccccccbbbbbbaaccabccbacaccbcabacbbccacaabaacacaabccacababbacabbcacacbbaccacbbbacbbccbccabbccacabcbaacbbccaccbbbccbccbcabacbcacbbaabbabbbcaacabcccbbbbabcaaababacababcaccbcbbcabbbbcabbaccaaacabcacbbbcbacccbacbbbcababaccbcaabccaabccaccaaabbccaacacccccbaacabcccaaabccbacbbccbaabbacbcaccbaabcacaacaaaacbccabaccacbbaacbbbbababacabbabcaaaabccbcbabababbcccbcbbbcaccccbabbbaabacabbbbabacacabcabcbacabbccbcccbabaacababaabbaabacbcbbcbccaccccbacacababaaaaacaccccacbcaaaccccaccbcbacccbbacbbcbcbccbaccccaabbcbcbaaccccaabcccccbbbabacbbbcaaaaaabcacaaacabaccacacbaccbcbccacaaaacabccbcccbbaaaaaabbaabacbbaccbbaaabbccbabcbcabcbccacaacaaccccbccacabbccaaabacabcbbaccabbacccaacabcaaacbccbbcacbaaccaccccabbaaababaccacbbabcabbccccbaabcbcbbbacbbcacbacacaaacbbbcbbacbaccbbbbaabccbcbacbacbbaaabbbccbbcbbacabacabaccbabbcabccabcbaacbcabacaaaacbbccccaababcabcabcbbaacbccaaccbcaccaabaaabacaccabababccbbcccccccabcbbbbbccbcbbcacbaaaabbbcbbcccbbbcccbccacbacacaccabccbacababbbacaabbabacbabccaaabcacaababcbabcaabcbcaaabcbbbbabaaacaacabcaaabaccbabbcaaccbbbaabcccabcacaaccbcabaccbcaaabbbaabcbaacaacacacaaccbbcaccbbcccbccaaccaaaaccccacbcbababccaaacaaacaccaabbbbbbcbbaabbabbcabbabaacbaaababccabaaccbababbcbabababcccaacbcaacaaababcbccaabacbbbacabaabaabbbaaacbabaaaccbaccbaaacbbcbcbaaabaaaabbbbccacbcacababcbccbbbbacbccbacccbccaccaacbcabbcccbabcccbcbbbcabcabacabcabccbcaaabbbcbacbcbbbabcccaaaacbcbaacaaabbbaaaabccaacccababcacbbacccabaccaaabbccbbaabcabcbaaabccccabaccbcbcaccbbbccabccababcbaaacabbabcabbbaacbbaacbbcabcabcccbcaaaacbbcbacacbccbaabaaaabbbcbaabcccbcaccccaaaacbcccacbcacabababcbbabccbcccccbaabbccabacbabbcccbbbbcaaabcbbaccbcacabaabaaacacbaaccaccbaaccaacbccbabaaccccccccaccbaaabbcaabababccacaccbaaccbcccbbabbccababaaccccccabaccaababcaaacbacbcbcacbcbacaabacacabaabcaabcaaccacacbcaccbcaccaacaababbcbbccbccccccbcccbbcbaabcaaaabaabaaacbababccbaaabbccbbcabcbcbbacabbbcbaacccaabcacbabccbbcbcbbacaaabacccbaaacbccacaacacbcbbcabbaccaaababcbcaacbababccacccccacbccbcabbbacabbcbabbcabbaacccaabccbbabbbabcabbcabbbcacbaaaccaccabacacbacbccabacaacbabbccbbbcbcacbaaaabcaacbcabcabcbccacacbcababcbbaccacbaabaaccacaccbccacacbaacbbaaaaababaacbbcaabbcccbaabcabaaabcbbbbabacbbababbbbabaaababcccccccbbabcbbabababbcacbbbabbbaaaabacbaacaaacccbabacbbbaccbaabbbbbccabbccacbbabbbacabccaaabbcccabaccbacabbaabacccaccbabccbbbacabccabbbcbccccbaabcaaccabcaaacaaacaccaabbaaabbbbcccabbcabccbccabbbbcbcbcbcccabaaaaabbbbcacabacccccacbbbcbbaccbcbcacccabaaccacbcacabcabbccbababababcccbbbbabaaaaacbbcbcaacbaccccbbbcacbabaaabbbcaacaccbaabaaccabacccbbbcbccbacabcbababcbaaaacbbaaaabaacbbbcaacbcbbbccccbcaccbcbaccacbbbcbbcacbacaacababcaacacbcabbcabccbbcbcabbaabaabbbcbbaabaccabbacbccbaccacbbcababbccaabaaaababacaabaacbacbbccbbcbacaaababcaaccbcbcaabaaccbcaccbccabcbabbaabbcaacccabbcbbbabccaacbbbbcbaabaacccabaabbcccbbaabbbcbbcabbcaaaacacbbcaccccbacbacbcbaacbaabaccaacccccabacbabbcbbacbcbbabacacbaacbbbbacabccbbabaabbaaaaabaccaaababcabaacbbcbbccabacabbcabcbcbaaacaabcabcababbacacbacbccbcbbccacbcabcbbababacbccbbcabbbabaaccbbabcbbcbcccbcccabcabbcaaabcbcaaabcaaccbcbbbacabcbbbbccbbcbcaaabcbcabaaacabcababbabbcabbbcabbabccacbacacabacbbbaaaacbbcbacabaccabcccbabccaabccbbbabaabbcbbcacaccbabbabaaacbbcaacbaaababaacbccbabbbabbcaabbbcbccbaaababcabbaccbaacccacaabacaabbcabbcacbabbcacabbbccccbbaaccaaaccbcaabcbcaabbcbccbcbbcccbababaaacaccbcacaccccabcbaccbcabababcbcbcbbbbabbbbcabccacabcaaacababaaccbabaabbacbacbbabccacbbcbabacabcbbbcaaaaaccacacbacbcbcacacabacccccccacaacabbaacaabbaabaacabcabaacccbbaabbbbbbcbbbbbccbcbcabccbcbcabbcaaabbcbacbccccaabcbaaabbaacacbbccbbabcccaaababaacccaababccacaacbcabbabaaababbcaaccbccaccaabccbbccbaacabbcaccbcacabbcbcbbabbbccbabaaabcabcbaabacaacbcabbbbabcaabaacbbcaabaccaacbabcacccacbcaacababaabccaaccabbaabcabcacbcaabacabccbbbbbbaabcaccbcbaabaaccbcbabbbcbccabbaabcaacbcaaababbabaabcbbbccabcccccabcccaaaaccbbaaccaccaaaaccbcbabbaccbcbbbabbbacbaccbcbbcbbacacccacabbbccaaccaccacbcbbcacccacbcbccababbccaabcccccbcccbcaaaccbcacbcabacaabcccbaccabacaaacbabbaababcaaabacbbbcccbcbaacbccaccaaccaabacbaccccaaaacabcccbbbccaacbaaacaacbabbbbabccbaabbbaacccbbcbcbccaccbccbbcbcbabcaacabcbbaaaacccbcbaabccbabacacbcbbbacbbbabbbbcbbaccaabcccaccbaacbaabaaccaabcaaacaccaccbccacbcbaabccacacbccbabaaccacabcaaabbaccccbabbaabaccbcccaaaabbaabcaabacbacbbbbaaabbbaaabccabaabbcbabcbaccbcabacaaacaaaccabbabbcabaabcbcacbaaaaabbaaacbcaaacaabbbacabacaacabcabbabbbbcaccaaacabccbcbbcbbcbbbccabcababbabbcbbaacbacccccbbbcbabccaabcabbbccbabcccbbbcbcacccccbbbbcacbababbaacccbabcababcacacccbbabacccabcaaacaabaaabccacccaacaacbcaaababacaaabaaacaccacabcbcaaccabbbcacbbcacaaaccbcaacbbbacaaacabbccaaababcaabcacbbabbccabcbbbbccbbcbcbabaaabccacbcbcaaccccccabaabcabacabbbabbaaabbcccabbcaabaaaaccbabbbabccaaacaaaacacacccbaaabacbcaaabaabccacabccaaabccccacbbbbccacabcbbcaaababcbbbbbabbcaabacccaacbaabbcacbcbbccccaccaacccbbbcbbaaccabccbcabcabbcbbcccbcccacbcbacabbabaacabbbccabcabacaababccbcccaacacaabbcbbaaabcccccabaabbcaaccacabbcccbbcccacacacacaaccaacabcacbabbaccbaccbbacabacacbbacabaabbbbbbabacacabbbbbbabaaacacbabaaaacacabcabbbbcccacbacccbacaaccbbbabacaaacababaaacbcbacbccbcaacacacaabbaacacaabcaccaaabccaabacacabbbccbcbccacccabccbaaccbababababccbacbbaaccbabbcccccabbbbaabaabbbcbbcbbcbcacbabaaabaacacccacaababbbcacaaacccabccaacccabcacbbbbbacbbcaabbacabccccbabaccccaccbababbacbcabbaacaaaaccaacbabbcbaaaacbbcbcbcccbcbbaaaabbacaaaababbbaabacbbbbbcbccbcaaababccacbabaacabbbbcbcabacbbcaaaacaabccbabbcccbbccacbbcccabcbbbcabcacbababcbbbbccbaaabcababbbacccbbbcccbaccbaccbacabcbcbbbacacbbacbcbbcbbacbbaabccbabbacbacbaabccbabbbbccbabccbbaaabacacaacbcccbbbbabababcabbbbcbaaabaccbacbabaabaccbabacaabbccacbcaaccaaacacbccbcccbcccaabbbcbccacbcabccacabbabbcabbabccabacbacaaccabbcacbbbaacccbbacbacabcccbcbbbabccacabcbcbabccbbbcaaabcaaaabaabaacbbabbcaccaaaaacbcaabbbcbbaabcbbccccbacabaacbacbcbbcbcbbcabccbbccbabababccbcabacbcbcccbbcacbbbababccbabbbbbcbcbbccbbbcbbccbcbcacaaccbcbabbaacaccccaaacabcaccbcbbacacccacacbabbcacbbcbcbabbacbcacbcaaacbbbaaccccabbccaacababcbabacccbcbabbcacabccccaabcacaabbcbaacbbcbbabaabcbcbbcacaaacbacacaababbabaabcbaccbcccbbaacbcacbaaacbbcaaabaabaaacbbabccacccbbabcaaabbbccbaaabccbcaacccaaacacaaaaacbaaababaacbcccbbcacccaacacccabaabccacaababbabcacbabcbbbbbacbabcccacabcacaccbcbbbacbacbaaababacabcabbcaabcccabccacabacbaabcbcbacacccacbabacabbcacbbaabababacabcabcbabbaaabbccbccacccbbbcbaabcaacabbabbbbccacbbbcbbaaacbcbccbbcacbacacaccababcbaacacabbcaabaaccacbcaccccbcbabbabcaccccbaacbcabcaabbccbcbaabcbbbbcaaabcccbbbbaccbcbababccccbaaaaccaabcacbcccbbbbccababaacbcbcbbaabbaccacccbcbaacbaacabcacabccaccccbbbaaabcaababbcbbcabababcacbcccacbbaaaaaabacaaaabcbcbacbccbcaccccaacababbcbaaaaaccbabacabbcbcbbccaaabcacbaacbcacaacbcbaacbcabcbaacbaacacaaaaaacccbcaacacbbbcacaccbbcaacccabcbabacccaaacbacccbacccaacbbaabbbbbcbcacacbbaaabbccccaabacbcccbcbcabcacaabacbacbcbaaabaccbccccccaabaabbccbacbaccccababcbcabaacbababcbacabbbbcaacccababbaaccbaccaabaccabababcabccacabcaaacbcbbcccacacbcbacacaaaacccbcaacaacbaacababcacbaccacbccabbcaaaaccacbaaaaabababbaabcbccbbcbaabcaababaaaccbcabcbcabacacbaaabacbaaaabcbbcaaaabacbbaabcbbacaabccbcbabcaaabacbbaabbcacabcaabcaccbbaccacbaaabbbbbacbbbaaaaacbcbbabcabccaccacbaabbaccbbaaabaabcbccabaccbcabbbabcaaaabbaccababbaacccaaaaabbcbaabccbaccaccbbbaabacbaababaccaccacbacabbabcacbccabaacccbccabcacacaacbcaacaccbbaacbcbbbaaccbacbaaacaacbcbbaabbacaabcbccccbbabaaccabaabacccbaaacbbbaabacbcacabaaaaccaabcbacacbccbabacbbcccccababcbbbbcbcccbcbcbcbbbaaacaaaaacacaaaaccbabbbccbbbacbcacbbbcbabcbbbcbacbaacccabbbaaaccabbcababccabbcccbcbabcabacaacbacccacacabaabbcaabaabcaaaaaabbbcbbbababccccabaabbaacaabbaaccbbcccccbbccacbccacaccbcbcacbbcacabcbccabababbcacbcaaacaacccbaaabaccbaaaabcacabcbbcacbabcbacacacaccccaababbbbaabbbacbbaabcacaacaaccccaaaabcccccbcccbabbacaacaacbababcccbaccaacbbbcababbccccaabbaaacabbcbabccaacccabcaccaccaabcccccabbacbccbbbaacbbcbaacaccacbabcacababacaabcaccaaccbcaabcbabbccabacaccbacbccacbcbaabcbabbccabbabccbbcabccaacbbcccaabbaabbbcabcccaaabaabbbacaabacabcbbacbabbcaaababbbbccbacacabbababcaacbbcbccbaabbcbcaabacbcbccbaaaaccaabaaaccacaaabcbcbcbbcbbbacbccabbbbbacccbccaabcaccacbabacccacbacabaaabcaaccacababcaccaaaaacbcbacbbabaacabcbcaacbccccaabbacbcbbaacccacbaccaabbbababcbbacabbbbccaacaacbcabcacabbcaaccaccbacbaacacabcbccabcaccbbabacbcaacccabccbaabbcabbbccaccbcaaccabacaabccacccbcabcabbbbbacccacaaacacccbcacbbcaccabaaccaabbabbabcbccbacaaabccacbbcacacabbccacbccacbccabcccbaccaacbbcbaaaaccbaccbabbbbabacabbcbcbbbabcccbbbbaccbabbbcaccbbaccacaababccabcaaaacaababbcbaaabacacbcabbbccbbacbcbacacabbbbcbbbacabccacbbbaacababbcbbbcbcbacaacbababcacbcacbbbbaccbcabbababcabcbbababaabbabbcccaccccabacaababccaaaaacaaccbacaccbbbaaaacaacbbaaaccaababccbbbacbcacccabccbabababbabacbcbcbbcaabcccacccaacbbaccbbbaabcbccccaaabcbaccbcaccccaacbaabccccccbccbccbabbcacabccabcccabacbbcacaccbabbcccbcabaacaaccbabaccaccbbcababcacabcbbccbbbbccabbccccbaabbbcbcbccbbcbcbcaaabcabcabcabbaccbabcbcbabbababbbbbbacbbcaabcbababcbacbabaacaabbaabccaccbcbbccabcaaabaccabcbabaaaccaacbaacaaccaacbbacbaccbcbccbacaabcbcbacbbbacabbcbaacbaacacbbcbbabbcbbcbcabbbcbccbababcaacacbccbcaabbcccababcaabbbaabcbbbbbabcbbcaacababaabbccaaacbcacbabcbcbabbcbbbbcacacaccaccabbaccbbccbbaabaaaccbbcabccbaaacabcacabaaaabbcaacacaaacbbacaaaccbcbaaabaaaaaaaabccbbcacbabaabbcaaacccacacbcacbabbcaaccacaabcccabcaabcabbabcaababaabbaacaacbcccacbbababbabaaaccbcaabaaaacbacaccacbbbcacccbababcacaacaccbccbabbcabccabcababbbcaccacbbbbccbbaacaccbacabbbaabbacbcbcbcbccbcbaabaaabbabcababbaabbcaabaacccabacaccbbccbabaaacaaccacbaccaabacabbaaabcaababaccaaabbacbbccbcbabababaaabcccabbacbacbcbabaababaababacaaaccabbaacacaacacaabbcbabaacbccbccbcbbccbbaccbaaaccabbcaacbccacbcbcaacbabaaaaaccaaabbcccbbccbcacaaacaabcacbaccabaacbbbaabcababcaaaabaaaacbccccbcccbacbcabcababacccbbbcccacacbaabcabbbcbbbbbaccabaaaaaacbabcacaccbababcbbbacbbbbaabaabcabbababbcacccccbcbbccccaaaccacaccccaabbbcbbbcccacbbaaaaaabbaccccbbabbbcacacbccbbacacbbbcbabbbacbbaabccacbabbbbbacaccbbbacccccccacbcbabaaaaaabbaccacbcbcacbbcacbacaacccbcbcbbabacaccbabcabcbbabaaccaacbacbbbbbccbcbcaccbbbaacabcababaaaacbacacbcccbcbaaaacbcacbbbcacbbccccbbabbcaaaaabaaabcbccbabacabcabcabbcccabacaaacbbaccbbccbbacbabacaacabcbbbabaccbacbbbcacabaacabacbabbbccbbcabcabacbccaaaaabbbabcbcbaccaabccccacabaacacabbbaacbacbcababacaabbbabbaccaccaaccaaacbcbaacabaaccaccabaccaccababbccbcbcacbaccabaacccababaabcbabcbbacccbcabbabcabbcbabaabaaaaabbbbbaabcaaacbcaccbbbccaaabccaccabcbaccaabcaacabcacabccbcaacaaccacabbbacbccbaabbabbbbacbbcbbacbbcbbabbbcbbcbbaccbcaacacaaabcbcccabbacabbcbacbaacbacbbbbabccaabbcbbabcaaabcacaacabccbcbccacbaaaacbabbacbcabaacbbbacbabcacaccbcbcbcbcacacacbcabcbbaabcbabcbcbabcacbabcaabcbababcacccaaccacabaacaabbacbbaccbabbbacbccbcbaaaaaccaaccabbacaaacbacacccaacbcbabacbcbaccabbacaaaabbbcbabaaaaabbbbaaabcabcbcbbcabbacbabbaaacabcbaacbcaaaabaaaaccbcabcccbbaaaaccccbabbaabbbbbabcacbabccbccaacabbcababbaabaacacccbabccaaacbaaabbacacbcaccccbcabacaaacbaccabbaaccbbbbcbacccbcccbacbbaabbababaacbacbbbababcbcaabcbcbcaacccaacbbbabacaccbcbbabbccccbbcbbbabccaaacbccaacaaababaccabaaaaacabbbccaacbabacbaacaaaacbcacbcbbbcaabcaaaababaaababcccbcabcaabbcbcaabaaaccabaaacbacccaabbccbabbbacaaaacaaabbacbbaaaacbccccbabcabbaabcabcbcabacaabbcbbcccbbcacbbcbbcbaababaabbbacbabccaaabacaabcbbbabcccaaaccabaaaacabacbacaabbccbccccbbaabbaccacbabcababccbccaababcbccbcbbcbabcbabbacbabacacbcacaacccbacabbccccacabbacaacacbacaacccccbaacbbbcacacbcbabbcbaababaababbacbcacacbbabbbbbacbbbbaacababbcbbbccbbcbbbabccbbbaabbbbaccabbabcccabbbbbcbcacababbabcbcabacbaaccabcbcbcbbcbcccbabacccaaccbbccbbaabcbcbbbcabbabcbacabcbaababcabcacccacacaacbabbcacababbccaccbcbccbaccbacbcccbcbcacabccaccaaccabaaccccabbccccccaabcbacbacbcccaacacbbcabcabbaabcacbcacbcaccccacaabcbabbbbbcabcaaaccacbbccbbccbcccbabacabbcabbbccccbbbbcacbcabbbcaabbaaabaacaccacbcccaaccacbcabbaaabcaaccccbbbbaacbbabcbaaaacabcbcbcaaacabcacaabaacbcaaacabbcccaabbcccabacabbbaacabacbcacaccaacaaccbbaabaaaacbcccbacbbbbacbcbaccaaabcbccababcbcacccabbbbbbbaaaccacbbacaaabbbcccababcbbbaccbacbaabaacaccabacbcabaabaccbcbcbababacbccabaaacbbbbbbababaacbcbacccaacacaabbbaaaabcababcbcbbaacaabcbacacacacaaabbaaabcabcacbcbacbcaacccaccbbaaccabcabbaccbcbbbbccaccacabccbccaccbccbbcbccbbcbaccbabaabcacaababbacacccbccacbaccabacabcbcbcabcbacbcbcabaabcbbbbbcccbcbaabcccaacaacbbaaccaacaaaaaccabbacabccacabbcabbaaaaabcabcacbbaabbbabbbabaaababbccccbcbcccabccaabbbabacbabcbaabababacbacabcbabcbacaacaabcaabbccacccbbccbabcbbcabcbcabbbacbbccacacacaaacacacccbaaccaaaabbcccbaabcccccaccccacccbabcabcbcbaabaaaacbabccbabccaababcccaabcbbaaaabccbacacbbbaacabccaacacaacbababcaccccabcbcacbaabcbcaabcacabcccaaabcbbbaaccaccaccccaacbbabacccbbbbacaabcaaabccbcabcccccbbcbbcbcbcbabaccbbcccbcbccbbbacacbcbccbbccbaacbbcaabbbcaabcbbacbbababbbaabbcaacccbacbabbabcbbbbacaacacabbcabbbbbbbbabcccaabaaabcaccbbbcacbaaabcaabbaccacccacbaaaaccacbabbbcbacbbcbbbbbbcbbbccbabcaaccbbacaacabaabcbabcaacccbbbaaccacccacabaaacaacacaabcacacaccbbbbcbabcaaccacaaccbcaabccbaabbcbbbaabaacbcbccccabbacbccbbacabbbaccabcacacabccabbcaccabbbbacbcabcacaaabbccbbcbabbacacaaccbabacbacacbbcababccaccaabaccacbcbbbbaaaabacbcacacbaaacabbacaacbbccabbacbacacbaacacbbbccabbbbbaabaabccacacacbcabcacccbcabccccbaabbbaaabbccccaccacbcccbaabccacacacaacabacbbbbbbbcccaaabbabaaacaaabbcaaccccaccbcccbabbacaabbbcccabcbbccacbcaccbcbbacbabbaabaaccaccbabccbbacbbaccaacacbbcaabababbccbbaccccbbaaabaaccacbacbacbcccacbcaccbbbcbcaaaacaaabccabcbcccbaababcabbccbbbcccacabcbcccbabbcaaacbcbcbcacacbabbbbbbacbbccbbaccabaacccbaaabbaccccacbcbbaabbcaacbacabcbccabcabcbabcacabaccaacbacacbabbcaaccbcbbbbaccbcaacbccaacbcbaccccccacbaabcccbcccbbcccacbbaaccbbbacbbcababbcbbaabbaaccbcccbbaabbcccbacaccbbaaababcaacbbcbbabacacccbbbcbbcababcaacbcccbcbbabaababaabbcbaaacccaacccaaccbcbbaacaccbbbbbcbbbbbabcccbaaaaccaacccbbccaacbbccacabaaacabcbbcbcbbbaccaacccaacaaaabbbbbbcaabcaabacacabccbbccabacaccaabccabcccabccbcbbacaacabbbcbaabcbacaaabaacabcaaaacbbcbabbcccaabacabcaabacbbcbbbabccabbacbccccbbccaaacccccaccabcabbacccbbaabcbccbabcbbcbabcbbaacbbcbcccbacbcbbbaaccbbbaaacccabcaaabbbaccacabcaacacaabccabbbaabbcbbcaaaacbcccbccaabbbbbbbbcabacbbbbcbbbbacacbbcbabcbbbaccabbcccabccbacacbcaabcbcaaccabaabacbaccbcaaccbbaaabcacccccaccaabaabccbcaaabcbbbacccabbbccacaabcabcacbaaabbbcabcbaccbbacaaaaacaaccaacabacacaabbbcabbccbbacbaacbaaabbcbabcabbbabbbcbabcabbccabbbbbababbaaabaabccccbbccbbcabcbbacbacbcaaaaacbcaccbaccbabbcacccbcbaccbbbcbbabbaaabbbbabccabccbaaabcbccbcbbbaccababbccccaacabbbcbcacbacbaabbbaaacccbbacbbbcababbccababaaaacccbbaabcbccaaaacbcacaaccbcbbbaccccccaabbbbacbacacaccacaccacabbbacacbcabcbcabccabccacbacbbccacbccaaacbaababbacbcbabbccaabaaabcbabbaacabbbcaccacbbcacabccccacacccaaccbbacabbbaccbaababccacccbcccabcbbaaacbbababcabacbabbbcbabcbbbbbacbbaabacaabbcbabcacacacababcbcbcabbaacaaccbababaaaabbacaaabcaacaccbcbbcbcacbccaaaaabbcbabbabcbbcbbabaabcbbbbababaabcacbbbaabccaabcbcaaaabbaabcbcbccaacaabcaaababcacbcaccaccaaccbacbcaccacaabbbcccabcbcaccaabcbaaaaaacbacbaccacabccaccbbbacbaccbccbcbcaababcacabcbaaaaccbcbaababbccccccaabbbcbcacbaabacbcbabbbabbacaacccacbacbcbbaababaabaaaabbaacbaacabbcbaaaabaabacbbabacbabaabacbacacaccbbabbababccccaaaacaabcabbaacabcabaaaaaccaccbbbbabbccbbabcbcbaccbacaabbbbcaaccccabcaaabacbabcaccccbbcabaccabccbacacacbcbaaaccacaababcaabbcabccacacbcbaacbaccacbaaccaacbccabcaabbaaabaaaabcacbabacbbcacbaaabaacbaaaaaabccaccaaaaabaabcbbcaabbccbaccabaccbcccacacaaabcccbaacaccababccaacabbacaabacccacbcbaacaaabccccbbabbbcbababbbaccccbaabcbbcbaaccabcbaacbcbbccabbabbbabcbbcbccaacaaacbcacacbbcbbccbccaabbcacaaacaccbbcbcabbbabbccaccccbacbbbbabbaabcaaccababbcccabbccacaabcbcbabaaaacacaccbccccaccabbbcbbcbcbccccbcababacccababaaaaaaccaaccaacbacbcbcbaccacbbccacbbcbccccbcccbbccbacacacabccbacaacccbcacbaacabcbcbaccbbbcaacccccacbbaaaaaaabcbaaccaaabababcbacbcbcacbbccbaacabbacabaabaacbbbabcabcccaaaaaabacabaaabcbcacccccbaacbbbbccaaccaabccaccccabbcacabbbbabbbabacccbbaabbcacbcbaccabcaccacbbbabbbabcbccabcacbccbbcbccacaabaabcbaccbbabacabcbbcaaababcbabacaabaaccaaacbbcccaaccaabbbbbbcbbccaacbbaabccacbacccbcabbccaccaccbaababbbcbbcabcbccabccacbaacbcaabcaaacabcbbabbabacabccbcbccbacccbbcbcbccacabbbcccbcbbaabaaababcabcacaabbacbcbbcabccbcccabbcbabcccccaccabcaaabacbcabcbbaaabbbabcaacbccaababcbbbbbacbbcbcacaabcaacacabcacbccccaabacaccbbaaabbbbaaaabbabbacbbacbcacabbbcbacaaabbbbacbaaaacaacbbabcbcaaacaaccaccbcaabcbbbabcaacaaaccccbccabcbacabcaccbbbabaaabaacaccbcaacabaabacccacababcabbbaabacacbaabcaacccccccbacbabcabbcaccacbbacaaaababcbabacbbbabbbabcbabcaaaaaaaccaabbbccabcbaababaccabaaabccacccbbccaccbbbacbbccbacbcabcacacbbacaacabcccacbcbbbcbbbcaccaacbcacababbcabacaabcacacabcaccabcacbbbaaacaaccbbcaacbacaaccbcbcccabababbbcbcbaabbbacbccbbababaccbbaacbbbcaacbcaacaacbccbcbbabcbacabccaaccbbbacabccbbaaacbaabacaccbbccbaacabacabbcbcbacbbbababcaaabcaaaacbbccbbbccbcacabbabbccbacacccbcaacacbbabbbaacabaccccaacacccbaaabbcbabacbacbbbbbaacaaccbbcbbcacaaaabbaccbcaccabacbcbbcaabacccababbccccabbaabcaabaccabbabcaaabccccbbbaccbabcbbbbbbcaaacbbcccaabbcbbccbacaccbbcababaabbcaccbcabbcaacacbcacccaccbccbcbbccacaaccacaaaacbacacacaaaacbcbbbcbabbbcbbacaacaccbcccbbccbcccbcbbaacacaacbcabababbcacacacaaabaabcbaaccaaabbaacbbabbaacabbaaabbcbcabbbbbababbabbcbcccabbabbbaaaabcaaacaabbcccabbacabaacbcbbaaabbbbcaacbcbccacbbcbcbacabbaacbaabccbabacabcaacbbabacccabcabbcbbabcbcaabccbcccacaabccbabcaccbaaabbbcbbbbcbabacccccbcaccabbbbcaabcaaaabaaccabcaaccccccccbabcabccccacabacbbcaccabbccccccabccbcaaaaacaccabbccacabbbabcbcbbcaabcacaabbccbcccabbcbbbbcaabbaababacaaaccbbbcbccbccbacbcaacabbcababacbccbcccbacbcabbabcacabaabcacbbacacabaccbaaabacbccccbcaabcccaabccbacccaacbabccabbbbbbcccccccbccacbabbbabbcccaabcccccbcbbaabaacaaabcabaacababaacbccacbacacccabbcaaabccbbccccbaccaccbbbbabbaaaaaabcbaabacabcbbbaaabcacaaabaccccbcbcabacacabaaaaababcbbbcbbabcaaabbaaabcbbbaccaacaaacaacbababccbbbccbbcabcbcbbbccbcacabbcacacbbbbccabcbaaaabaacbbbbababbcabaaacbccbcaabbcbcbbbacbbaaccacaaabacbacacbbbaaccaccbbbcbbbcbaccccbabaabbbbcaabcccccacaaccbcabacacacacabbccaabbaabbbbabbbbbcaccacaacaccbbbbbaacbbcaaacababaacacbbcacabbcccbbbcbbacaaccbbcacbaccaacabcbabcccaccacabcbcccbbbcccccbcababbabaabcbbbababbacccbcaccbbaabcaacabbaabcccbcbbacbcabcbbcabcccaccabacabcaaacbabcbbcabababccbbabcabbbcbbcacacccbccaacaababccacbbcaaabaccccaccaacaccccbcccaaccaabbcccacccabccacaabcacaaabbccaacbacabbcbabccbcaaacaabccacbccbcbcaaccbccbbbbcccccbabacbccccbbbbbbacacacbbbacbaaccbaaabccacbbaaacccaabaabbccaaaabcabacbaaaccbbaacbcccabaccbcbcccaaacccabccbccaababcbaccabacacbaccbabcabcaabcccbcbacaacbbcbbcbabaaabbbbbbabacacbbccabbcabababccccbbabcccaccaacbbcccbbaababcaacaaaaacbbcccbbabacacaacbcbaabcccababbcabababbabbcbbacaabbbbcaabaacbabcacabcbacbacbcccabacccccbbbacbcabbaabcabbcccaabcaaccabaacacacababcaabcabbbbbaaaaaacccbbccaaabbaaaabccbccabbccbaabbaaabbaacbcacbcabbcabcccacabacababbabcbcaaabccbbaacacabcbacacabcaccccbacccabacbcbcbacabbbbaaabcacccccbcacabbcaabcbcabcaccbbccccbcabcbabcacccccbaaacbcbabccaccbacbcbccbcaccaaaaccabcabababaabcccacabbabccbbbcccbbababcabbacbccbbcacaabababcbbbbabbbcaacbbacbcabbaaaccaaccbccacabacabbbcaaaabbbcbbcbbbcbacaccaccbcabaabaabaabcccbbabcccbaacbccbcbbaaacbbbabbcbcccacacbbbacabacbccbabbaabcacabccaacaccabaacabbcbaaaabcbbbbabcacaaccccbaaccbbbabbbcacabaccbcabbabaacaaababaacccbbcccbabbbaccabcbcacaaababccabaacababbbaacaaababaaabbcaacbacccbcccbbbbcaaababcbcbbacccaaacabcbbaccbacbcacccbacbcacbccaaababbaccbabcbabcccaacacbabbaaccbacaaacbcabbcbababccccbcbcacacaabcacbbaabbccbcbcccabbcbcbbcaaccbcccababbabacaaaccbcabccacccaaaaabcaccbcbccaaaacbcbcbcaccaaaccacccccacbbccabbcabcabacbbabbabbaacababcbacbbbcccccabcccbccabcbbbccaacbccacbcacbcabbcbccaaabbbbccbbabbcaaaccbacabccbababaacabacaacbbacaacabbcabaabaccababaacabbabababcababbbbbaaaabaaccbabacacaaccbbaccbcbcaaaaabcbbbcabcbabbcaccbbbbacccaacbbcbacbaccccbbccaccccaaabaabcbcabaaacbcccaaabbacbabaabaaacbbcaabaacaacbabbcbbbbbbbaabaacbbbaccaaacccaccaccaaabbcbaacbabaacbbbbbbcbacbaaabcbbccaabcbcababbbacbcaccbaabcbccccbaacbccacacbabaacccbbbbbabcabcbbbbcaacccbaccacbbaaabbcbbbacaabcbaaabacbaacbacacbabaaabaabbacbbccacccabcccaccbaccbaabacccbabcabcaccbccbcbaaccaabbacbacbaacabbcaaabcabcccbacbaacabccababbbbcaacccaacbaaacbaaaacbbcbabbcacbabacbaacccbcbaabcabaaccbacbbcbaaccaaaaaaabbaaabbcbcaccbbaaacccbbaccbcabbcabaacaaccbcccccaaacacaabaaacabcbcbbbcabcbccabccbbcccaccaacabaccbbabaacabbcbcbabbbcbbaabbaaabacabcaaaacacccaabbabaccaccbcbacbcbacacabcccbcacbbbcaabbbccccacbbabbabbabaccabcacabaaaccabbbabbcbcbccaaaabaccbaacccabbabbbcbccaaaabcccbabcaabbaacbbbccbbbbcbacabcccbacbcbaabcaabaaacaccacabaabacbbbbaabccbcaaabccccbacbaacaaabccccaccaacbbaabccacbcccabcbaabbbaaabacaaccbabaabccbbbcacbcbabbbbbbbbaccbccbbbcaccbcbcaacccabcabaabbacbbcbacababcbbcbcacacacbbacccbabbbbccbcaabccaccbbabacbabaacccccacbaacaabaccabacbccbbcccbacacaccbbaaacacbcbcbcabacbaccbccbacaaaacbbcbacacbbbbccbcabaaaccabcccccbabbaaccbacabbbcabbabacbcccccbaaacbcbcbbacabccaaabaabccbacccabcaaabbbccbabcbbbbacbbbabaacccbabbcccabacababcaaaaacbbcabbaacaacacbcccbbaccacbbabacbbccccabbbccbbbcbccaabbcabbcbcbbcbbbabbbbabccbaaaacaaaaccaaaaaaababbbccbbaaabbcabbbbacaababbacbbcbbabacacbbaaaacabcbbaabababbbacaacbacaabbabcbbccccbabcbbaaccccabcbccabbbcbbcaabbcbcbbabbaacabcaccacbbbaccccbacccbcaacaabaccaabababaabaacbcbcaccaccccaacbaabcacbbaababbabaabbaccaaacabcbccabbacaaabcbbbcbbaaaabcccacabcbbbcbcbcacaaabaccacababababaaaaabaacbbaacabacaaccabccbacbbcbccbaaabcccabbacabacacacbcabaabbcabcbcacacaacbabcaacaaaaccaacbaabbbbbbbcaabcbcccccabcbcacaaababaaccbbbbbaabaabcbccbabbaabacbabababbaaccbababbacbacabaacbcaaaccaaabbcbcaccccbcaacbcbabcbbccacbccaaabaaccaabbbbbbcccccabbcacbcbabbbcacccbaaabbcbacacbccbacbbbabcbbabcacaaabcaabcbbbaaabcacbbacbbaccbcacbccbabbccbaaabaccacabaacbcbaaaaccbcaabaccbccccabcaacabccaacacbcaaacabbcccbaaacbbccaabacbcbacccaabaabaaccbaaabbccbabcbaaccaacacabbcccbccccabaabcacbcccaabccaaccbcccaaacbbbabbbbcbbcaacccaccbcaaccbccbaacacacaaabbcababbbaccbacbbbcbabcaaacaabbbbbabaccbcaabaccacacababbbaacccabbbbabbaccaccbcbcaaacbbabbbaccbbbcacaaccbcabcaabbacbbcabababaacabcaabcbbabcaccbccbabcbcacbbbbcbcacbcacabaaabcaabababcabaaabacacbabcaacccbabbbaabacbbabcccacccabbabcabcaabbccbabbababbcaccbabcaacbbbaaacacccabcbcabcaaabacbcabcaccbbbccaccbcbabbacbaccbaaaaaaacbcbbaccbcaaabbaacaabacccbbcccaacaaaaaaaaaabacbcabababbbbbbacbbcccbacbbcaabbbbccbaaccbacababacacbcaabbabcccaaabbbbbccaabcbcccabbabcabacaccabbabcbcccbacaaccbbbcaaaabbaacabaccbcbccbccccabacccbcbbccccbaaacbaacacbcbcccaacabbbacbabbcaccabbaabcccaccaccacbcabacbcbabbcbbabbccbccabacbbbacccbbaaaabcccccbabcbcccbccbbbccccabaabcacaacaacaaabacbccababccacacabaabaaaccacccaababcacbcaaaccbacbaaaacccacabbacccaaabbbcacacccbacbcbabacbcabaacccbbccaabbbbcbcacaabcabbccabccacbabcaabbbcbabccaccaccaaabbaaaababccaaaabcacaccabccccbcbacabaabcbcbbcbabcacbcabaacaabbbbbccaabaccacbbbaccacaaaacbccbbccaaaabaaacccbcaabcaacbbccccccaacaccccacbccbcacaabccacacabcacaaaaabaacbbabbcbbcabbbacacbbcbcbcccccabbcbabbabcaaaacabccabbbcacbbacbcbbbaccabaaacabbcbbacabbcccbbbccbbcbcaabcabcccaabcbccaacbcbbcabcbabacabaacccaaccccbbacccabaabacbacbbbcccbabcaabcbccccabaccacbcbcaabbababaaacbbbccaabbbbabcabcabacabaabcbaacaccabcaccccccbcaaacaabbaaccabaacbabcccbcacccabcabbaaaabbcacbbabbcacbcbbcaacacbaaacbacaaccbcbbcacaaccbaacbccaacaacbbbcaabaaababcbcbbbbbaaaaacccccaacbbacbaabaccbccbaabcbbabcccaaaabcccbcccaccbaccccbcbbbaabaccbcaaacacbabbacbbbccabcabacbacaaabaaaacaccbabacacacbbbbccbccbcccbbcaaabcaccacaaabccbcacbaaabbcaacbbccbccabbabbacbbcbbaaaacabbabcbaaccbbacbbbcbcacaabcbcabccacbaacbcbabcaccacaaaccabbbcacccaccbcccbcaaaacabcbbccbcabcbcaccaabbaccbabcaabaabbcaaaaaccacbaacaaaccabaaccbcbaacbcacaccccabaabbacaacccccabccbcabbacbabbacbbcababbbbcbbcbbabbbccabacbbbccbabbabbaccabbaccbaaccbbababccbbcacbacabbccaaccbbccaababccbabccaabccccaacbcabacbacabcabbcbbcccbbabbcacbaccbcaccbccbcbabbacccbabaccbaaacabcacabbccaabccacbaaccbccaabcabcaacaaaabcbbaccacaaabacacabccbbccacaabcaacccaaaabbabbbbabbcabaaacbbcaaaccccabcbacaacbbbbcccccbacababbbaabcaaccabbbbcbacbaacbabbacbbbacbbbacabcacbcabbacaaaabaccbbbaaaabccaccccacbabcbccabccbcaacccbaabbbcaccbbcbabbbacbbacccbabbacbbcaacabaabcaabbbbcbabbccacacbbcaaccbcaccacbcccbbbbbabababcbcbcbaaacaaaaacacacbcbcbcabcabcabcbabbababaacaacabbaccaaccaacbabbccaaabaccccabcccaccbcbcbcccccbcaabbbabbccaaaccbcabcacacbbbbcbaccaaacabacccbccbaacbcbcaccbbccbaabccabcccabbaccacacbaabbcacaaabcaaaabcccbbcbcbaaabaacbbcabaaaaacaccbabcbaccabaacabacbcbcacccbbaccbbacbccabccbbbabbbbabacaccacccabaaabbcccaabccbcacbbabbccbcaccabacbacbaacabaccccaccbacbcacababbacbbbababbbaacaccacaabaaaabcacbabaabbbabccbaaaabaabccbaababaabcaabbbbabbabbcbcbbcbbacaabccbacbbcaccaabccabbbbccccbabbbabbbcabaaabbbaabbbabcaabbbabaabcbcaabaacaccaaacbcbabbbcaaabbababbacbacbcacccbcbccbcaabacacbababbbbbbcabaaaccbcbbbbaaccbccbaccbabcbcccbacabbbcaaacacccaaababcbcbaacaccccccabcaccababacaaabbccccbacccacbabbbaabccacccaacbbccccbcbaaacacabbcabccbaacbacccabaacbcbcacaccbbccbaacacabccacccbbbcacaabcbacacbccaacaabaccccabcbacaabcccaccacbcabaabbaccbccbccaacacaababbcbccabaaaaaacccabbbacbbcaabbbacbcabaaccbccaaacbaccccccbbbbabacbabcabccabaabcbabcaaaacbcbcbabacbaccacbcabccbacbbaabbbccacbbaabcbacabacabbcccabacbbcbccbccababcbbccaaaaaabcbbacababaabcbcaaccbabaabbcabbccccbabaabcabbaabaaabbcbcbccacbcbccabcccbcaaabacacbbaabcabacacccbbcacbccababcbcbcaaaacacccbbaccbbbbbcaccbbcbaaaabacaaacaccbacaaaabcbacbacaccabaabcbbaccaabcbccbbccbabcbaccbaaaacacabcaaabbacaabcbcbbbbccaccabcbbcbbbacabbbbaccbcccbcbbaabcbaaabccaaabcaaabbacaccbbaccabcabacbcbaabcccaccbcaccaacbacacacccbccaabbacccbcbacbbbbabcccbcbbbacbbcbbbacaaaacaacaaccccccbabcbacbabcaacacbabcbcbccaaccaccaaccabccabcbbbcbcbaacbbbcacaababcabaaacbcbaacaabaccaabcbbccbacacacacabaabaaccbbcaaccacabbacacacacbcacaabbbaaaaabaababcbbbcacacbcaabaabaccaccbcaababaaacabacbaaabbacbbaaabbcaccbbabcbaccabbbbbabcaacacaccbbbbbbccbaccbcabccbcbabbbbcbaccbcabcbcccaccbabcaaacccaccabacabaacacabbaacbcbbcbcbacccbababcccccacbbcaaabcaaaabacbacaabacccaccacbacccbabacaccbaccbbacbaaaaabcbbbabbccabbccacbbcbcabbaababbcacacababcbaabbcababacbabababacbcbbbbccccbcacabbbaaabbaabbcacbcbcbbacbabacacacbaacaabbbcabbccabbcbccaaabaaabaaccaaaabbabccccbbbbbbabbbcababcaaacccbbcccbbaaccacaaabaaccbcbbccabbcabcacaaaaaabbbcaabababbcacbcacabacbabcbbaabaaaccbbcabbcacbcacbaacbacbcaacbcbaabaaaccabbaabbaaacababacacabbcbbcabacbbabccccbcbcacaabcacbaccabbbccbbbcabccacabcbaabcbcbaccbccaccbabaccabbacaaabbabbbbbacaabbabcaccbabcacacccbccabacaaabcabbbccbccaacbaccccbaabaccccbcaacaccaabbbabaabcbaacaccccbacaaccbcacababbccaccbbbbccbcabaaabcbaacabbccbaaabcbacabbbacbcbcabbcbacaabcabababbbcaacababbcbcacbabcbaccbcbbccacccbbcaaaabbbabaabcccbaccacaaacccbcaaccbabbaaabbbbabaabbcbababcaaaaccabbcbaabbcabbbbaacccbabcbbcbbbbbcbaccccccccbacbbaccbcccbccbaabaaaabcabccabacabbbababbbccaabcaaacbbbccaccbacbccbaabbcaabbcbabcabacbcbcbcaaacabcacbbccaccaabbbbcbcaabbbbaabbbcacabbbbccbcbcbacaacccbbccbabaaccbcbbbabbbaccbbccccaacacaaabbbaccbcbaabbccbbacabbabbcccbbacacbaaabcbcbbabccabcabcbacabaacaaacccbabbccabbccbbbacbbccaaaaaccbcccbaaacbcbcbbabbbccbcccbccbbabbaacbbbacbaaccacaccbccbbcacaabcacaaaccbbbcaabccbabcbbbbaaabbbbcccbaaabccabaccaabaacbcccccbbcbccbaabbcbbbbaaaacbbacababcabcaababacaababacabcabcbacaacaccbcbaaabcbcacacacaaaacabacacbcabacbbcbcabcbaaaaacaaaabcbcbcacbacbabaaabbaacbcabcbaacccababcaacbbcabccaccaabacabaccacacbcbaabaccccccbccbcaabcbaabbbcaaacaaabcbcbcbbcacbaacaaaabaaabcaaabcbacbcabccccbccaacbabaabbcbccacbcbbabbbbcbacccacaccccbcacbbbbbbacacacbabacbbbcbacbcccaabccbcaccbcccbcbcbabbbaabacbaacbbbcbcaccbbcbabaccbabbccabccacbbcaaccccbbcabbaacbbabaaaabbcbcbbaacaacbbcccacbcabababcaabbabcaccacaaabacabccbccbbbcacccccbccbbaaabbbaaaaccacbaacccacabccacaabababccccacccabcbccccabaaaabacabbbcaaccacccbaabbbacaabbbccbcbbbbabcaabbacaacabacbbcabbabcaababaacacaacbbbcbababcbacbaababababcbcacaaabcbcbcaabbcbbaaaacbacabbbbacccabcbbcabacccbbacbabcbabbccaabbcacbbcbababaaacbbcbbbaabbbaabbcacabcbcbbcabcaacccbaacaacabacaabbaabcbaccbccacbbbabbbbccabaaaababcccabcabcbcbabbccacccbccaacbbcccccccccbccacaacbaaccababcbccbaabaabcbccacbbaaaacbcbccbcbaaabaabaccbcbcbababcbaaccabacaaacabcaaabcaaaaacbaabacaacabbabaccabbabccacbacbbbcccaccaabbaaacaaaacccbbacbccbbbbbcccbcaacacabbaacbaabcabbaccccbaacbbcbbbbabcbcbbbbbcabbacbccbbaabbaabbbcbaccbabbabaccaaabacaccaccccbaacbbabacbbaacaaccccbbccbcbabbaabbabbaccbccaccbabccbbbbccbccaabcacaacabbcbbccccbcacbabcccaababbcaacabccabaacccabcabbbbabcacabbaabbbbbbacbacbbcaaaacabbacbcabbcbaacaaaabcaacacbbccccaaacbaaacbcccbacbabcbccccacabaabcabbaaaacaacbacccbbabbbbcbacababbaccaaccbccaabccacacaccbaaabbcaaaabcbcbababcccbbbaacaacbcaaacabbaccbcbcaacbccbacaaaccacbbcababcbbbccbcaccccccbaccaccabcbbaaacaababbbbcabbbbcccbcaccbbaccabbababbaaacccccbcacaaababccaccbbbccacacabaccccaacbaccccbcbacbcccabcbbabbbcacccbccbcaababcbbccabcbabcbbacabbccbabbbccbacbcaccbcaaabcababbabcbccbcbacccabaababccccaccbccbaacccccbbbbbaacbbacbcaababbcacbcabbccccccbbaaccbbbbaccaccbbbcbcacaccabcbbbbbabaaaccbbcccababcaaacbacaaaccaabaacaccbacabcbabacbccccbbcbbabcbcacbbaaaaacacbbccacaaccbcbccbaaaaabbbbbcabccaabcbccbcbbcaacbbcabccbabaaccaacbcacbaacaccacbbcbcbcabaaabcaabbcbaaccaccccccaacbcaabbcaaabcbbbcaaacbbaacbbbccaababaaaccbbbbaccbccabababbcbcbbccabbccaaaaaabacccbcabcbacbbcabccccccaaaccabcccbbaaaccccaaaabbccbaaabbcacbccaaaabbccbbbbcabcabbbccccccbcabbabacbbcbaaabababcbaccccccabbbbcacbcbbaccbbabccaacabbccaaccaccacbabbacaccacbbcabcabbbbababbacabcbbbabbcaccbabbbaaccaaaaccbbbbaabcbcbbcaaabcccbcbcccbbccaacccbbaaabcbabbbcbbcccaaacaaaaacbaacbcbaababbcccaabbabcabbccabaabbcaacaaacbcccbcbccaabaccbaaaaabcaccbaaccbaacacbccaaaaaccccaccbcbabcbbaaaabcabcacaaccbcaccabaacbbabbaacbcbabaccaabccbcababcaacbbccbbacbabacabbcbaabbbbbccbcccbbabbabacbccccbbaabbaccbcccbbaacaabaacbcbabcaabcacabbbbbbbcbbccabcbbbcbccccbbbbbaabccacbaacacccbcabbbcbbbbcbacbcaccabcbcbbccabbbaaaacbbaaaabbccbaacacaccabccbcbaaccbbccbaaacabbcacacbcaaaabbccbabccbaaaccbccabaacbcccabbbbaaababbbbbbbbababcbbabbabbacbccbccacbbaabbabcccabbbcacaccacbcbabcbcbcbbbbbacabbbcacbaacaabccabcccbbaaabaaabacbccacbbaaacbabcabcabbcaaacbbbaaacacbbbcaabcabcbbabcbcbcaacbabccabaaacbccaccccabbacacbbababcbacccbcaacabbbcabaabbbbbabbcccbababccbbaacbabaccbbcaacccaccaccbcbbcabccbbbaabaaccbbaaabaaabaccbccbaccbcaccaaaabcbacbbabbcccaabccbbcbabccaccacaaabcbabcbaabcbcabaaacbccaabbaacaaccbaccaabcbcbaabcbbcbbccbccbbbbaccaccbacbcbaaccabcbabbbccbbcaaabbbbbbbaaabbcbaaacbaabaaaaccbcbabaabbbbabaababacaabcaabababcbabcccaaababbcbaabbabcccaaabcbbaabbbcacaabcabbcbbbbaabcabbbbbabacbbabacacabcabccbbcacbbaacbabbabbbabcbcbcbcbacacabbbcbcabbabbaacaaaabaaccaabcbbbaaaaacacbbccbaabaabcbbacabbbabbcacbabbbbbabaccbabbcbaaaaacbabbbacbbccbabbaaabbccbabcbaccacaaabcbcccbbbbbaacacaaabaacacbaababbacccbabbcabcabcabcbbcabbaaaacbbaabbbcbbaacbaccabaaacccccccacabbbbccabbcbaabaccababccccaccaaaacbccbcbbbbcbccaabbaccccbacbabccbbababbbbcbcbcbbcbcabbbccaaccbbbccbcccccccbcbabbcaaccbbccacccbcaaaccabacbccbcbaaaabccacaabbbbbbacaacccbacbaabbaaaaccbbaabaabccbbbaaaacaabaababaacacbcaacbacabacacbccbcaacacaabaccabbcaacabbacbbabaabbccbbbabccbcccabcaaccbabccccbcbaabcacccbcbbcbaccbcbcbcccbbcbcbbbcaccaaabaacccbccbaabcbbcbacaacbacaaabccacabcaccbcbaabcbaccbaccbaaacbabbabccaccbcbcacbababbcabbcaabbbcbcbacacaabcccabbcaaacbcbacaaacbacaacbcababcccbabaacbaabcacaaabcbaacbabcbcaaaaaabbccacaaabacbaccbcbabbbbcbabbbccaaccbacbbabcbbbaccaaaacbbcacacaccabbaaccacabbaabbcaabccaaaaabcacacbaacbbacaacabacabcacacaabcbcbccbaabbccaaabbcababcbabcbbccabbabcaacaaaabccbbabaaaaccbbacacbbccabbcbccabaaccababbcabcbcaacbbcbcbacbabaaacabbcbbbbcbaabccbaaaabbaabcbacaaaacabaacaaacaacbcbcaabacbabcaccbacbbcabcaababcbbcbacbcbacbaccbbaaabcbbabbaaccbbbcbacbbccbacabaccacacacacaaccccbacbcaccaabcbbcababcacaabbcccaacbcaabcccacbaaccccbccccbbcbccabccabcccacaaacaccaccbabccbacabcbabcaccccbbccbcabaabbbccabbaabccaacbcabbcaacabcbaaaacacaccbcbcbaccccbccbcbababcbcacbcbbbbaccccbaabbabacbbcbbcbcaaacbccaaabbacacbcabcbcbacbbaaaaabcccaacbaacacabbabcacbcbccacacccabaccbcbccbaccbbbbbcbcbcbbbabbbbbcbabbaacbacbbcbcaabbbcaacbbabbbbaabbacbaabbcaabccacacbaaacaccbabcaccbbcbbcabbbabacbaabbcbbbacaaacbabcabbaaabbbccbaacabbabacaabbabaacbacccaaccccbbbbaccacacabccaaccbcacabcbbacccccaacabaaaccbcaaaccbcacbcabbcabcaaaabbcabbcbaccbbaccaaacbaaabbccbccbacbaaabccabccaccacbaaabacccbabbbcbcacaccbbccaacbababcaacabbabcbaabbcabaaabbbbabcacbcaaabbbcbaaabaccabbbacacabbbababcbccbacaabaaababbbaccaacabaaccccaaccbccacbbcaaabbcbaabcccaabcabbaccccccbbabcacbbbbbabbcacbcccbcacccaabbcabbbacabbaaabbacbacaaabbabcacabbcbaccabbabbaccacabbbacbcaaabbcabcabcccaaccbacbbccaabbcbccbaccccbbbbbaabcacacacccccbbacabaacacccbabcbbcaccababcbbbacabacbbbacaacbcacbbacabaccaacbbccabacacaaacaaababbbbacacbacbbcccbbbcbccaacccaacbaacacaccbaccbcbaabbcababcbbabcaccbcccaccbaacaabccbcabbcbcbbabaabaacababababcbccacaaabbcbbcccacabaacbbbbcbbabaaabbaababaabacbabcaacbbcbabbcbbbabccbcbbbabbccaacaccccabbcbbbbcccccccabcaacaabcbcabacbacabbccbbbcbabbbabcacbaaaacaaaaabcbabcaabacbbbbabcbcacccabbabcabccbbacaababaaaacacaacbabaaacccaabaabcacabacbacababbaaccbabaabcbcaabbcccaaaaaabcabcbaabcaabaaaacccacaccbaacabacbbaaacaaabcbcccbcbaaccabbaabbbcaaacaabaaccabcbcccaacaccccbcbaaacccbbccbccbbcbcacbbbabbacbabcccbbabcbacaccbccabccaccaaacabccccbbcaccbacaaacabbcababababbcbcccbacccaccbccacccacaabbcbaacbbacccbcbbaacacabbbccabcbbabbccaabccabccaacacbabbabbaababaacccbcbabacacccbcbacaabbcaacabbccbcaccacabacbbccbabacbccbbbcaacccabbbbcbaaabacaaacaabbbacaccaabbbbaacaaaabbbababacaaabbbbcacacbbcacbcababaabaccbaabcacbcccbbcaacbacacabbbcbbbbbabbccccbbbccabaacbacbaaaacaacbccbcaaccabaaaacccababaccbbbbccbabacbcacbbaaabbabbcbabacbcacbbabaababbbababaaacbaabccacbbabbbcbbbcccccccbbbbababcababbbaacacabbaccaabcaccacbcbbacbaaabaabcaabcbacabbacbccbabbbcbccccabcbbcbbacbccabbabcaccbacbcabbabbaabcbabcacccbbaaaabbcaccacbaabacbabbcaabbcacbcccabcbbabcbaacacbcacabbccccccaababbacbabbaaabcccbbcbbcbcbcaccaaabcacabbbbbccbabbacbccccacabbcbcaaccacbbabaaaabcbbabbbcababaabcacaaaccbacbbbaacaacabacbabacbcaccbcbbcabbcbccbbacbaaaabbcaaccbabcbbccbcbbbbbaccaabcabcacaacbbabcabacbacbbaaaaacccaaccbcaacabbabbbbbcbbabccaaaacbbcbccbbaacccccbacacacbbaacababcaabcacbabbacabbcaacaaaabbcccaaaabcabcbccacbcbaccbbaacccababbaaccbcaaabbabccabaaabbacabaccabbcbabaaacacbcccbbcbaabccaacbacaacbabccacbaacabbbacbaaccbacabaababbbcaaacccbbacacbababbcaabacccbcbcababbbbbcbbcbbabbcbbaaacbcbaaccbacccbaacccaccbcaaccbacaaaccbcaacacbaaabbcacaabbbacbaabaacacbbcacbababcaaaaabbcbbaacaccaababbacacbaaacbabacbaccccaaccacaaccaccacacaaccacaccccbcaabbaabcbbaccbcaaccbaababccbbaaabcbbbbaabbcaacbccbbcaccaacbcbacccbacaacbccabbcabcacbaabbaaabcbcbabaccbcaccabbcacbaababccacacbaabacbcaabbabbbacaaaabbabcabbcacbbbaccbacbcbcbbbabbcbcabccbacababbcababbbbbbbbbabbcbccacabbcbbabcabbbaababaabbabcaacabacbabbbabbcababacbbababcbbcccaabbbcaccabcacbabcaaccabccbcbccccacbbcaaabcacaaccbacbbccababcbbabbacacbabbcbbacabababababccacccababbcccbbcbcccbcaacbacabaccabccabacaacabcbaabbbbabcccaaacaacccbaabaaacacccbbaccbaccaaabcabbaccabbaacbababcacbbbbcccccbaaabbcbbbcbacababacaccacabbcaaacacababbcaaacccbbbabbacacbccaaaaacabbbabbbcbabaaaaaccbacbaacccbbaabbcccbabaaabbccaaccacbcbbabcbaaacbccacacbbccabaabaaaabacbaabaabbbbaccbcaacbaaabbbbbcbaacbababbcacaaabaccbcaaacbccacaacccacbbcabbabbacbbaabcaacbabacbaabccbabbaabababcabbbaaccaacbcaccbbbcbbaacccacbccaabccacbcbacacabcaabbcbcbcbbbcabcabbbbbbccccbbcabccaacacbbccbbbaacccbcabcacbaccabbbacabbaabcaaaaccbabababbbcaacbbbabacccacbcccbcbbaaacbcaaaccbacbccbccbcbbabababaabbababaabbbabccacccabbbaabcaaaacaccbabcbbcbacbcbbaccacabbcbacbcbcbaccbcbacacccbcbcabcabcaccaacbbcbcbbbabbbcabcbbaacacbccbcabcaccaccaaccccbacacbcacaaacbaccbaabcbbcbcbacbacacaaababbacbcabcabcacababcbccbcbacbcbacabaabcacacaaaacacababbbababcbcaccabbabaaaabccacaabbccccccacccccacaabbbabbbcbbccbbbabbaaccaabbcccaabbbbbbbabcaabbbbabbbcbbccabaacabcbcacccabccbbcbbcccaabbabacccccaacbccaabababbbbccaaababacaaacbabcaabbacbcbbaacabcbbaacacbbacbaaaacbaacabcbabaacabccbccbcbccbcbbbaacacacaabbabaacacaacbcaacacbaaaabaaaabcaccabbbbcaacaaaacbcaccabaccbccbccacbcbcaaabbacacbbacbcabcabcacbbaabaccbbcaaabcbbacbacaacacbabbacabcccbcbcbcacbaacbbbacbcbaabaaccacbbabaccacaaccabaabbccbcccabcbaabaaabaaabbaacbacacbabbbabbaaabbcbcaabaabcaabaccbbcbabcbcbbcccaabcabacaaacccaabcbcacbccacbbacccbbaacabaacbcbbaaaccbcccacabcaaaabaccbccbcbcabaacbbcabaaabcbcbacbcbacbccabaaabccbbbaabbbcaabbcbbcbacaabcaabbaaabcacccabcbccccbbccaacccccccacbabcbacbabcccabbaaccbabbabbacabbbbbcbabbaacaacaccbabcbabaaaccbaccaabbacbbcbaabbababbccbccbbacbabbcbbabbcabcbccaacccbacbbacaabacbcbbbaccaaccbacabbccacacbbcaccbbabbcbbbcaabaacacbabccaacaabaababbcbccacbbacbbaabbcbbabbcbabbacaaaccccaabaabbbbbcbbcbaaacacaabbacbabbbbaaaabbabcbabaacbacaaccaaaabacbcaabbbbbbcccbccaaccabacabbbaccbcbcabbcaaaacbbacacbabbabbabcbcaacacccacacbcaababbccabcbbacacbccbacbccaaaaccacaccaabaabababcbbcaacacbaabaaacbaaaabaaaaacbabcaaccccaccbcccababcabccacacbbabcbabaabaccacabbcbbabcbbcbbcccaacccaabcaaaaaabbbcabbacabbcbccacababbaaabbcbaccaaabbbcabcabcaabaababcbccbbacccbaabcccbcbabaccbccbcbabbcabbbaaabaccaccbaaaccbcccacbccbbaaaacbabcabbbcccabccbacaccbaacacaaabbbcacabcaaacabcacabcaccbcabcaccbccbbbbaaabbcaccacaacacbababbcbcbacbbbbccbacaccbaccbacaacbcbcbacbccbcababbccbcbccbacbccbbccbccabbcaabcaabbabccbaaabccaabccbbbbcbacccaccabbaabababcacbacccabacbbaaccbabaabbacabcaaacabbacaabcccaabbbbcbabbccacacaaabababcabbaabbbcbcbcbcacbbbcacaabaabbccaaaaabaacbacaababbcbbbaaabbccbcaabcbccaaabaaaacbbababaacbbcbabaaaaccbbcaabbaacabaacabaacbacbaacbcacaaccbcaccaaaaacaaacbcbbacbabacababcbcaabcaacabbabbbbaaaaacabacaccacacbaccabbcaacbbbcaabccabacccbbababbcbcabaaabbbaabacaccaaccabcaacbaaacbcaaccbcabbcccbcccacbcbbaccacacbcabcbcccaccbcccbbbaabcbacbabcaabcccbbbcabbbcbacaaaacbcbabacacacccaaaccbcacabaacbcccbbbbacacbbaccccbcbbacbabacabcbbbcbcabacbabaccaacabcabacbbbccbbbaccbcbccbabbacbcbccacbaaccaabcccaaacbabcbccabbbacbcbaababbbabbbbcbcacbacbababbaccabbaaabbcacccbabbaccaababbaacaacbcbabaacacbbaaacbbcabaababcabcaaaabbcbcbcbccaacaacbbcbaaababbbbacbabbabcbcaaacaacabacbbbaaaabaccbccbabbbaaaccabacbcacccacabcaabaccbababccacccababccbccccabaaaaccbcbbbccccaabccbaabaaabcccaaccababbbcbbabaaabcabcbcaaacaccccacaaacabbbaaaccbbbbbbcbccccbbbbacbabccaabbabcacbacacbcacbbbcbcaabbbcbbbbcbacaaabbcaaabaabccccabcacaacaacaabcabbaacbccabcbaaaabcbbcabbcbcbcccbccbbcabcacbaaabababcbaaaaaccbbcbbcbccbbaaccbacabbbcbcabcbaaabcaacbbbcaaaabcaccacbaccbbabaacabccaaabbacccbbbaaabacbbbcaccbaacbbacabaababbaccacbaaabbaabcbabbcbbaabbcacabccccaacccccbbbbccbacbbbbabbcbbbababbbccacaacacbcbaabaababaacbbbcbcaaacccccacbccacabcaaabbaabaaaabcaaaaaaaaccacacaaababcabbcabccabcbbcacabbaccabbbcacccaccabbbcbccbaccccbccbacbbbcaaacccbcbcbbbcaabaabaabcaabcbbbcacbbbccbabacccaabbcacccaacabcbcaacacbbacccababacaaaaccccccccacbaccbccccbacaccbacccabaabacacbacbccaaacacaccaaccacbbbbccacaabaaabacaacbabcacccacbabbbcbbbbabbaacbccabaaabccaaaabccbcbbbbaaacbabcbbacababbaccbaaacbbabbaccbccccccbaacbabbbaabaaacbabbaabaacabbbbaaabaabababbaaabacbacaaabcacabaaaabbacbaaabcaabacaaacbccaabacccacabcbccaaaccacbaabaaacccaabcbcccccbacccbbaaabcbcacbbcabbbbaaccbacacbcabaccaaaaaacbacabccccbbbcaacacacaaabbbacbccababbaccbbbcccbccaccabacabcaccbcccbaaacaccccbababcccbbccabbcbbacccabcabacacbccaccccbcaacbbababcabbcbaacaccaacabbbaabbbacabcaabcabbaaccbccabaccabcbcccbaababaaaaaacacaabbcabcbbbacabacccabcaacaccacccbcacaabaaccbabcccccaabbcaccacacbcbcabccabbbccabbccaacaacccbccaabcccaabaaccacbbccbabaabaababcccbcbcabbababccbbbccaacbaccacbbaabacbacbccabbccbaaccbbaabbbbcacabccbcbbbcccccacbabacaabacbbcbbcaacbbbbbcacccbcccaccaacbbabacabbbcaccccabccaaacccbbacccbbccbacacabacabcabbccabaaacaaccbccccabbabccabbacaaccccbbccaccccacaaacaccbccccaacbabcaabbbcaabcbccabcccacaacabcaaacccccbaccbbababbcababcbbcccaaaabccbcccaacacaacbbcbbbacbabbccccbaabcacbaabacacbbcababccabcbcaacaccccabaaabbaaaabacbabacbbbbcbaccccaabbbcaaccbbccbcccaaabbcabcaacbccbaacaccacbaaaaaaaaaccbacacbaabbbbaccccbaaccaaaaaacaccbabaacacbbcbaacccbcccbabbbbaaccbccaaccbcabcaccccaaacaaccacbccabbaabbbbccbcccabaacbaccabababaaacaccbbcbcbbccccccabcabababcbbccbaccacaacabbcccbabaabaaabaaccabccccbcccaacbacaacbabcccbaababacbccbccbacabcbcccccbbaaaaaabbbbbaacbbccbccaacaacabcacccacbccbbcbaccaacccaacccccabcbbcacbccabcbbcbcbacccbcabaabbabccbbcbcccabcabcbbaaabbaacabccbcaaabbcaacccbcbacaaaacaabcccbccacbbbcbccabbaaccccbabcbbbaaccabaacbbacccbaccabccbaccbccacaaccaaabcbbccccbacacabaccaacaabcacccaccacabbcccaacbcccbbbaccbbccacaacabcccccbaabbbcabaabbbacaccbbccaabaaabbaabcabbbbcbccaabcacccabbcbbbabbcaaacbcacbaccbcbcabcacccababcbbbbcaaabaabaccababacacbaaaccaabccabbcbababacabcabbbbabacaacaaacaaacccaabacbcacbacbccbcacbbccbcbabbbcabccabcbababbbabacbacaacacbaaacacababacbcbcccbbbcabacccbababbbbaccacaccbccbabbcabcaccccccaabcbbaabaacacabbbcbabcababcaacbcbbbabbbcbbbbcbcbccabacacaabcbbcabcacabaacaaabbbaabacbbccabbaacbcaacbaabcaacbbcbbcaaaaaacbccacacccacacbcbaacbabbccbbabbacbaabbaacacccabcccaacabacbbccaabccababcaacacbccabbbbacaabbccabbcccccaaaabcacaaacccbbcaacacabacbbaabccacaaabaaaaabaccbacbbabaaacbaacccbccccbcbbabbacbbbcccccacababbabbabbbbacbccccacbcccbbccaabbbcaaabaccacccaabcccbacbabcbbbabaacccacbbbbbabaabccbaaacbccabacacbabaacbccabbbcacccabbabbccbaabbababbaacacbabaabacbcbbbaaabaababcbcbbcabacbbcaacccbaabcbcbacbbbcccabcacacbcabbcbabbabbcabbbcbbcabacaccaabbacaaaccacbbabccbcaabbabcccbacbcabaaacababaabaabccacbccabbcbbbcccccbbacbc"))
print(Solution().longestPrefix("level"))
print(Solution().longestPrefix("ababab"))
print(Solution().longestPrefix("leetcodeleet"))
print(Solution().longestPrefix('a'))
print(Solution().hasValidPath([[1,1,1,1,1,1,3]])) # True
print(Solution().hasValidPath([[2],[2],[2],[2],[2],[2],[6]])) # True

print(Solution().hasValidPath([[2,4,3],[6,5,2]])) # True
print(Solution().hasValidPath([[1,2,1],[1,2,1]])) # False
print(Solution().hasValidPath([[1,1,2]])) # False
'''
