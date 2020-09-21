# Time:  O(n) on average
# Space: O(n)

# 1058
# Given an array of prices [p1,p2...,pn] and a target, round each price pi to Roundi(pi) so that
# the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target. Each operation
# Roundi(pi) could be either Floor(pi) or Ceil(pi).
#
# Return the string "-1" if the rounded array is impossible to sum to target. Otherwise, return the
# smallest rounding error, which is defined as Σ |Roundi(pi) - (pi)| for i from 1 to n, as a string
# with three places after the decimal.
#
# Hint: If we have integer values in the array then we just need to subtract the target
# those integer values, so we reduced the problem.
# Similarly if we have non integer values we have two options to put them flor(value) or
# ceil(value) = floor(value) + 1, so the idea is to just subtract floor(value).
# Now the problem is different for each position we can sum just add 0 or 1 in order to
# sum the target, minimizing the deltas. This can be solved with DP.

import math
import random


class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        def kthElement(nums, k, compare=lambda a, b: a < b):
            def PartitionAroundPivot(left, right, pivot_idx, nums, compare):
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in range(left, right):
                    if compare(nums[i], nums[right]):
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == k:
                    return
                elif new_pivot_idx > k:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k.
                    left = new_pivot_idx + 1
        
        errors = []
        lower, upper = 0, 0
        for i, p in enumerate(map(float, prices)):
            lower += int(math.floor(p))
            upper += int(math.ceil(p))
            if p != math.floor(p):
                errors.append(p-math.floor(p))
        if not lower <= target <= upper:
            return "-1"

        round_down_count = upper-target
        kthElement(errors, round_down_count)
        result = 0.0
        for i in range(len(errors)):
            if i < round_down_count:
                result += errors[i]
            else:
                result += 1.0-errors[i]
        return "{:.3f}".format(result)

print(Solution().minimizeError(["0.700","2.800","4.900"], 8)) # '1.000'
print(Solution().minimizeError(["1.500","2.500","3.500"], 10)) # '-1'