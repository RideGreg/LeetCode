# Time:  O(n)
# Space: O(1)

# 1004
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s.

# Sliding window: Find the longest subarray with at most K zeros.
# For each A[j], try to find the longest subarray.
# If A[i] ~ A[j] has zeros <= K, we continue to increment j.
# If A[i] ~ A[j] has zeros > K, we increment i.

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result, i = 0, 0
        for j in range(len(A)):
            K -= 1 - A[j]
            while K < 0:
                K += 1 - A[i]
                i += 1
            result = max(result, j-i+1)
        return result

    # In fact, as we want the maximum window, we don't need to check window of smaller size.
    # The following works: maintain K all the time. for each j, if # of zeros more than K,
    # increemnt starting point i to compensate.
    def longestOnes_better(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:         # no need do while to reduce window size
                K += 1 - A[i]
                i += 1
        return j - i + 1

print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10
