# Time:  O(n^2)
# Space: O(n)

# 673
# Given an unsorted array of integers, find the number of longest increasing subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are
# 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed
# to be fit in 32-bit signed int.


# 给定未排序的整数，计算最长递增子序列的个数。
# DP: 数组length[x], count[x]分别表示以x结尾的子序列中最长子序列的长度和个数

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        max_len, max_count = 0, 0
        length = [1] * N
        count = [1] * N
        for j in range(N):
            for i in range(j):
                if nums[i] < nums[j]:
                    v = 1 + length[i]
                    if v > length[j]:
                        length[j], count[j] = v, count[i]
                    elif v == length[j]:
                        count[j] += count[i]

            if length[j] > max_len:
                max_len, max_count = length[j], count[j]
            elif length[j] == max_len:
                max_count += count[j]
        return max_count

# 必须存以当前元素(比如5)结尾的最长子序列的个数，不然无法统计以7结尾的最长子序列的个数
print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2])) # 3

# 更新全局统计量max_len, max_count必须在当前元素已经处理完后进行
print(Solution().findNumberOfLIS([2,2,2,2,2])) # 5

# 全局统计量max_len, max_count必须初始化为0，edge case空数组
print(Solution().findNumberOfLIS([])) # 0