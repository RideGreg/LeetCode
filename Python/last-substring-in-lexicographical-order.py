# Time:  O(n)
# Space: O(n)

# 1163 weekly contest 150 8/17/2019
# Given a string s, return the last substring of s in lexicographical order.

import collections


class Solution(object):
    # USE THIS: ming. Find the largest char, if the count is 1, return; if count is more than 1, find largest char in next positions
    # maintain/inherit the starting pos of each new position. Trick: stop when all char visited to avoid repeating calc on same substring (TLE).
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        maxc = max(s)
        pos = [i for i, x in enumerate(s) if x == maxc]
        if len(pos) == 1:
            return s[pos[0]:]

        visited = len(pos)
        start = {p:p for p in pos}
        while True:
            maxc = max(s[i+1] for i in pos if i < len(s)-1)
            pos = [i+1 for i in pos if i < n-1 and s[i+1] == maxc]
            visited += len(pos)
            if len(pos) == 1 or visited >= n:
                p = start[pos[0]-1]
                return s[p:]
            start = {p: start[p-1] for p in pos} # inherit the starting pos

    def lastSubstring_kamyu(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)

        max_c = max(count.keys())
        starts = {}
        for i in count[max_c]:
            starts[i] = i+1
        while len(starts)-1 > 0:
            lookup = set()       # use this to filter repeats
            next_count = collections.defaultdict(list)
            for start, end in starts.items():
                if end == len(s):  # finished
                    lookup.add(start)
                    continue
                next_count[s[end]].append(start)				
                if end in starts:  # overlapped
                    lookup.add(end)			
            next_starts = {}
            max_c = max(next_count.keys())
            for start in next_count[max_c]:
                if start not in lookup:
                    next_starts[start] = starts[start]+1
            starts = next_starts
        return s[next(iter(starts.keys())):]


    def lastSubstring_discuss1(self, s: str) -> str: # pretty but hard to understand
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:

            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + k + 1
            else:
                i = max(j, i + k + 1)
                j = i + 1
            k = 0
        return s[i:]

    def lastSubstring_discuss2(self, s: str) -> str:
        def getLargestChar(plist):
            dp = [[] for _ in range(26)]  # the locations for each char

            for c, i in plist:
                dp[ord(c) - ord('a')].append(i)
            for i in range(25, -1, -1):
                if len(dp[i]) >= 1:
                    return i, dp[i]

        ans = ''
        n = len(s)
        plist = [(c, i) for i, c in enumerate(s)]
        count = 0
        while len(plist) > 1 and count < n:
            c, largest = getLargestChar(plist)
            count += len(largest)
            plist = [(s[i + 1], i + 1) for i in largest if i + 1 < n]
            ans += (chr(c + ord('a')))
        if len(plist) >= 1:
            ans += s[plist[0][1]:]
        return ans

print(Solution().lastSubstring('za'*4)) # 'zazazaza'
print(Solution().lastSubstring('abab')) # 'bab'
print(Solution().lastSubstring('leetcode')) # 'tcode'
print(Solution().lastSubstring('azabcdzaazabzaz')) # 'zaz'
print(Solution().lastSubstring('ababz')) # 'z'


