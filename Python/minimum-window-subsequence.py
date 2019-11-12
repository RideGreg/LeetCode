# Time:  O(s * t)
# Space: O(t)

# 727
# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such minimum-length windows, return the one with the left-most starting index.

# - All the strings in the input will only contain lowercase letters.
# - The length of S will be in the range [1, 20000].
# - The length of T will be in the range [1, 100].

class Solution(object):
    # DP: 数组dp[i]存储当T[0 .. i]在S中找到子序列匹配时，对应的最大起点下标(注意是不断update到最大起点不是最小起点，所以子序列最短)
    # 初始令dp[0 .. len(T) - 1] = -1
    def minWindow(self, S, T):
        ans = ''
        ls, lt = len(S), len(T)
        dp = [-1] * lt
        for x in range(ls): # traverse S, update dp for each substring S[:x]
            for y in range(lt - 1, -1, -1):
                if T[y] == S[x]:
                    # if y==0 (starting), then record the starting pos in S.
                    # else y!=0, inherit the starting pos from the previous char.
                    dp[y] = dp[y - 1] if y else x
                    if y == lt - 1 and dp[-1] > -1: # whole string matched and all previous chars have a match
                        nlen = x - dp[-1] + 1
                        if not ans or nlen < len(ans):
                            ans = S[dp[-1] : x+1]
        return ans

    def minWindow_kamyu(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        lookup = [[None for _ in xrange(26)] for _ in xrange(len(S)+1)]
        find_char_next_pos = [None]*26
        for i in reversed(xrange(len(S))):
            find_char_next_pos[ord(S[i])-ord('a')] = i+1
            lookup[i] = list(find_char_next_pos)

        min_i, min_len = None, float("inf")
        for i in xrange(len(S)):
            if S[i] != T[0]:
                continue
            start = i
            for c in T:
                start = lookup[start][ord(c)-ord('a')]
                if start == None:
                    break
            else:
                if start-i < min_len:
                    min_i, min_len = i, start-i
        return S[min_i:min_i+min_len] if min_i is not None else ""

    
# Time:  O(s * t)
# Space: O(s)
class Solution2(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dp = [[None for _ in xrange(len(S))] for _ in xrange(2)]
        for j, c in enumerate(S):
            if c == T[0]:
                dp[0][j] = j

        for i in xrange(1, len(T)):
            prev = None
            dp[i%2] = [None] * len(S)
            for j, c in enumerate(S):
                if prev is not None and c == T[i]:
                    dp[i%2][j] = prev
                if dp[(i-1)%2][j] is not None:
                    prev = dp[(i-1)%2][j]

        start, end = 0, len(S)
        for j, i in enumerate(dp[(len(T)-1)%2]):
            if i >= 0 and j-i < end-start:
                start, end = i, j
        return S[start:end+1] if end < len(S) else ""

print(Solution().minWindow("abcdebdde", "bde")) # "bcde"
print(Solution().minWindow("abcebdde", "bde")) # "bdde"
print(Solution().minWindow("acccedde", "ccd")) # "cced"
# dp = [-1,-1,-1]
#      [ 1,-1,-1]
#      [ 2, 1,-1]
#      [ 3, 2,-1]
#      [ 3, 2,-1]
#      [ 3, 2, 2]
#      [ 3, 2, 2]
#      [ 3, 2, 2]