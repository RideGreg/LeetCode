# Time:  O(n * n!)
# Space: O(n)
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
#

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    def permuteUnique(self, num):
        def backtrack(cur):
            if len(cur) == len(num):
                result.append(cur[:])
                return
            for i in range(len(num)):
                if i > 0 and num[i] == num[i-1] and not used[i-1]: # remove dup
                    continue
                if not used[i]:
                    used[i] = True
                    cur.append(num[i])
                    backtrack(cur)
                    cur.pop()
                    used[i] = False

        result = []
        used = [False] * len(num)
        num.sort()
        backtrack([])
        return result


class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        solutions = [[]]

        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)

            solutions = next

        return solutions

if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2])) # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    print(Solution().permuteUnique([1, 1, 2, 1])) # [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
    print(Solution().permuteUnique([1, -1, 2, -1, 2]))
    # [[-1, -1, 1, 2, 2], [-1, -1, 2, 1, 2], [-1, -1, 2, 2, 1], [-1, 1, -1, 2, 2], [-1, 1, 2, -1, 2], [-1, 1, 2, 2, -1],
    # [-1, 2, -1, 1, 2], [-1, 2, -1, 2, 1], [-1, 2, 1, -1, 2], [-1, 2, 1, 2, -1], [-1, 2, 2, -1, 1], [-1, 2, 2, 1, -1],
    # [1, -1, -1, 2, 2], [1, -1, 2, -1, 2], [1, -1, 2, 2, -1], [1, 2, -1, -1, 2], [1, 2, -1, 2, -1], [1, 2, 2, -1, -1],
    # [2, -1, -1, 1, 2], [2, -1, -1, 2, 1], [2, -1, 1, -1, 2], [2, -1, 1, 2, -1], [2, -1, 2, -1, 1], [2, -1, 2, 1, -1],
    # [2, 1, -1, -1, 2], [2, 1, -1, 2, -1], [2, 1, 2, -1, -1], [2, 2, -1, -1, 1], [2, 2, -1, 1, -1], [2, 2, 1, -1, -1]]