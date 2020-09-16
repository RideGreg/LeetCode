# Time:  O(k * 2^9), 回溯的题目中，无法给出一个严格的渐进紧界，只能分析一个较为宽松的渐进上界。9个数每个位置可以选或不选，
# 每次递归最多选 k 个数。
# Space: O(k)

# 216
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Ensure that numbers within the set are sorted in ascending order.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
#

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}

    # USE THIS: no need to build candidate list, use min=1/max=9 directly. Good for large range candidate pool
    def combinationSum3(self, k, n):
        def backtrack(start, cur, tgt):
            if tgt == 0 and len(cur) == k:
                ans.append(list(cur))
            elif tgt > 0 and len(cur) < k:
                for num in range(start, _max + 1):
                    if num > tgt:
                        break
                    cur.append(num)
                    backtrack(num + 1, cur, tgt - num)
                    cur.pop()

        if n > 9 * k or n < k: return []
        ans, _max = [], 9
        backtrack(1, [], n)
        return ans


    def combinationSum3_kamyu(self, k, n):
        result = []
        self.combinationSumRecu(result, [], 1, k, n)
        return result

    def combinationSumRecu(self, result, intermediate, start, k, target):
        if k == 0 and target == 0:
            result.append(list(intermediate))
        elif k < 0:
            return
        while start < 10 and start * k + k * (k - 1) / 2 <= target:
            intermediate.append(start)
            self.combinationSumRecu(result, intermediate, start + 1, k - 1, target - start)
            intermediate.pop()
            start += 1

print(Solution().combinationSum3(3, 7)) # [[1,2,4]]
print(Solution().combinationSum3(3, 9)) # [[1,2,6], [1,3,5], [2,3,4]]