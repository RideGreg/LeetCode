# Time:  O(nlogn)
# Space: O(logn)

# 254
# Numbers can be regarded as product of its factors. For example, 8 = 2x2x2 = 2x4
# Write a function that takes an integer n and return all possible combinations of its factors.
# - Assume that n is always positive.
# - Factors should be greater than 1 and less than n.

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n): # USE THIS: standard backtracking
        def backtrack(start, cur, tgt):
            if tgt == 1:
                if cur:
                    ans.append(list(cur))
            else:
                for num in range(start, n):
                    if tgt % num == 0:
                        cur.append(num)
                        backtrack(num, cur, tgt // num)
                        cur.pop()

        ans = []
        backtrack(2, [], n)
        return ans


    def getFactors_kamyu(self, n):
        result = []
        factors = []
        self.getResult(n, result, factors)
        return result

    def getResult(self, n, result, factors):
        i = 2 if not factors else factors[-1]
        while i <= n / i:
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)
                result.append(list(factors))
                factors.pop()
                self.getResult(n // i, result, factors)
                factors.pop()
            i += 1


print(Solution().getFactors(1)) # []
print(Solution().getFactors(37)) # []
print(Solution().getFactors(8)) # [[2, 4], [2, 2, 2]]
print(Solution().getFactors(12)) # [[2, 6], [2, 2, 3], [3, 4]]
print(Solution().getFactors(32))
'''
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]'''