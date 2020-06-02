# Time:  O(m * n)
# Space: O(n)

# 10 正则表达式匹配
# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
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
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true
#

# dp with rolling window
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def singleMatch(i, j):
            return (s[i] == p[j]) or (p[j] == '.')

        dp = [[False]*(len(p)+1) for _ in range(2)]

        # first padding row
        dp[0][0] = True # empty string vs empty pattern
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            dp[i%2][0] = False # non-empty string vs empty pattern
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    dp[i%2][j] = singleMatch(i-1, j-1) and dp[(i-1)%2][j-1]
                else:
                    #         * for 0 repeat  * for >= 1 repeat
                    dp[i%2][j] = dp[i%2][j-2] or (singleMatch(i-1, j-2) and dp[(i-1)%2][j])
        return dp[len(s)% 2][-1]

    # without space optimization
    def isMatch_fullSpace(self, s, p):
        result = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        result[0][0] = True # empty string vs empty pattern
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                result[0][j] = result[0][j-2]

        for i in range(1,len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    result[i][j] = result[i][j-2] or (result[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return result[len(s)][len(p)]

    # cannot handle '.*', should write a match function for a==b or b=='.'
    def isMatch_wrong(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = False if i else True
            for j in range(1, len(p)+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1] if i else False
                elif p[j-1] == '*': # wrong for '.*'
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (i and s[i-1]==p[j-2] and dp[i-1][j])
                else:
                    dp[i][j] = s[i-1] == p[j-1] and dp[i-1][j-1]
        return dp[-1][-1]


# iteration
class Solution3:
    # @return a boolean
    def isMatch(self, s, p):
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        last_ptr = []
        while s_ptr < len(s):
            if p_ptr < len(p) and (p_ptr == len(p) - 1 or p[p_ptr + 1] != '*') and \
            (s_ptr < len(s) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '.')):
                    s_ptr += 1
                    p_ptr += 1
            elif p_ptr < len(p) - 1 and (p_ptr != len(p) - 1 and p[p_ptr + 1] == '*'):
                p_ptr += 2
                last_ptr.append([s_ptr, p_ptr])
            elif  last_ptr:
                [last_s_ptr, last_p_ptr] = last_ptr.pop()
                while last_ptr and p[last_p_ptr - 2] != s[last_s_ptr] and p[last_p_ptr - 2] != '.':
                    [last_s_ptr, last_p_ptr] = last_ptr.pop()

                if p[last_p_ptr - 2] == s[last_s_ptr] or p[last_p_ptr - 2] == '.':
                    last_s_ptr += 1
                    s_ptr = last_s_ptr
                    p_ptr = last_p_ptr
                    last_ptr.append([s_ptr, p_ptr])
                else:
                    return False
            else:
                return False

        while p_ptr < len(p) - 1 and p[p_ptr] == '.' and p[p_ptr + 1] == '*':
            p_ptr += 2

        return p_ptr == len(p)

# recursive, backtrack
class Solution4:
    # @return a boolean
    def isMatch(self, s, p): # Ming
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return len(s) == 1 and (p[0] == '.' or s[0] == p[0])

        if p[1] != '*':
            if len(s) > 0 and (p[0] == '.' or s[0] == p[0]): # cannot be len(s)>1: "a", "ab*"
                return self.isMatch(s[1:], p[1:])
            return False
        else:
            if self.isMatch(s, p[2:]):                # .* match 0 char in s
                return True
            if p[0] == '.':
                for j in xrange(len(s)):
                    if self.isMatch(s[j + 1:], p[2:]):  # .* match 1,2,3... chars in s
                        return True
            else:
                if not s or s[0] != p[0]: return False

                for j in xrange(len(s)):
                    if s[j] != s[0]:
                        break
                    if self.isMatch(s[j + 1:], p[2:]):
                        return True

            return False

    def isMatch_kamyu(self, s, p):
        if not p:
            return not s

        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

if __name__ == "__main__":
    print(Solution().isMatch('a', 'ab*a')) # False
    print(Solution().isMatch("ba", "")) # False
    print(Solution().isMatch("abab", "")) # False
    print(Solution().isMatch("abab", "a*b*")) # False
    print(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")) # False
    print(Solution().isMatch("aa","a")) # False
    print(Solution().isMatch("aa","aa")) # True
    print(Solution().isMatch("aaa","aa")) # False
    print(Solution().isMatch("aa", "a*")) # True
    print(Solution().isMatch("aa", ".*")) # True
    print(Solution().isMatch("ab", ".*")) # True
    print(Solution().isMatch("aab", "c*a*b")) # True
