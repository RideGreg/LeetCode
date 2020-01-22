# Time:  O(n)
# Space: O(n)

# 1297 weekly contest 168 12/21/2019

# Given a string s, return the maximum number of ocurrences of any substring under the following rules:
#
# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.

# Constraints:
#
# 1 <= s.length <= 10^5
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)

import collections


# rolling hash (Rabin-Karp Algorithm)
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        M, p = 10**9+7, 113
        power, rolling_hash = pow(p, minSize-1, M), 0

        left = 0
        lookup, count = collections.defaultdict(int), collections.defaultdict(int)
        for right in xrange(len(s)):
            count[s[right]] += 1
            if right-left+1 > minSize:
                count[s[left]] -= 1
                rolling_hash = (rolling_hash - ord(s[left])*power) % M
                if count[s[left]] == 0:
                    count.pop(s[left])
                left += 1
            rolling_hash = (rolling_hash*p + ord(s[right])) % M
            if right-left+1 == minSize and len(count) <= maxLetters:
                lookup[rolling_hash] += 1
        return max(lookup.values() or [0])


# Time:  O(m * n), m = 26
# Space: O(m * n)
class Solution2(object):
    def maxFreq2(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        lookup = {}
        for right in xrange(minSize-1, len(s)):
            word = s[right-minSize+1:right+1]
            if word in lookup:
                lookup[word] += 1
            elif len(collections.Counter(word)) <= maxLetters:
                lookup[word] = 1
        return max(lookup.values() or [0])

    # O(n*size) where size = maxSize-minSize+1
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt=collections.defaultdict(int)
        n=len(s)
        st=0
        ed=st+minSize
        while st<n:
            letters=set(s[st:ed])
            while len(letters)<=maxLetters and ed-st<=maxSize and ed<=n:
                    cnt[s[st:ed]]+=1
                    ed+=1
                    if ed<n:
                        letters.add(s[ed])
            st+=1
            ed=st+minSize
        return max(cnt.values()) if cnt else 0

    def maxFreq_506140166(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt=collections.defaultdict(int)
        n=len(s)
        st=ed=0
        while st<n:
            letters=set()
            while len(letters)<=maxLetters and ed-st<=maxSize and ed<=n:
                    if ed-st>=minSize:
                        cnt[s[st:ed]]+=1
                    if ed<n:
                        letters.add(s[ed])
                    ed+=1
            st+=1
            ed=st
        return max(cnt.values()) if cnt else 0

    # TLE: O(n*size) where size = maxSize-minSize+1
    # TLE because no pruning, when letterCnts > maxLetters, we should stop. But the problem is we
    # cannot maintain the count of unique letters if exit the current iteration early.
    def maxFreq_ming(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        sizes = maxSize-minSize+1
        dp = [[0] * 26 for _ in range(sizes)] # letters for all valid sizes
        letterCnts = [0]*(sizes) # count of unique letters for all valid sizes
        subsCounter = collections.defaultdict(int)
        ans = 0
        for j, c in enumerate(s):
            for i in range(len(dp)):
                dp[i][ord(c)-ord('a')] += 1
                if dp[i][ord(c)-ord('a')] == 1:
                    letterCnts[i] += 1

                if sum(dp[i]) == minSize+i:
                    pos_to_discard = j+1-minSize-i
                    if letterCnts[i] <= maxLetters:
                        subs = s[pos_to_discard:j+1]
                        subsCounter[subs] += 1
                        ans = max(ans, subsCounter[subs])
                    dp[i][ord(s[pos_to_discard])-ord('a')] -= 1
                    if dp[i][ord(s[pos_to_discard])-ord('a')] == 0:
                        letterCnts[i] -= 1
        return ans

print(Solution().maxFreq("babcbceccaaacddbdaedbadcddcbdbcbaaddbcabcccbacebda",1,1,1)) # 13
print(Solution().maxFreq("aababcaab", 2,3,4)) # 2
print(Solution().maxFreq("aaaa", 1,3,3)) #2
print(Solution().maxFreq("aabcabcab",2,2,3)) # 3
print(Solution().maxFreq("abcde",2,3,3)) # 0

