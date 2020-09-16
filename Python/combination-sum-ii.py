# Time:  O(n*2^n), n 是数组 candidates 的长度。在大部分递归 + 回溯的题目中，无法给出一个严格的渐进紧界，只能分析
# 一个较为宽松的渐进上界。最坏情况下，数组中的每个数都不相同，在递归时，每个位置可以选或不选，如果数组中所有数的和不超过
# target，那么 2^n种组合都会被枚举到；在 target 小于数组中所有数的和时，我们并不能解析地算出满足题目要求的组合的数量，
# 但我们知道每得到一个满足要求的组合，需要 O(n) 的时间将其放入答案中，因此我们将 O(2^n)与 O(n) 相乘，估算出宽松的时间复杂度上界。

# Space: O(target)，空间复杂度取决于递归的栈深度，最差情况下每次加 1，需要递归 O(target) 层。

# 40
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]
#

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target): # USE THIS: sort then we can prune
        def dfs(start, cur, tgt):
            if tgt == 0 and cur:
                ans.append(list(cur))
                # return        # WRONG cannot return here, should continue, maybe item 0 in candidates

            for i in range(start, len(A)):
                if tgt < 0 and A[i] > 0:
                #if A[i] > tgt:  # WRONG for [-8, -2], target = -10
                    break
                if i == start or A[i] != A[i - 1]: # remove duplicate
                    cur.append(A[i])
                    dfs(i + 1, cur, tgt - A[i])
                    cur.pop()

        ans, A = [], sorted(candidates)
        dfs(0, [], target)
        return ans

    def combinationSum2_while(self, candidates, target): # this also works, but for loop above is more familiar
        def dfs(res, curr, cans, target, pos):
            if target == 0 and curr:
                res.append(list(curr))
                return

            i = pos
            while i < len(cans) and cans[i] <= target:
                if i == pos or cans[i] != cans[i - 1]:
                    curr.append(cans[i])
                    dfs(res, curr, cans, target - cans[i], i + 1)
                    curr.pop()
                i += 1

        candidates = sorted(candidates)
        if not candidates or candidates[0] > target:
            return []

        res = []
        dfs(res, [], candidates, target, 0)
        return res


if __name__ == "__main__":
    print(Solution().combinationSum2([-8, 0, 8], 0))
    # [[-8, 0, 8], [-8, 8], [0]]

    print(Solution().combinationSum2([0, 0, -2], -2)) # [[-2], [-2, 0], [-2, 0, 0]]
    print(Solution().combinationSum2([-8, -10, -2], -10)) # [[-8, -2], [-10]]

    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
