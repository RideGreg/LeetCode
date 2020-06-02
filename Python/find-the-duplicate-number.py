# Time:  O(n)
# Space: O(1)
#
# Given an array nums containing n + 1 integers where each integer
# is between 1 and n (inclusive), prove that at least one duplicate
# element must exist. Assume that there is only one duplicate number,
# find the duplicate one.
#
# Note:
# - You must not modify the array (assume the array is read only).
# - You must use only constant extra space.
# - Your runtime complexity should be less than O(n^2).
#

# Two pointers method, same as Linked List Cycle II.
# 我们对nums数组建图，每个位置 i连一条 i→nums[i] 的边。由于存在的重复的数字 target，因此 target 这个位置
# 一定有起码两条指向它的边，因此整张图一定存在环，要找的target 就是这个环的入口，那么问题就等价于 142环形链表 II。
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # slow = fast = 0 # WRONG: cannot initialize slow/fast to 0 -> they don't enter the 1st while loop.
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# Time:  O(nlogn)
# Space: O(1)
# Binary search method: 定义cnt[i]表示nums数组中小于等于 i的数有多少个，假设重复数target，
# 那么 [1,target−1]里的所有数满足cnt[i]<=i，[target,n] 里的所有数满足cnt[i]>i，具有单调性。
# 答案就是在[1,n]中寻找最小的 i 满足cnt[i]>i。

class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2
            # Get count of num <= mid.
            count = sum(x <= mid for x in nums)
            if count > mid: # mid is ok
                right = mid
            else:
                left = mid + 1
        return left

# Time:  O(n)
# Space: O(n)
class Solution3(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = 0
        # Mark the value as visited by negative.
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                duplicate = abs(num)
                break
        # Rollback the value.
        for num in nums:
            if nums[abs(num) - 1] < 0:
                nums[abs(num) - 1] *= -1
            else:
                break
        return duplicate

print(Solution().findDuplicate([1,3,4,2,2])) # 2