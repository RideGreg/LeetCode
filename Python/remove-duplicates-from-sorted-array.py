# Time:  O(n)
# Space: O(1)
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].
#


class Solution(object):
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1 # the position ready to be written
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]: # also ok to check nums[j] != nums[i-1], where i-1 is last written
                nums[i] = nums[j]
                i += 1
        return i

    # 写入次数少，但最后输出长度要加一
    def removeDuplicates2(self, A):
        if not A:
            return 0

        last = 0 # the position already written last time
        for i in xrange(len(A)):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
        return last + 1
