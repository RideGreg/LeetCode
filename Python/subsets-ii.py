# Time:  O(n * 2^n)
# Space: O(1)

# 90
# Given a collection of integers that might contain duplicates, S, return all possible subsets (the power set).
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums): # USE THIS
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]
        previous_size = 0
        for i in range(len(nums)):
            size = len(ans)
            for j in range(size):
                # Only union non-duplicate element or new union set.
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    ans.append(ans[j] + [nums[i]])
            previous_size = size
        return ans


# Time:  O(n * 2^n) ~ O((n * 2^n)^2)
# Space: O(1)
class Solution2(object):
    def subsetsWithDup(self, nums): # ALSO OK: backtracking
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(i, cur):
            if i == len(nums):
                if cur not in ans: # uniqueness check make time complexity quadratic
                    ans.append(cur[:])
                return

            backtrack(i + 1, cur)
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

        nums.sort()
        ans = []
        backtrack(0, [])
        return ans



# Time:  O(n * 2^n) ~ O((n * 2^n)^2)
# Space: O(1)
class Solution3(object):
    def subsetsWithDup(self, nums): # use bitmask idea
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, count = 0, 1 << len(nums)
        nums.sort()

        while i < count:
            cur = []
            for j in range(len(nums)):
                if i & 1 << j:
                    cur.append(nums[j])
            if cur not in result: # uniqueness check make time complexity quadratic
                result.append(cur)
            i += 1

        return result


if __name__ == "__main__":
    print(Solution().subsetsWithDup([1, 2, 2]))
    # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
