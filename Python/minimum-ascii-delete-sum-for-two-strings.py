# Time:  O(m * n)
# Space: O(n)

# 712
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
#
# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
#
# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
#
# Note:
# - 0 < s1.length, s2.length <= 1000.
# - All elements of each string will have an ASCII value in [97, 122].

# DP with rolling window
class Solution(object):

    def minimumDeleteSum(self, s1: str, s2: str) -> int: # USE THIS: ming's soluion, min delete equivalent to max keep
        s1, s2 = list(map(ord, s1)), list(map(ord, s2))
        sum1, sum2 = sum(s1), sum(s2)
        if sum1 == 0:
            return sum2
        elif sum2 == 0:
            return sum1

        dp = [0] * len(s2)
        for m in s1:
            ndp = [max(dp[0], m * (m == s2[0]))]
            for j in range(1, len(s2)):
                if m == s2[j]:
                    ndp.append(dp[j - 1] + m)
                else:
                    ndp.append(max(ndp[-1], dp[j]))
            dp = ndp
        return sum1 + sum2 - 2 * dp[-1]

    def minimumDeleteSum_bookshadow(self, s1, s2): # also good, not do complimentary
        a1, a2 = map(ord, s1), map(ord, s2)
        l1, l2 = len(s1), len(s2)
        dp = [0]
        for x in range(l1):
            dp.append(dp[-1] + a1[x])
        for x in range(1, l2 + 1):
            ndp = [dp[0] + a2[x - 1]]
            for y in range(1, l1 + 1):
                if a2[x - 1] == a1[y - 1]: ndp.append(dp[y - 1])
                else: ndp.append(min(dp[y] + a2[x - 1], ndp[y - 1] + a1[y - 1]))
            dp = ndp
        return dp[-1]


    def minimumDeleteSum_kamyu(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2)+1) for _ in xrange(2)]
        for j in xrange(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])

        for i in xrange(len(s1)):
            dp[(i+1)%2][0] = dp[i%2][0] + ord(s1[i])
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j]
                else:
                    dp[(i+1)%2][j+1] = min(dp[i%2][j+1] + ord(s1[i]), \
                                           dp[(i+1)%2][j] + ord(s2[j]))

        return dp[len(s1)%2][-1]


# Time:  O(m * n)
# Space: O(m * n)
class Solution2(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2)+1) for _ in xrange(len(s1)+1)]
        for i in xrange(len(s1)):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for j in xrange(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])

        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1] + ord(s1[i]), \
                                       dp[i+1][j] + ord(s2[j]))

        return dp[-1][-1]

print(Solution().minimumDeleteSum("sea", "eat")) # 231
print(Solution().minimumDeleteSum("delete", "leet")) # 403
