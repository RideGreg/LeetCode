# Time:  O(n^3)
# Space: O(n^2)

# 664
# There is a strange printer with the following two special requirements:
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from
# and ending at any places, and will cover the original existing characters.
#
# Given a string consists of lower English letters only,
# your job is to count the minimum number of turns the printer needed in order to print it.
#
# Example 1:
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from
# the second place of the string, which will cover the existing character 'a'.
#
# Hint: Length of the given string will not exceed 100.



# DP: similar to but much easier than 546 remove boxes

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(l, r):
            if l > r: return 0
            if not dp[l][r]:
                v = dfs(l, r-1) + 1
                for i in range(l, r):
                    if ch[i] == ch[r]:
                        v = min(v, dfs(l, i) + dfs(i+1, r-1))
                dp[l][r] = v
            return dp[l][r]

        ch = []
        for c in s:
            if not ch or ch[-1] != c:
                ch.append(c)

        M = len(ch)
        dp = [[0] * M for _ in range(M)]
        return dfs(0, M-1)

    '''
    bookshadow: 动态规划（Dynamic Programming）

    dp[i][j]表示打印下标[i .. j]的子串所需的最少打印次数；记目标串为s
    状态转移方程为：
    dp[y][x] = min(dp[y][x], dp[y][z-1] + dp[z][x-1] + k)   当s[x-1] != s[z-1]时k取值1，否则k取值0

    JAVA code
    class Solution {
        public int strangePrinter(String s) {
            int size = s.length();
            int[][] dp = new int[size + 1][size + 1];
            for (int x = 1; x <= size; x++) {
                for (int y = 1; y <= x; y++) {
                    dp[y][x] = x - y + 1;
                    for (int z = y; z < x; z++) {
                        dp[y][x] = Math.min(dp[y][x], dp[y][z - 1] + dp[z][x - 1] + 
                                (s.charAt(x - 1) != s.charAt(z - 1) ? 1 : 0));
                    }
                }
            }
            return size > 0 ? dp[1][size] : 0;
        }
    }
    '''


print(Solution().strangePrinter("aaabbb")) # 2
print(Solution().strangePrinter("aba")) # 2
print(Solution().strangePrinter("abbaabba")) # 3
print(Solution().strangePrinter("abbaadda")) # 3
print(Solution().strangePrinter("abdddada")) # 4
