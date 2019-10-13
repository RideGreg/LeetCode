# Time:  O(9^2 * 2^9) = O(41,472)
# Space: O(9 * 2^9)

# 351
# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9,
# count the total # of unlock patterns of the Android lock screen, which consist of
# minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
# 1. Each pattern must connect at least m keys and at most n keys.
# 2. All the keys must be distinct.
# 3. If the line connecting two consecutive keys in the pattern passes through any other
# keys, the other keys must have previously selected in the pattern. No jumps through
# non selected key is allowed.
# 4. The order of keys used matters.
#
# Explanation:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
#
# Invalid move: 4 - 1 - 3 - 6
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
#
# Example:
# Given m = 1, n = 1, return 9.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


# Time:  O(9!) = O(362,880)
# Space: O(9)
# Backtracking solution. (TLE) Similar to Solution_TLE.
class Solution(object): # USE THIS. Easy to write.
    def numberOfPatterns(self, m, n):
        jump = [[0]*10 for _ in range(10)]
        jump[1][3] = jump[3][1] = 2
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[3][9] = jump[9][3] = 6
        jump[4][6] = jump[6][4] = jump[2][8] = jump[8][2] \
            = jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5
        used = [False]*10

        def dfs(length, cur):
            if length > n: return 0
            res = 0
            if m <= length <= n:
                res = 1

            used[cur] = True
            for nxt in range(1, 10):
                if not used[nxt] and (jump[cur][nxt] == 0 or used[jump[cur][nxt]]):
                    res += dfs(length + 1, nxt)
            used[cur] = False
            return res

        return (dfs(1, 1) * 4  # starting with 1,3,7,9
            + dfs(1, 2) * 4  # starting with 2,4,6,8
            + dfs(1, 5))




# DP solution. Hard to remember.
# 一共9 keys, 可表示0-511 in binary. DP list covers 0-511. First loop iterate the DP list
# (O(2^9)) to populate how many ways this number can be constructed with 1-9 as ending number.
# Add the # of ways to every other number can be extended from this number.
# Only count the ways for numbers using [m, n] keys.
#
# used是一个9位的mask，每位对应一个数字，如果为1表示使用，0表示不使用
# number_of_keys 是0-511每个数字使用了几个key
#

