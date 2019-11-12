# Time:  O(k * n^k)
# Space: O(k)

# 39
# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]
#

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target): # USE THIS: sort and prune
        def dfs(idx, cur, tgt):
            if tgt == 0 and cur:
                ans.append(list(cur)) ## KENG: must copy list to ans

            for i in range(idx, len(A)):
                if A[i] > tgt:        # prune
                    break
                cur.append(A[i])
                dfs(i, cur, tgt - A[i])
                cur.pop()

        ans, A = [], sorted(candidates)
        dfs(0, [], target)
        return ans

    # no sorting of input, no pruning
    def combinationSum2(self, candidates, target):
        def dfs(idx, cur, tgt):
            if tgt == 0 and cur:
                ans.append(list(cur))
                return
            elif tgt < 0:
                return

            for i in range(idx, len(A)):
                cur.append(A[i])
                dfs(i, cur, tgt - A[i])
                cur.pop()

        ans, A = [], candidates
        dfs(0, [], target)
        return ans

    def combinationSum_kamyu(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            self.combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1

if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7)) # [[2,2,3], [7]]
    print(Solution().combinationSum([2, 3, 5], 8)) # [[2,2,2,2], [2,3,3], [3,5]]
