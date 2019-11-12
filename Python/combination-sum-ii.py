# Time:  O(k * C(n, k))
# Space: O(k)

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
    def combinationSum2(self, candidates, target): # USE THIS: sort and prune
        def dfs(idx, cur, tgt):
            if tgt == 0 and cur:
                ans.append(list(cur))

            for i in range(idx, len(A)):
                if A[i] > tgt:
                    break
                if i == idx and A[i] != A[i - 1]: # remove duplicate
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


    def combinationSum2_kamyu(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0 and intermediate:
            result.append(list(intermediate))
        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if prev != candidates[start]: #this is a bug
                intermediate.append(candidates[start])
                self.combinationSumRecu(candidates, result, start + 1, intermediate, target - candidates[start])
                intermediate.pop()
                prev = candidates[start]
            start += 1


if __name__ == "__main__":
    print(Solution().combinationSum2([-8, 0, 8], 0))
    # [[-8, 8], [0]]

    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
