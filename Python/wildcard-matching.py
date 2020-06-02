# Time:  O(m + n) on average, O(m * n) on worst
# Space: O(1)

# 44 通配符匹配
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false
#

# iterative solution with greedy
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        count = 0  # used for complexity check
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        while s_ptr < len(s):
            if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_ptr += 1
                last_s_ptr = s_ptr
                last_p_ptr = p_ptr
            elif last_p_ptr != -1:
                last_s_ptr += 1
                s_ptr = last_s_ptr
                p_ptr = last_p_ptr
            else:
                assert(count <= (len(p)+1) * (len(s)+1))
                return False
            count += 1  # used for complexity check
 
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            count += 1  # used for complexity check

        assert(count <= (len(p)+1) * (len(s)+1))
        return p_ptr == len(p)


# dp with rolling window
# Time:  O(m * n)
# Space: O(n)
class Solution2(object):  # USE THIS
    # @return a boolean
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(2)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            dp[i][0] = False
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[i % 2][j - 1]
                    # TLE dp[i][j] = dp[i][j-1] or reduce(operator.__or__, [dp[k][j] for k in range(i)])
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '?')
                ''' Below is a bug: due to reuse space, every cell has to be set, CANNOT be kept old value.
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                '''
        return dp[m % 2][-1]


# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution3:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        result[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in range(1,len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i][j] = result[i][j-1] or result[i-1][j]
                    # TLE result[i][j] = result[i][j-1] or reduce(operator.__or__, [result[k][j] for k in range(i)])

        return result[len(s)][len(p)]


# recursive, slowest, TLE
class Solution4:
    # @return a boolean
    def isMatch(self, s, p):
        if not p or not s:
            return not s and not p

        if p[0] != '*':
            if p[0] == s[0] or p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0:
                if self.isMatch(s, p[1:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[1:])

if __name__ == "__main__":
    print(Solution2().isMatch("abcdefde", "abc*def")) # False
    print(Solution2().isMatch("aaaabaaaab","a*b*b")) # True
    print(Solution2().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")) # False
    print(Solution2().isMatch("aa","a")) # False
    print(Solution2().isMatch("aa","aa")) # True
    print(Solution2().isMatch("aaa","aa")) # False
    print(Solution2().isMatch("aa", "a*")) # True
    print(Solution2().isMatch("aa", "?*")) # True
    print(Solution2().isMatch("ab", "?*")) # True
    print(Solution2().isMatch("aab", "c*a*b")) # False
