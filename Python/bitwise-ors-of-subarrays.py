# Time:  O(32 * n), each intermediate set have no more than 32 unique values.
# Space: O(1)

# 898
# We have an array A of non-negative integers.
#
# For every (contiguous) subarray B = [A[i], A[i+1], ...,
#                                      A[j]] (with i <= j),
# we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].
#
# Return the number of possible results.
# (Results that occur more than once are only counted once in the final answer.)
#
# Example 1:
#
# Input: [0]
# Output: 1
# Explanation: 
# There is only one possible result: 0.
# Example 2:
#
# Input: [1,1,2]
# Output: 3
# Explanation: 
# The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.
# Example 3:
#
# Input: [1,2,4]
# Output: 6
# Explanation: 
# The possible results are 1, 2, 3, 4, 6, and 7.
#
# Note:
# - 1 <= A.length <= 50000
# - 0 <= A[i] <= 10^9

# Solution: note of the fact that for subarray A[i], ... A[j+1],
# result(i, j+1) = result(i, j) | A[j+1].
# Time complexity is not bounded by O(n^2). In fact, any result set can have
# unique values at most 32, because when building a result set, each new inserted
# value must have more 1s' in its binary representation (to a maximum of 32 ones).

class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans, curr = set(), set()
        for x in A:
            curr = {x} | {x | y for y in curr}
            ans |= curr
        return len(ans)
