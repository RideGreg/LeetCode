# Time:  O(m * n)
# Space: O(k)

# 1337 weekly contest 174 2/1/2020

# Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
# return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.
#
# A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers
# in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand
# in the frontier of a row, that is, always ones may appear first and then zeros.

# 2 <= n, m <= 100

# ituition: special matrix (all ones appear before zeros), each row sorted, no more sorting needed.
# Traverse by column to find zeros (weaker rows). If not enough, add all-one rows starting from smallest row id.
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        result, lookup = [], set()
        for j in xrange(len(mat[0])):
            for i in xrange(len(mat)):
                if mat[i][j] or i in lookup:
                    continue
                lookup.add(i)
                result.append(i)
                if len(result) == k:
                    return result
        for i in xrange(len(mat)):
            if i in lookup:
                continue
            lookup.add(i)
            result.append(i)
            if len(result) == k:
                break
        return result


# Time:  O(m * n)
# Space: O(k)
import collections


class Solution2(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        lookup = collections.OrderedDict()
        for j in xrange(len(mat[0])):
            for i in xrange(len(mat)):
                if mat[i][j] or i in lookup:
                    continue
                lookup[i] = True
                if len(lookup) == k:
                    return lookup.keys()
        for i in xrange(len(mat)):
            if i in lookup:
                continue
            lookup[i] = True
            if len(lookup) == k:
                break
        return lookup.keys()


# Time:  O(m * n + klogk) quick select
# Space: O(m)
import random


class Solution3(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def partition_around_pivot(left, right, pivot_idx, nums, compare):
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in xrange(left, right):
                    if compare(nums[i], nums[right]):
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_idx = partition_around_pivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == n:
                    return
                elif new_pivot_idx > n:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < n
                    left = new_pivot_idx + 1
        
        nums = [(sum(mat[i]), i) for i in range(len(mat))]
        nth_element(nums, k)
        return map(lambda x: x[1], sorted(nums[:k]))

    # full sort has worse Time:  O(m * n + mlogm)
    def kWeakestRows_ming(self, mat, k):
        v = [(sum(mat[i]), i) for i in range(len(mat))]
        v.sort(key=lambda x: (x[0], x[1])) # O(mlogm)
        return [i for s, i in v[:k]]

print(Solution().kWeakestRows([
 [1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]
], 3)) # [2,0,3]