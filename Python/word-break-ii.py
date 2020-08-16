# Time:  O(n * l^2 + n * r), l is the max length of the words,
#                            r is the number of the results.
# Space: O(n^2)
#
# Given a string s and a dictionary of words dict,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].
#

class Solution(object):
    def wordBreak_backtrack(self, s, wordDict): # USE THIS: may slower than wordBreak_memorization 
                                                # but easy to remember
        def dfs(start, cur):
            if start == len(s):
                ans.append(' '.join(cur))
                return
            for i in xrange(start + 1, len(s) + 1):
                if s[start:i] in dset:
                    cur.append(s[start:i])
                    dfs(i, cur)
                    cur.pop()

        # check doable O(n^2) to avoid TLE. See word-break.py
        if not wordDict: return []
        n, dset = len(s), set(wordDict)
        maxlen = max(len(w) for w in dset)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = any(dp[i] and s[i:j] in dset \
                        for i in xrange(max(0, j - maxlen), j))

        ans = []
        if dp[n]:
            dfs(0, [])
        return ans

    def wordBreak_memorization(self, s, wordDict):
        def dfs(s):
            ans = []
            if s in dset:
                ans.append(s)
            for i in xrange(1, len(s)):
                prefix, suffix = s[:i], s[i:]
                if prefix in dset:
                    rest = tokenDict.get(suffix)
                    if rest is None:
                        rest = dfs(suffix)
                    for x in rest:
                        ans.append("{} {}".format(prefix, x))
            tokenDict[s] = ans
            return ans

        # check doable O(n^2) to avoid TLE. See word-break.py
        if not wordDict: return []
        n, dset = len(s), set(wordDict)
        maxlen = max(len(w) for w in dset)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = any(dp[i] and s[i:j] in dset \
                        for i in xrange(max(0, j - maxlen), j))

        tokenDict = {}
        return dfs(s) if dp[n] else []


class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)

        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))

        can_break = [False for _ in xrange(n + 1)]
        valid = [[False] * n for _ in xrange(n)]
        can_break[0] = True
        for i in xrange(1, n + 1):
            for l in xrange(1, min(i, max_len) + 1):
                if can_break[i-l] and s[i-l:i] in wordDict:
                    valid[i-l][i-1] = True
                    can_break[i] = True

        result = []
        if can_break[-1]:
            self.wordBreakHelper(s, valid, 0, [], result)
        return result

    def wordBreakHelper(self, s, valid, start, path, result):
        if start == len(s):
            result.append(" ".join(path))
            return
        for i in xrange(start, len(s)):
            if valid[start][i]:
                path.append(s[start:i+1])
                self.wordBreakHelper(s, valid, i + 1, path, result)
                path.pop()


if __name__ == "__main__":
    print Solution2().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])

import timeit
#2.99112820625
print timeit.timeit('Solution().wordBreak_backtrack("aaaaaaaaaaaaaaaaaaaaa", \
                    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])', 'from __main__ import Solution', number=1)
#1.07430911064
print timeit.timeit('Solution().wordBreak_memorization("aaaaaaaaaaaaaaaaaaaaa", \
                    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])', 'from __main__ import Solution', number=1)
