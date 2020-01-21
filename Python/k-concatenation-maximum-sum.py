# Time:  O(n)
# Space: O(1)

# 1191 weekly contest 154 9/14/2020

# Given an integer array arr and an integer k, modify the array by repeating it k times.
#
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].
#
# Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.
#
# As the answer can be very large, return the answer modulo 10^9 + 7.

# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4

# Just need to handle two repeated arr. If the result cross 3 or more arrs,
# all the arr above 2 would be full arr.
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def kadane_k(arr, k):
            result, curr = float("-inf"), float("-inf")
            for _ in range(k):
                for x in arr:
                    curr = max(curr+x, x)
                    result = max(result, curr)
            return result
        
        MOD = 10**9+7
        if k == 1:
            return max(kadane_k(arr, 1), 0) % MOD
        ans = max(kadane_k(arr, 2), 0) % MOD
        if sum(arr) > 0:
            ans += (k-2) * sum(arr)
        return ans % MOD

print(Solution().kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4], 5)) # 20
print(Solution().kConcatenationMaxSum([1,2], 3)) # 9
print(Solution().kConcatenationMaxSum([1,-2,1], 5)) # 2
print(Solution().kConcatenationMaxSum([-1,-2], 7)) # 0