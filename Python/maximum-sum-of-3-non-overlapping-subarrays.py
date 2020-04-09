# Time:  O(n)
# Space: O(n)

# 689
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed).
# If there are multiple answers, return the lexicographically smallest one.
#
# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
 #
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
#
# Note:
# - nums.length will be between 1 and 20000.
# - nums[i] will be between 1 and 65535.
# - k will be between 1 and floor(nums.length / 3).

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k): # USE THIS
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        accu = [0]
        for num in nums:
            accu.append(accu[-1]+num)

        # left_pos[x] is start pos of largest k-size subarray in nums[:x] (included).
        n = len(nums)
        left_pos = [0] * n
        total = accu[k]-accu[0]
        for i in range(k, n):
            cur = accu[i+1] - accu[i+1-k]
            if cur > total:
                left_pos[i], total = i+1-k, cur
            else:
                left_pos[i] = left_pos[i-1]

        # right_pos[x] is start pos of largest k-size subarray in nums[x:] (included).
        right_pos = [n-k] * n
        total = accu[n]-accu[n-k]
        for i in reversed(range(n-k)):
            cur = accu[i+k]-accu[i]
            if cur >= total:    #!!!! THIS IS IMPORTANT need lexicographically smallest when sums are equal
                right_pos[i], total = i, cur
            else:
                right_pos[i] = right_pos[i+1]

        ans, max_sum = [], 0
        for i in range(k, n-2*k+1):
            left, right = left_pos[i-1], right_pos[i+k]
            total = (accu[i+k]-accu[i]) + \
                    (accu[left+k]-accu[left]) + \
                    (accu[right+k]-accu[right])
            if total > max_sum:
                max_sum = total
                ans = [left, i, right]
        return ans

    # 预处理，时间复杂度O(n)
    # 构造K项和数组sums，sums[i] = sum(nums[i .. i + k - 1]) !!<- this sums is complex than accu in above solution
    # 从左向右构造K项和最大值及其下标数组maxa，其元素记为va, ia。maxa[x]为以x及其以前元素为开头的正向K项和最大值。
    # 从右向左构造K项和最大值及其下标数组maxb，其元素记为vb, ib。maxb[x]为以x及其以后元素为开头的反向K项和最大值。
    #
    # 在[k, nsize - k)范围内枚举中段子数组的起点x
    # 则3段子数组和 = sums[x] + va + vb
    def maxSumOfThreeSubarrays_bookshadow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        nsize = size - k + 1
        sums = [0] * nsize
        maxa = [0] * nsize
        maxb = [0] * nsize
        total = 0
        for x in range(size):
            total += nums[x]
            if x >= k - 1:
                sums[x - k + 1] = total
                total -= nums[x - k + 1]
        maxn, maxi = 0, 0
        for x in range(nsize):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxa[x] = (maxn, maxi)
        maxn, maxi = 0, nsize - 1
        for x in range(nsize - 1, -1, -1):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxb[x] = (maxn, maxi)
        ansn, ansi = 0, None
        for x in range(k, nsize - k):
            va, ia = maxa[x - k]
            vb, ib = maxb[x + k]
            if sums[x] + va + vb > ansn:
                ansn = sums[x] + va + vb
                ansi = [ia, x, ib]
        return ansi


    # TLE O(n^2), filled upper triangle of 2D DP array, actually only need to fill 1 row dp[0][:] and 1 column dp[:][N-1]
    def maxSumOfThreeSubarrays_ming(self, nums, k):
        N = len(nums)
        dp = [[0] * N for _ in range(N)]  # store the sum of nums[i:j+1]
        idx = [[0] * N for _ in range(N)] # store the starting idx of largest k-size subarray in nums[i:j+1]

        # prepare the data
        for i in range(N - k + 1):
            dp[i][i + k - 1] = sum(nums[i:i + k])
            idx[i][i + k - 1] = i
        for size in range(k + 1, N + 1):
            for i in range(N - size + 1):
                j = i + size - 1
                if dp[i][j - 1] >= dp[i + 1][j]:
                    dp[i][j] = dp[i][j - 1]
                    idx[i][j] = idx[i][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j]
                    idx[i][j] = idx[i + 1][j]

        # divide the whole array into 3 parts
        max_sum, max_i, max_j, max_k = float('-inf'), None, None, None
        for i in range(k, N - 2 * k + 1):
            ssum = dp[0][i - 1] + dp[i][i+k-1] + dp[i+k][N - 1]
            if ssum > max_sum:
                max_sum, max_i, max_j, max_k = ssum, idx[0][i - 1], idx[i][i+k-1], idx[i+k][N - 1]
        return [max_i, max_j, max_k]

print(Solution().maxSumOfThreeSubarrays([9,8,7,6,2,2,2,2], 2)) # [0,2,4]
print(Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)) # [0,3,5]
print(Solution().maxSumOfThreeSubarrays([1,2,1,1,2,6,2,2,1], 2)) # [0,4,6]
print(Solution().maxSumOfThreeSubarrays([1,2,1,1,2,6,2,2,2,1], 2)) # [0,4,6]