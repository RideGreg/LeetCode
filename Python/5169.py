from typing import List

class Solution:

    def closetDivisors(self, num):
        import math
        def divor(n):
            r = int(math.sqrt(n))
            while n % r:
                r -= 1
            return [r, n//r]

        x1, y1 = divor(num+1)
        x2, y2 = divor(num+2)
        if abs(y1-x1) < abs(y2-x2):
            return [x1, y1]
        else:
            return [x2, y2]


    def largestMultipleOfThree(self, digits: List[int]) -> str:
        dp = [0, 0, 0]
        has = [[], [], []]
        for num in digits:
            temp = [num+x for x in dp]
            nhas = list(has)
            for i, x in enumerate(temp):
                if x > dp[x%3] or (x==dp[x%3] and len(has[i])+1>len(nhas[x%3])):
                    dp[x%3] = max(dp[x%3], x)
                    nhas[x%3] = has[i] + [num]
            has = nhas
        if dp[0] == 0:
            return '0' if 0 in has[0] else ''
        has[0].sort(reverse=1)
        return ''.join(map(str, has[0]))

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def leapYear(n):
            if n%400 == 0: return True
            if n%100 == 0: return False
            return n%4 == 0
        y1,m1,d1 = map(int, date1.split('-'))
        y2,m2,d2 = map(int, date2.split('-'))
        if y2<y1 or (y2==y1 and m2<m1) or (y2==y1 and m2==m1 and d2<d1):
            return self.daysBetweenDates(date2, date1)
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        days1 = sum(days[:m1-1])+d1
        if leapYear(y1) and m1>2: days1 += 1
        days2 = sum(days[:m2-1])+d2
        if leapYear(y2) and m2>2: days2 += 1
        ans = days2-days1
        ans += sum(366 if leapYear(x) else 365 for x in range(y1, y2))
        return ans

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        par = {}
        for i, c in enumerate(leftChild):
            if c==-1: continue
            if c in par: return False
            par[c] = i
        for i, c in enumerate(rightChild):
            if c==-1: continue
            if c in par: return False
            par[c] = i
        return len(par) == n-1

    def getPrefix(self, p):
        prefix = [-1] * len(p)
        j = -1
        for i in range(1, len(p)):
            while j > -1 and p[i] != p[j+1]:
                j = prefix[j]
            if p[i] == p[j+1]:
                j += 1
            prefix[i] = j
        return prefix



    # 1353
    # Greedy: traverse days from 1 to max(endTime). For each day, maintain the endTime of all events
    # starting before or on the day in a minHeap, pick the earliest endTime for this day.

    # USE THIS: save space, not storing start-end pairs; need sorting by startTime
    def maxEvents(self, events):
        events.sort(reverse=1)
        M = max(e for s, e in events)
        end = []
        ans = 0
        for d in xrange(1, M + 1):
            while events and events[-1][0] == d:
                _, e = events.pop()
                heapq.heappush(end, e)
            while end and end[0] < d:
                heapq.heappop(end)
            if end:
                heapq.heappop(end)
                ans += 1
        return ans

    def maxEvents_awice(self, events): # store start-end pairs, easy to understand
        M = max(e for s, e in events)
        A = [[] for _ in xrange(M + 1)]
        for s, e in events:
            A[s].append(e)

        end = []
        ans = 0
        for d in range(1, M + 1):
            for e in A[d]:
                heapq.heappush(end, e)
            while end and end[0] < d:
                heapq.heappop(end)
            if end:
                heapq.heappop(end)
                ans += 1
        return ans

        '''
        d = collections.defaultdict(list)
        used, ans = set(), 0
        for s,e in events:
            d[e-s].append([s,e])
        for i in sorted(d.keys()):
            ee = list(d[i])
            if not ee: continue
            ee.sort(key=lambda x:x[1])
            last = 0
            for s,e in ee:
                if last < e:
                    last = max(s, last + 1)
                    while last in used and last <= e:
                        last += 1
                    if last <= e:
                        ans += 1
                        used.add(last)
        return ans
        '''
print(Solution().getPrefix("AABAACAABAA")) # [-1,0,-1,0,1,-1,0,1,2,3,4]
print(Solution().constrainedSubsetSum( [10,-2,-10,-5,20], 2)) # 23

print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,4,2,7,5,3,8,6,9]
print(Solution().findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
# [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
print(Solution().findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
# [1,4,2,5,3,8,6,9,7,10,11]
print(Solution().findDiagonalOrder([[1,2,3,4,5,6]])) # [[1,2,3,4,5,6]]

'''
print(Solution().closetDivisors(8))
print(Solution().closetDivisors(123))
print(Solution().closetDivisors(999))

print(Solution().largestMultipleOfThree([8,1,9]))
print(Solution().largestMultipleOfThree([8,6,7,1,0]))
print(Solution().largestMultipleOfThree([1]))
print(Solution().largestMultipleOfThree([0,0,0,0,0]))

print(Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1]))
print(Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1]))
print(Solution().validateBinaryTreeNodes(2,  [1,0], [-1,-1]))
print(Solution().validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1]))

#print(Solution().daysBetweenDates("2019-06-29", "2019-06-30"))
#print(Solution().daysBetweenDates("2020-01-15", "2019-12-31"))

print(Solution().maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])) # 5
print(Solution().maxEvents([[1,3],[1,3],[1,3],[3,4]])) # 4
print(Solution().maxEvents([[1,2],[2,3],[3,4]])) # 3
print(Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]])) # 4
print(Solution().maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])) # 4
print(Solution().maxEvents([[1,1000]])) # 1
print(Solution().maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]])) # 7
'''