# Time:  O(n^3)
# Space: O(1)
# http://www.sigmainfy.com/blog/summary-of-ksum-problems.html
#
# Given an array S of n integers, 
# are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Given an array S of n integers, 

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


# Two pointer solution. (1356ms)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res


# Time:  O(n^2 * p)
# Space: O(n^2 * p)
# Hash solution. (224ms)
class Solution2(object):
    def fourSum(self, nums, target):
        import collections
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                is_duplicated = False
                for [x, y] in lookup[nums[i] + nums[j]]:
                    if nums[x] == nums[i]:
                        is_duplicated = True
                        break
                if not is_duplicated:
                    lookup[nums[i] + nums[j]].append([i, j])
        ans = {}
        for c in xrange(2, len(nums)):
            for d in xrange(c+1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for [a, b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            quad_hash = " ".join(map(str,quad))
                            if quad_hash not in ans:
                                ans[quad_hash] = True
                                result.append(quad)
        return result


# Time:  O(n^2 * p) ~ O(n^4)
# Space: O(n^2)
class Solution3(object):   # USE THIS, fastest
    def fourSum(self, nums, target):
        import collections
        nums, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                lookup[nums[i] + nums[j]].append([i, j])

        result, resultSet = [], set()
        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and \
                           b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            quad_hash = ' '.join(map(str,quad))
                            if quad_hash not in resultSet:
                                resultSet.add(quad_hash)
                                result.append(quad)
        return result

import timeit
# 1.3177011013
# 0.589632987976
# 0.163089036942
print timeit.timeit('Solution().fourSum([1, 0, -1, 0, -2, 2, 7,8,9,7,8,9,11,12,13]+range(50), 0)', 'from __main__ import Solution', number=100)
print timeit.timeit('Solution2().fourSum([1, 0, -1, 0, -2, 2, 7,8,9,7,8,9,11,12,13]+range(50), 0)', 'from __main__ import Solution2', number=100)
print timeit.timeit('Solution3().fourSum([1, 0, -1, 0, -2, 2, 7,8,9,7,8,9,11,12,13]+range(50), 0)', 'from __main__ import Solution3', number=100)