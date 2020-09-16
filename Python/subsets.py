# Time:  O(n * 2^n)
# Space: O(1)

# 78
# Given a set of DISTINCT integers, S, return all possible subsets (the power set).
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums): # USE THIS: space O(1)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]
        for num in nums:
            #This works, get the size of prev list
            size = len(ans)
            for j in range(size):
                ans.append(ans[j] + [num])

            # or use the concise version
            # result.extend([cur + [num] for cur in result])

            ''' WRONG!! infinity loop, iterate and edit the same list
            for cur in result:
                result.append(cur + [num])
            '''
        return ans


    def subsets2(self, nums): # USE THIS TOO: standard backtracking, space O(n) recursion stack cost.
        def backtrack(i, cur):
            if i == len(nums):
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

    def subsets3(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(2 ** n):
            # generate bitmask, from 0..00 to 1..11. Append subset corresponding to that bitmask
            # '000' -> []
            # '101' -> [1, 3]
            # '111' -> [1,2,3]
            bitmask = bin(i)[2:].zfill(n)
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return ans


# Time:  O(n * 2^n)
# Space: O(1)
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, count = 0, 1 << len(nums)
        nums.sort()

        while i < count:
            cur = []
            for j in xrange(len(nums)):
                if i & 1 << j:
                    cur.append(nums[j])
            result.append(cur)
            i += 1

        return result


# Time:  O(n * 2^n)
# Space: O(1)
class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsRecu([], sorted(nums))

    def subsetsRecu(self, cur, nums):
        if not nums:
            return [cur]

        return self.subsetsRecu(cur, nums[1:]) + self.subsetsRecu(cur + [nums[0]], nums[1:])


if __name__ == "__main__":
    print(Solution().subsets([1, 3, 2]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]