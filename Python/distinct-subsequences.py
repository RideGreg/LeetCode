# Time:  O(n^2)
# Space: O(n)
#
# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.
#

class Solution:
    # @return an integer
    def numDistinct(self, S, T):    # USE THIS: space optimization
        ways = [0 for _ in xrange(len(T) + 1)]
        ways[0] = 1
        for S_char in S:
            for j in reversed(xrange(len(T))):
                if S_char == T[j]:
                    ways[j + 1] += ways[j]
        return ways[-1]

    '''
    dp[i][j] is how many distinct subseq of S[:i] equals to T[:j]
  |-|a|b|b|c   (S)
- |1|1|1|1|1
a |0|1|1|1|1
b |0|0|1|2|2
c |0|0|0|0|2
(T)
    '''
    def numDistinct_2D(self, S, T):
        ls, lt = len(S), len(T)
        dp = [[0]*(ls+1) for _ in xrange(lt+1)]
        dp[0] = [1]*(ls+1)
        for j in xrange(ls):
            for i in reversed(xrange(lt)):
                if S[j] == T[i]:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]  #the new char in S is useless, same # of subseq
        return dp[lt][ls]




# TLE: brute force, get all subsequences with length of len(t)
class Solution_brute(object):
    def numDistinct(self, s, t):
        def combine(n, k):
            def dfs(start, cur, k, n):
                if len(cur) == k:
                    ans.append(cur)
                    return
                for i in xrange(start, n + 1 - (k - len(cur)) + 1):
                    dfs(i + 1, cur + [i], k, n)

            ans = []
            dfs(1, [], k, n)
            return ans

        ret = 0
        allCombine = combine(len(s), len(t))
        for c in allCombine:
            ss = ''.join([s[i - 1] for i in c])
            if ss == t: ret += 1
        return ret

if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    result = Solution().numDistinct(S, T)
    print result

