# Time:  O(n)
# Space: O(1)

# 27
# Given an array and a value, remove all instances of that value in place and return the new length.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#

# solution: two pointers
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, nums, val):
        j = 0
        for n in nums:
            if n != val:
                nums[j] = n
                j += 1
        return j

    # When the elem to remove are rare. This solution changes the order of remaining elem.
    def removeElement2(self, A, elem):
        i, last = 0, len(A) - 1
        while i <= last:     # 'last' is last valid, so need to check 'last'
            if A[i] == elem: # not convenient to use for loop as i doesn't increment in this case
                A[i] = A[last]
                last -= 1
            else:
                i += 1
        return last + 1

if __name__ == "__main__":
    print(Solution().removeElement([3,2,2,3], 3)) # 2
    print(Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 2)) # 4