# Time:  O(n)
# Space: O(1)

# 398
# Given an array of integers with possible duplicates,
# randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large.
# Solution that uses too much extra space will not pass the judge.
#
# Example:
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly.
# Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);

import random
from typing import List
class Solution(object):
    def __init__(self, nums: List[int]):
        self.__nums = nums

    def pick(self, target: int) -> int:
        reservoir = -1
        n = 0 # count of matched nums
        for i in range(len(self.__nums)):
            if self.__nums[i] == target:
                # when count of matched nums are n+1, only 1/(n+1) chance picking i (last index)
                # n/(n+1) chance picking previous reservoir which is evenly distributed cross [1,n]
                reservoir = i if random.randint(1, n+1) == 1 else reservoir
                n += 1
        return reservoir

# space complexity: O(n) not good
class Solution2(object):
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cand = [i for i, x in enumerate(self.nums) if x == target] # take O(n) space
        return random.choice(cand)

# Your Solution object will be instantiated and called as such:
obj = Solution([3,3,1,2,3])
print(obj.pick(1)) # 2
for _ in range(10):
    print(obj.pick(3))  # 0 or 1 or 4