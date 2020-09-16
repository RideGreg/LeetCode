# Time:  O(S), 其中 S为所有可行解的长度之和。本题是一棵搜索树，时间复杂度取决于搜索树所有叶子节点的
# 深度之和，即所有可行解的长度之和。本题很难给出一个比较紧的上界，O(n×2^n) 是一个比较松的上界，即n个位置
# 每次考虑选或者不选，共2^n种可能，再乘上每次时间代价 n。实际运行时不可能所有的解都满足条件，我们还会剪枝，
# 所以实际运行情况是远远小于这个上界的。n是candidates数组长度。

# Space: O(target)，空间复杂度取决于递归的栈深度，最差情况下每次加 1，需要递归 O(target) 层。

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
    def combinationSum(self, candidates, target): # USE THIS: sort is important, only then we can prune
        def backtrack(start, cur, tgt):
            if tgt == 0 and cur:
                ans.append(list(cur)) ## KENG: must copy list to ans
            else:
                for i in range(start, len(A)):
                    if A[i] > tgt:        # prune
                        break
                    #if i > start and A[i] == A[i-1]: continue # this dup removal also ok
                    cur.append(A[i])
                    backtrack(i, cur, tgt - A[i])
                    cur.pop()

        ans, A = [], sorted(set(candidates)) # remove dup since each number can use unlimited times
        backtrack(0, [], target)
        return ans



if __name__ == "__main__":
    print(Solution().combinationSum([1,1,3], 4)) # [[1,3]]
    print(Solution().combinationSum([3, 2, 6, 7], 7)) # [[2,2,3], [7]]
    print(Solution().combinationSum([5, 2, 3], 8)) # [[2,2,2,2], [2,3,3], [3,5]]
