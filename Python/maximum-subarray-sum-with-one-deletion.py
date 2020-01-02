
# 1186 weekly contest 153 9/7/2019
# Given an array of integers, return the maximum sum for a non-empty subarray (contiguous
# elements) with at most one element deletion. In other words, you want to choose a subarray
# and optionally delete one element from it so that there is still at least one element left
# and the sum of the remaining elements is maximum possible.
#
# Note that the subarray needs to be non-empty after deleting one element.

class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result, prev, curr = float("-inf"), float("-inf"), float("-inf")
        for x in arr:
            curr = max(prev, curr+x, x) # max up to this elem, may contain or not contain this elem
            result = max(result, curr)
            prev = max(prev+x, x) # max up to this elem, must include this elem
        return result

    def maximumSum_ming(self, arr): # USE THIS: easy to understand
        n = len(arr)
        forw, back = [0]*n, [0]*n
        cur = 0
        for i in range(n):
            cur = max(cur, 0) + arr[i]
            forw[i] = cur
        ans = max(forw) # don't delete elem

        cur = 0
        for i in range(n-1, -1, -1):
            cur = max(cur, 0) + arr[i]
            back[i] = cur
        ans2 = max(forw[i-1]+back[i+1] for i in range(1, n-1)) # delete one elem

        return max(ans, ans2)

print(Solution().maximumSum([1,-2,0,3])) # 4
print(Solution().maximumSum([1,-2,-2,3])) # 3
print(Solution().maximumSum([-2, -3, 4, -1, -2, 1, 5, -3])) # 9