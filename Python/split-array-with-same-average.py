# Time:  O(n^4)
# Space: O(n^3)

# 805
# In a given integer array A, we must move every element of A to
# either list B or list C. (B and C initially start empty.)
#
# Return true if and only if after such a move, it is possible that
# the average value of B is equal to the average value of C, and B and C are both non-empty.
#
# Example :
# Input:
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
#
# Note:
# - The length of A will be in the range [1, 30].
# - A[i] will be in the range of [0, 10000].

# 给定整数数组A，求是否可以将A分成平均数相等的两个非空子数组
# subset sum problem

class Solution(object):
    # O(2^n) for each new number, calc sum of full combinations (2^n) of numbers prior to it
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # sort is necessary to avoid duplicate key and overwrite in dict
        # e.g. in [10,29,13,53,33,48,76,70,5,5]: [76] and [53,13,10] have the same key
        # key 161 ([10,29,13,33,76]=161:5 => [10,33,48,70]=161:4) is before
        # key 166 ([29,13,48,76]=166:4 => [10,53,33,70]=166:4), so when first 5 comes,
        # it overwrites key 166 to 166:5, then creates key 171 to 171:6: fail to find solution.
        A.sort(reverse = True)
        dp = {0 : 0}
        size, total = len(A), sum(A)
        for a in A:
            # sort is necessary to avoid duplicate key and overwrite in dict
            for k in sorted(dp.keys(), reverse = True):
                dp[k + a] = dp[k] + 1
                curSum, cnt = a+k, dp[a+k]
                if cnt and size-cnt and curSum*size == total*cnt:
                    return True
        return False

    def splitArraySameAverage_kamyu(self, A):
        def possible(size, total):
            for avg in range(1, total//2+1):
                if size*avg%total == 0:
                    return True
            return False

        n, s = len(A), sum(A)
        if not possible(n, s):
            return False

        sums = [set() for _ in range(n//2+1)]
        sums[0].add(0)
        for num in A:  # O(n) times
            for i in reversed(range(1, n//2+1)):  # O(n) times
                for prev in sums[i-1]:  # O(1) + O(2) + ... O(n/2) = O(n^2) times
                    sums[i].add(prev+num)
        for i in range(1, n//2+1):
            if s*i%n == 0 and s*i//n in sums[i]:
                return True
        return False


print(Solution().splitArraySameAverage([10,29,13,53,33,48,76,70,5,5])) # True
# 29,13,48,76,5 => avg = 171/5 = 34.2
# 10,53,33,70,5

print(Solution().splitArraySameAverage([1,2,3,4])) # True