class Solution1(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def merge(used, i):
            return used | (1 << i)

        def number_of_keys(i): # get how many bits are set in a number's binary representation
            number = 0
            while i > 0:
                i &= i - 1 # remove least significant 1 from the number
                number += 1
            return number

        def contain(used, i):
            return bool(used & (1 << i))

        def convert(i, j):
            return 3 * i + j

        # dp[i][j]: i is the set of the numbers in binary representation,
        #           dp[i][j] is the number of ways ending with the number j.
        dp = [[0] * 9 for _ in xrange(1 << 9)] # 2D list 512x9
        for i in xrange(9):
            dp[merge(0, i)][i] = 1 # initialization: all single digits end with itself

        res = 0
        for used in xrange(len(dp)): # time complexity O(2^9)
            number = number_of_keys(used)
            if number > n:
                continue

            for i in xrange(9):
                if not contain(used, i): # i is the current key
                    continue

                if m <= number <= n:
                    res += dp[used][i]

                x1, y1 = divmod(i, 3)
                for j in xrange(9): # j is the next key
                    if contain(used, j):
                        continue

                    x2, y2 = divmod(j, 3)
                    if ((x1 == x2 and abs(y1 - y2) == 2) or
                        (y1 == y2 and abs(x1 - x2) == 2) or
                        (abs(x1 - x2) == 2 and abs(y1 - y2) == 2)) and \
                       not contain(used,
                                   convert((x1 + x2) // 2, (y1 + y2) // 2)):
                            continue

                    dp[merge(used, j)][j] += dp[used][i]

        return res


# Time:  O(9^2 * 2^9)
# Space: O(9 * 2^9)
# DP solution. Similar to Solution 1, but use an `exclude` logic.
class Solution2(object):
    def numberOfPatterns(self, m, n):
        def merge(used, i):
            return used | (1 << i)

        def number_of_keys(i):
            number = 0
            while i > 0:
                i &= i - 1
                number += 1
            return number

        def exclude(used, i):
            return used & ~(1 << i)

        def contain(used, i):
            return bool(used & (1 << i))

        def convert(i, j):
            return 3 * i + j

        # dp[i][j]: i is the set of the numbers in binary representation,
        #            d[i][j] is the number of ways ending with the number j.
        dp = [[0] * 9 for _ in xrange(1 << 9)]
        for i in xrange(9):
            dp[merge(0, i)][i] = 1

        res = 0
        for used in xrange(len(dp)):
            number = number_of_keys(used)
            if number > n:
                continue

            for i in xrange(9):
                if not contain(used, i):
                    continue

                x1, y1 = divmod(i, 3)
                for j in xrange(9):
                    if i == j or not contain(used, j):
                        continue

                    x2, y2 = divmod(j, 3)
                    if ((x1 == x2 and abs(y1 - y2) == 2) or
                        (y1 == y2 and abs(x1 - x2) == 2) or
                        (abs(x1 - x2) == 2 and abs(y1 - y2) == 2)) and \
                       not contain(used,
                                   convert((x1 + x2) // 2, (y1 + y2) // 2)):
                            continue

                    dp[used][i] += dp[exclude(used, i)][j]

                if m <= number <= n:
                    res += dp[used][i]

        return res


# Time:  O(9!) = O(362,880)
# Space: O(9)
# Backtracking solution. (TLE)
class Solution_TLE(object):
    def numberOfPatterns(self, m, n):
        def merge(used, i):
            return used | (1 << i)

        def contain(used, i):
            return bool(used & (1 << i))

        def convert(i, j):
            return 3 * i + j

        def numberOfPatternsHelper(m, n, level, used, i):
            number = 0
            if level > n:
                return number

            if m <= level <= n:
                number += 1

            x1, y1 = divmod(i, 3)
            for j in xrange(9):
                if contain(used, j):
                    continue

                x2, y2 = divmod(j, 3)
                if ((x1 == x2 and abs(y1 - y2) == 2) or
                    (y1 == y2 and abs(x1 - x2) == 2) or
                    (abs(x1 - x2) == 2 and abs(y1 - y2) == 2)) and \
                   not contain(used,
                               convert((x1 + x2) // 2, (y1 + y2) // 2)):
                        continue

                number += numberOfPatternsHelper(m, n, level + 1, merge(used, j), j)

            return number

        number = 0
        # 1, 3, 7, 9
        number += 4 * numberOfPatternsHelper(m, n, 1, merge(0, 0), 0)
        # 2, 4, 6, 8
        number += 4 * numberOfPatternsHelper(m, n, 1, merge(0, 1), 1)
        # 5
        number += numberOfPatternsHelper(m, n, 1, merge(0, 4), 4)
        return number


# Sum all the valid patterns when using m, m+1, … n keys together to get the result.
# THIS IS INEFFICIENT, WE SHOULD BUILD m+1 KEYS ON THE TOP OF RESULT OF m KEYS.
# In each case, use DFS to count the number of valid paths from the current number (1–9)to
# the remaining numbers. To optimize, use the symmetry of the 3 by 3 matrix. E.g. start from 1 or 3 or 7 or 9,
# the valid paths number should be the same.

class Solution_repeatedPrevSteps_slow(object):
    def numberOfPatterns(self, m, n):
        # Keep a recod of invalid numbers on the path between two selected keys
        skip = [[0]*10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        visited = [False] * 10

        def DFS(cur, remain):
            if remain == 0:
                return 1

            visited[cur] = True
            ans = 0
            for i in range(1, 10):
                # Next key must be unvisited
                # Current key and next key are adjacent or skip number is already visited
                if not visited[i] and (skip[cur][i] == 0 or visited[skip[cur][i]]):
                    ans += DFS(i, remain-1)
            visited[cur] = False
            return ans

        ans = 0
        for i in range(m, n+1): # BAD BY CHECKING THE KEYS SEPARATELY
            ans += DFS(1, i - 1) * 4
            ans += DFS(2, i - 1) * 4
            ans += DFS(5, i - 1)

        return ans


print(Solution().numberOfPatterns(1,1)) # 9
print(Solution().numberOfPatterns(2,2)) # 56 = 5*4 + 7*4 + 8
print(Solution().numberOfPatterns(3,3)) # 320 = 31(i.e. 66667)*4 + 37(i.e. 4455667)*4 + 48(i.e. 55557777)
print(Solution().numberOfPatterns(2,3)) # 376
print(Solution().numberOfPatterns(1,3)) # 385

