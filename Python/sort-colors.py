# Time:  O(n)
# Space: O(1)
#
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
# click to show follow up.
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's,
# then overwrite array with total number of 0's, then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?
#


#  荷兰国旗问题：给每个数字设定一种颜色，并按照荷兰国旗颜色顺序对三色进行调整。
# Dutch National Flag Problem

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def triPartition(nums, target):
            i, left, right = 0, 0, len(nums)-1
            while i <= right: # 不能用for loop
                if nums[i] > target: # 右边从2区换过来的数没扫过，i不能前进
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                else: # 包括<=target两种情况，i都要前进。左边从0区换过来的数已经扫过
                    if nums[i] < target:
                        nums[left], nums[i] = nums[i], nums[left]
                        left += 1
                    i += 1

        triPartition(nums, 1)

    def sortColors_wrong(self, nums):
        l, r, i = 0, len(nums)-1, 0
        while i < len(nums): # WRONG: right右边全是2. 如果 i > right继续做，又把2换到中间去了
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        return nums
if __name__ == "__main__":
    for A in ([2,1,1,0,0,2], [2,0,2,1,1,0]):
        Solution().sortColors(A)
        print(A)
