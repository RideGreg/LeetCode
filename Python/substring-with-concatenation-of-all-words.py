# Time:  O(m * k), where m is string length, n is dictionary size, k is word length
# Space: O(n)

# 30
# You are given a string, s, and a list of words, words,
# that are all of the same length. Find all starting indices of substring(s)
# in s that is a concatenation of each word in words exactly once and
# without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).


import collections

# Sliding window solution:
# since the length of all words is same and fixed, treat each word as a UNIT
# we can convert the problem like: s = 'acxbccacy', find substrings containing ['a', 'b', 'c', 'c']
# obvious we can use sliding window to solve it in O(len(s)).
# Now each UNIT is a word, we should try starting from each char in a word in O(len(word[0])).
class Solution(object):
    def findSubstring(self, s, words): # USE THIS: much better time complexity
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans, cnt, wlen = [], len(words), len(words[0])
        if len(s) < cnt * wlen:
            return ans

        expect = collections.Counter(words)
        for i in range(wlen):               # Time: O(k), test i in 0,1,2,..k-1 where k is word length
                                            # for each i, do sliding window with word treating as a UNIT
            start, curCnt = i, 0
            actual = collections.defaultdict(int)
            for cur in range(i, len(s)-wlen+1, wlen): # Time:  O(m / k)
                sub = s[cur : cur+wlen]               # Time:  O(k)
                if sub not in expect:
                    start, curCnt = cur + wlen, 0
                    actual = collections.defaultdict(int)
                else:
                    actual[sub] += 1
                    curCnt += 1
                    while actual[sub] > expect[sub]:
                        actual[s[start : start+wlen]] -= 1
                        curCnt -= 1
                        start += wlen
                    if curCnt == cnt:
                        ans.append(start)
        return ans


# Time:  O(m * n * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)
class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        cnt, wlen = len(words), len(words[0])
        expect = collections.Counter(words)
        for start in range(len(s) - cnt * wlen + 1):       # O(m)
            actual = collections.defaultdict(int)
            for i in range(cnt):                           # O(n)
                sub = s[start+i*wlen : start+(i+1)*wlen]   # O(k)
                if sub not in expect or actual[sub] + 1 > expect[sub]:
                    break
                actual[sub] += 1
            else:    # finish iteration of cnt, no break
                ans.append(start)
        return ans


    # similar to the above, just not that Pythonic
    def findSubstring2(self, s, words):
        ans, m, n, k = [], len(s), len(words), len(words[0])
        if m < n*k:
            return ans

        expect = collections.defaultdict(int)
        for i in words:
            expect[i] += 1                            # Space: O(n * k)

        for i in xrange(m+1-k*n):                     # Time: O(m)
            actual, j = collections.defaultdict(int), 0
            while j < n:                              # Time: O(n)
                word = s[i+j*k : i+j*k+k]             # Time: O(k)
                if word not in expect or actual[word] + 1 > expect[word]:
                    break
                actual[word] += 1
                j += 1
            if j == n:
                ans.append(i)

        return ans

if __name__ == "__main__":
    print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])) # [0, 9]
