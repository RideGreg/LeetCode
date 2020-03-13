# Time:  O(n)
# Space: O(1)
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
#

class Solution(object):  # USE THIS: backward scan, break after find the first item
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                k = i
                break
        else:
            nums.reverse()
            return

        for i in reversed(range(k+1, len(nums))):
            if nums[i] > nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]

        nums[k+1:] = nums[:k:-1] # reverse scan from last to k+1 [right:left:-1]
        

# Time:  O(n)
# Space: O(1)
class Solution2(object): # forward scan, don't break: find the last item for k and l
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i

        if k == -1:
            nums.reverse()
            return

        for i in range(k+1, len(nums)):
            if nums[i] > nums[k]:
                l = i
        nums[k], nums[l] = nums[l], nums[k]

        nums[k+1:] = nums[:k:-1]


if __name__ == "__main__":
    num = [1,9,0,2,5,4,1]
    Solution().nextPermutation(num)
    print(num) # 1,9,0,4,1,2,5

    num = [2, 4, 3, 1]
    Solution().nextPermutation(num)
    print(num) # 3,1,2,4
    Solution().nextPermutation(num)
    print(num) # 3,1,4,2
    Solution().nextPermutation(num)
    print(num) # 3,2,1,4
