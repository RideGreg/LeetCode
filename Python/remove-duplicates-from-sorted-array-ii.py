# Time:  O(n)
# Space: O(1)
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array A = [1,1,1,2,2,3],
#
# Your function should return length = 5, and A is now [1,1,2,2,3].
#

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates_brief(self, A): # USE THIS PASSED
        if len(nums) < 3: return len(nums)
        prev = 0
        for i in xrange(2, len(nums)):
            if nums[prev] != nums[i]:
                prev += 1
                nums[prev+1] = nums[i]
        return prev + 2

    def removeDuplicates(self, A):
        if not A:
            return 0

        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i += 1

        return last + 1

if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
