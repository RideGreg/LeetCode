# Time:  O(n)
# Space: O(n)

# 1326 weekly contest 172 1/18/2020

# There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
#
# There are n + 1 taps located at points [0, 1, ..., n] in the garden.
#
# Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap
# can water the area [i - ranges[i], i + ranges[i]] if it was open.
#
# Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

class Solution(object):
    def minTaps(self, n, ranges):  # USE THIS: awice, interval, greedy
        A = [(i-r, i+r) for i, r in enumerate(ranges)]
        A.sort()
        ans, s, e, i = 0, 0, float('-inf'), 0
        while i < len(A):
            if A[i][0] > s: break
            while i < len(A) and A[i][0] <= s:
                e = max(e, A[i][1])
                i += 1
            ans += 1
            if e >= n: return ans
            s = e
        return -1

    def minTaps_kamyu(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        def jump_game(A):
            jump_count, reachable, curr_reachable = 0, 0, 0
            for i, length in enumerate(A):
                if i > reachable:
                    return -1
                if i > curr_reachable:
                    curr_reachable = reachable
                    jump_count += 1
                reachable = max(reachable, i+length)
            return jump_count
    
        max_range = [0]*(n+1)
        for i, r in enumerate(ranges):
            left, right = max(i-r, 0), min(i+r, n)
            max_range[left] = max(max_range[left], right-left)
        return jump_game(max_range)

    # TLE: binary search + combination
    def minTaps_TLE(self, n, ranges):
        import itertools
        coverBy = [[] for _ in range(n+1)]
        for i, r in enumerate(ranges):
            if r == 0: continue
            for k in range(max(0, i-r), min(i+r, n)+1):
                coverBy[k].append(i)
        if any(not v for v in coverBy): return -1
        onTap, covered = set(), set()
        for v in coverBy:
            if len(v) == 1:
                onTap.add(v[0])
                i, r = v[0], ranges[v[0]]
                for k in range(max(0, i - r), min(i + r, n) + 1):
                    covered.add(k)
        if len(covered) == n+1:
            return len(onTap)

        offTap = [x for x in range(n+1) if x not in onTap and ranges[x]]
        offTap.sort(key=lambda x:ranges[x], reverse=True)
        notCovered = [x for x in range(n+1) if x not in covered]

        def can_cover(m, on):
            return any(ranges[i] and i-ranges[i]+0.5<=m<=i+ranges[i]-0.5 for i in on)

        def ok(k):
            for on in itertools.combinations(offTap, k):
                onlist = list(on)
                if all(can_cover(x, on) for x in notCovered):
                    return True
            return False

        lo, hi = 1, len(offTap)
        while lo < hi:
            mi = (lo+hi)//2
            if ok(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo + len(onTap)

print(Solution().minTaps(68,
[0,0,0,1,4,2,2,2,2,4,0,0,0,5,4,0,0,5,3,0,1,1,5,1,1,2,4,1,0,4,3,5,1,0,3,3,4,2,2,4,3,1,1,0,4,0,2,1,4,0,0,3,3,1,1,4,4,2,0,3,4,0,1,5,3,0,1,0,2]))
# 9
print(Solution().minTaps(38,
[3,1,5,0,4,3,2,5,0,2,4,2,1,3,4,4,5,1,3,2,3,0,1,3,1,0,3,2,0,3,4,2,1,0,5,5,0,4,2])) #6
print(Solution().minTaps(35, [1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]))#6
print(Solution().minTaps(5, [3,4,1,1,0,0])) # 1
print(Solution().minTaps(3, [0,0,0,0])) # -1
print(Solution().minTaps(7, [1,2,1,0,2,1,0,1])) # 3
print(Solution().minTaps(8, [4,0,0,0,0,0,0,0,4])) # 2
print(Solution().minTaps(8, [4,0,0,0,4,0,0,0,4])) # 1
