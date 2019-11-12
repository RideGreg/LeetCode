# Time:  O(n * k)
# Space: O(k)

# 629 求数字1到n的排列中，逆序对个数恰好为k的排列数
#
# Given two integers n and k, find how many different arrays consist of numbers
# from 1 to n such that there are exactly k inverse pairs.
#
# We define an inverse pair as following: For ith and jth element in the array,
#     if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.
#
# Since the answer may very large, the answer should be modulo 109 + 7.
#
# Example 1:
# Input: n = 3, k = 0
# Output: 1
# Explanation:
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
# Example 2:
# Input: n = 3, k = 1
# Output: 2
# Explanation:
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
# Note:
# The integer n is in the range [1, 1000] and k is in the range [0, 1000].


# DP: 求递推式，时间复杂度O(n * k)
#
# 观察下列推导过程：
#
# 当n=1时，k的取值范围是[0, 0]
# k   c
# 0 1 1
#
# 当n=2时，k的取值范围是[0, 1]
# k   c
# 0 1 1
# 1 1 1
#
# 当n=3时，k的取值范围是[0, 3]
# k       c
# 0 1     1
# 1 1 1   2
# 2   1 1 2
# 3     1 1
# Explain: 1st column is to start w/ digit 1: 1,[2,3], 1,[3,2]. Inverse pairs same as n=2: {0:1, 1:1}
# 2nd column is to start w/ digit 2: 2,[1,3], 2,[3,1]. Inverse pairs are 1 more than that of n=2: {1:1, 2:1}
# 3rd column is to start w/ digit 3: 3,[1,2], 3,[2,1]. Inverse pairs are 2 more than that of n=2: {2:1, 3:1}
# Then sum for all k.

# 当n=4时，k的取值范围是[0, 6]
# k         c
# 0 1       1
# 1 2 1     3
# 2 2 2 1   5
# 3 1 2 2 1 6
# 4   1 2 2 5
# 5     1 2 3
# 6       1 1
# Explain: in middle, 1st, 2nd, 3rd and 4th columns are inverse pairs when the permutation starting with digit 1,2,3,4.
#
# 当n=5时，k的取值范围是[0, 10]
# k            c
# 0  1         1
# 1  3 1       4
# 2  5 3 1     9
# 3  6 5 3 1   15
# 4  5 6 5 3 1 20
# 5  3 5 6 5 3 22
# 6  1 3 5 6 5 20
# 7    1 3 5 6 15
# 8      1 3 5 9
# 9        1 3 4
# 10         1 1

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [1] + [0] * k # store # of permutations with 0 -> k inverse pairs
        for x in range(2, n + 1):
            ndp = [1] + [0] * k
            for y in range(1, k + 1):
                ndp[y] = (ndp[y-1] + dp[y]) % MOD
                if y >= x:
                    ndp[y] = (ndp[y] - dp[y-x]) % MOD
            dp = ndp
        return dp[k]


    # hard to understand
    # To save space: for each x in [1,n], don't allocate space for k > (1+2+..+(n-1)) which are always 0
    # in case k is unnecessarily large
    def kInversePairs_bookshadow(self, n, k):
        MOD = 10**9 + 7
        dp = [1]
        for x in range(2, n + 1):
            ndp = []
            num = 0
            for y in range(min(1 + x * (x - 1) / 2, k + 1)):
                if y < len(dp): num = (num + dp[y]) % MOD
                if y >= x: num = (MOD + num - dp[y - x]) % MOD
                ndp.append(num)
            dp = ndp
        return k < len(dp) and dp[k] or 0

print(Solution().kInversePairs(5, 5)) # 22
print(Solution().kInversePairs(5, 7)) # 15
print(Solution().kInversePairs(5, 15)) # 0
