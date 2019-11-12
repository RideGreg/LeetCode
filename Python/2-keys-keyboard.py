# Time:  O(sqrt(n))
# Space: O(1)

# 650
# Initially on a notepad only one character 'A' is present.
# You can perform two operations on this notepad for each step:
#
# Copy All: You can copy all the characters present on the notepad
# (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given a number n.
# You have to get exactly n 'A' on the notepad by performing the minimum
#  number of steps permitted.
# Output the minimum number of steps to get n 'A'.
#
# Example 1:
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Note:
# The n will be in the range [1, 1000].


class Solution(object):
    # Math: the answer is the sum of prime factors
    # f(x) = f(x/2) + f(2) = ..., or f(x) = f(x/3) + f(3) = ...
    # The prime factorizaiton is unique. 
    # To get each prime number n, n ops "cpp...ppp" is needed
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans, p = 0, 2
        while p**2 <= n:
            while n % p == 0: # a factor that can be repeatedly used
                ans += p      # number of ops to generate a prime times of 'A' is itself
                n //= p       # floor/integer division, also ok to use true division
            p += 1
        if n > 1:
            ans += n          # remaining prime, itself
        return ans

    # DP: dp[n]表示生成n个字符所需的最小操作次数
    # dp[0, .. , n]初始为∞
    # dp[0] = dp[1] = 0
    #
    # 状态转移方程：
    # dp[x] = min(dp[x], dp[y] + dp[x / y]) ，y ∈[1, x) 并且 x % y == 0
    #
    # Note: this equation is wrong dp[x] = min(dp[x], dp[y] + x / y) because dp[x/y] <= x/y
    #       but the final answer is same and correct.
    def minSteps2(self, n: int) -> int:
        dp = [0, 0] + list(range(2, n+1))
        for x in range(2, n+1):
            for r in range(1, x):
                if x % r == 0:
                    dp[x] = min(dp[x], dp[r] + x//r)
        return dp[n]

    # The iteration has some problems. List 2 implementations and why they are wrong.
    def minSteps3(self, n: int) -> int:
        dp = [0, 0] + list(range(2, n+1))
        for x in range(2, n+1):
            for r in range(1, int(x**0.5)+1): # this upper bound is problematic
                if x % r == 0:
                    dp[x] = min(dp[x], dp[r]+x//r)     # wrong, x//r >= dp[x//r]. Don't actually need x//r ops.
                    dp[x] = min(dp[x], dp[r]+dp[x//r]) # wrong, dp[x//r] not calculated yet.
        return dp[n]

print(Solution().minSteps(9)) # 6 = 3+3
print(Solution().minSteps(10)) # 7 = 2+5
print(Solution().minSteps(11)) # 11 = 11
print(Solution().minSteps(12)) # 7 = 2+2+3
print(Solution().minSteps(71)) # 71
