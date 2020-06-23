# Time:  O(n)
# Space: O(1)
# 80
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
    def removeDuplicates(self, nums): # USE THIS: maintain a count, so no need to look back k times
        i, count = 1, 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                count += 1
            else:
                count = 1 # reset count for new elem

            if count <= 2:
                nums[i] = nums[j]
                i += 1
        return i

    # O(n * k), n is length of nums, k is duplicates allowed
    def removeDuplicates_moreTime(self, nums):
        def isDiff(cur, lastWrite): # retrace k times
            dupAllow = 2
            return any(nums[cur] != nums[lastWrite-d] for d in range(dupAllow))

        i = 2
        for j in range(2, len(nums)):
            if isDiff(j, i-1):
                nums[i] = nums[j]
                i += 1
        return i

    def removeDuplicates2(self, A): # not easy to scale if duplicates allowed more than twice
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

    # left is same number doesn't mean all previous k numbers are same
    def removeDuplicates_wrong(self, nums): # wrong for [3,1,3]
        if len(nums) < 3: return len(nums)
        left = 0
        for i in range(2, len(nums)):
            if nums[left] != nums[i]:
                nums[left+2] = nums[i]
                left += 1
        return left + 2

if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3])) # 5
    print(Solution().removeDuplicates([3, 1, 3])) # 3
