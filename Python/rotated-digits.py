# Time:  O(logn)
# Space: O(logn)

# 788
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.
# A number is valid if each digit remains a digit after rotation.
# 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other;
# 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
#
# Note:
# - N  will be in range [1, 10000].

# memoization (top-down dp)
class Solution(object):  # no time to research/remember this
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = list(map(int, str(N)))
        invalid, diff = set([3, 4, 7]), set([2, 5, 6, 9])

        def dp(i, is_prefix_equal, is_good):
            if i == len(A): return int(is_good)
            if (i, is_prefix_equal, is_good) not in lookup:
                result = 0
                for d in range(A[i]+1 if is_prefix_equal else 10):
                    if d in invalid: continue
                    result += dp(i+1,
                                 is_prefix_equal and d == A[i],
                                 is_good or d in diff)
                lookup[i, is_prefix_equal, is_good] = result
            return lookup[i, is_prefix_equal, is_good]

        lookup = {}
        return dp(0, True, False)


# Time:  O(n)
# Space: O(n)
class Solution2(object):  # USE THIS
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        INVALID, SAME, DIFF = 0, 1, 2
        same, diff, ans = [0, 1, 8], [2, 5, 6, 9], 0
        dp = [0] * (N+1) # INVALID is default
        dp[0] = SAME
        for i in range(N//10+1):
            if dp[i] != INVALID:
                for j in same:
                    if i*10+j <= N:
                        dp[i*10+j] = max(SAME, dp[i])
                        if dp[i*10+j] == DIFF:
                            ans += 1
                for j in diff:
                    if i*10+j <= N:
                        dp[i*10+j] = DIFF
                        ans += 1
        return ans


# Time:  O(nlogn) = O(n), because O(logn) = O(32) by this input
# Space: O(logn) = O(1)
class Solution3(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        invalid, diff = set(['3', '4', '7']), set(['2', '5', '6', '9'])
        ans = 0
        for n in range(N+1):
            nset = set(str(n))
            if (not invalid & nset) and (diff & nset):
                ans += 1
        return ans

print(Solution3().rotatedDigits(123445)) # 22233
