# Time:  O(n)
# Space: O(1)

# Given an array A of non-negative integers,
# return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3]
# would also be accepted.
#
# Note:
# - 1 <= A.length <= 5000
# - 0 <= A[i] <= 5000

class Solution(object):
    # Two pointers: fast pointer to overwrite slow pointer
    def sortArrayByParity(self, A): # USE THIS
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A

    # Two pointers start/end, need several while
    def sortArrayByParity_ming(self, A): # USE THIS
        l, r = 0, len(A) - 1
        while l < r:
            while l < r and A[l] % 2 == 0:
                l += 1
            while l < r and A[r] % 2:
                r -= 1
            A[l], A[r] = A[r], A[l]  # no need to increment/decrement index here, next while loop will do
        return A

    def sortArrayByParity_LeetCodeOfficial(self, A): # not straitforward, usually we don't do switch before increment
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1 # don't use while here, one while in top is enough
            if A[j] % 2 == 1: j -= 1

        return A

print(Solution().sortArrayByParity([3,1,2,4])) # [4,2,1,3]