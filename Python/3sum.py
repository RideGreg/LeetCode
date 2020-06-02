# Time:  O(n^2)
# Space: O(1)

# 15
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)

import collections


class Solution(object):
    # 排序 + 双指针
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result = sorted(nums), []
        for i in range(len(nums) - 2):
            if nums[i] > 0: break # no need to calculate more

            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
        return result
        # duplicate triple can be filtered at the end: list(map(list, set(ans)))

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = collections.Counter(nums)
        nums_2 = [x[0] for x in d.items() if x[1] > 1] # all nums appearing at least twice
        nums_unique = sorted([x[0] for x in d.items()]) # all unique nums
        rtn = [[0, 0, 0]] if d[0] >= 3 else []
        for i, j in enumerate(nums_unique):
            if j <= 0: # smallest num must <= 0 for sum = 0
                numss2 = nums_unique[i + 1:]
                for x, y in enumerate(numss2):
                    # if 3rd number repeat, it must be in duplicate set, or all 3 numbers are different
                    if (0 - j - y in [j, y] and 0 - j - y in nums_2) \
                        or (0 - j - y not in [j, y] and 0 - j - y in nums_unique):
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
        return rtn

print(Solution().threeSum2([-1,0,1,2,-1,-4])) # [[-1,-1,2], [-1,0,1]]
print(Solution().threeSum2([-2,0,1,1,2])) # [[-2,0,2],[-2,1,1]]
