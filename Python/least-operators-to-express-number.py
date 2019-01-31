# Time:  O(logn/logx) = O(1), or O(log(n, x)), n is target, we only visit up to two states for each base-x digit of target.
# Space: O(logn) = O(1)

# 964
# Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each
# operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).  For example,
# with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
#
# When writing such an expression, we adhere to the following conventions:
# - The division operator (/) returns rational numbers.
# - There are no parentheses placed anywhere.
# - We use the usual order of operations: multiplication and division happens before addition and subtraction.
# - It's not allowed to use the unary negation operator (-).  For example, "x - x" is a valid expression as it only
#   uses subtraction, but "-x + x" is not because it uses negation.

# We would like to write an expression with the least number of operators such that the expression equals the given target.
# Return the least number of operators used.
# 2 <= x <= 100
# 1 <= target <= 2 * 10^8


# Dynamic Programming:
# Target must be decomposed to sum of powers of x (x^0=x/x + x + x*x + x*x*x ...)
# for each of the above x^k, need k operators (consider the +/- op in front of it) except x^0.
# The total ops are sum of ops in each term then minus 1.
# In each modulo, both + remainder or - (x-remainder) need be considered. E.g. x=3, target=22,
# consider both 18+4 and 27-5.

from functools import lru_cache

class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        pos, neg, k = 0, 0, 0
        while target:
            target, r = divmod(target, x)
            if k:
                '''kamyu's code
                pos, neg = min(r*k + pos, (r+1)*k + neg), \
                           min((x-r)*k + pos, (x-r-1)*k + neg)
                '''

                #use x^k (cost k) as building block, so 6 need 3+3 (r=2,k=1), 18 need 3*3+3*3()
                a = r*k+pos
                b = (r+1)*k+neg
                c = (x-r)*k + pos
                d = (x-r-1)*k + neg
                pos, neg = min(a, b), min(c, d)
            else:
                pos, neg = r*2, (x-r)*2
            k += 1
        return min(pos, k+neg) - 1 # k is the cost of adding x^k in front of neg.

    # leetcode official solution
    def leastOpsExpressTarget_leetcode(self, x, target):
        cost = list(range(40))
        cost[0] = 2

        @lru_cache(None)
        def dp(i, targ):
            if targ == 0: return 0
            if targ == 1: return cost[i]
            if i >= 39: return float('inf')

            t, r = divmod(targ, x)
            return min(r * cost[i] + dp(i+1, t),
                       (x-r) * cost[i] + dp(i+1, t+1))
        return dp(0, target) - 1


print(Solution().leastOpsExpressTarget(3, 7)) # 3: 3+3+3/3
# k r  pos                                neg
# 0 1  2 (+3/3)                           4 (-3/3-3/3)
# 1 2  4 (3+3+3/3) vs 7 (3+3+3-3/3-3/3)   3 (-3+3/3) vs 4 (-3/3-3/3)
# 2                                       5 (3*3-3+3/3)
print(Solution().leastOpsExpressTarget(3, 22)) # 6: 3*3+3*3+3+3/3 or 3*3*3-3-3+3/3
# k r  pos                                           neg
# 0 1  2 (+3/3)                                      4 (-3/3-3/3)
# 1 1  3 (+3+3/3) vs 6 (+3+3-3/3-3/3)                4 (-3-3+3/3) vs 5 (-3-3/3-3/3)
# 2 2  7 (3*3+3*3+3+3/3) vs 10 (3*3+3*3+3*3-3-3+3/3) 5 (-3*3+3+3/3) vs 4 (-3-3+3/3)
# 3                                                  7 (3*3*3-3-3+3/3)

print(Solution().leastOpsExpressTarget(3, 19)) # 5: 3 * 3 + 3 * 3 + 3 / 3
print(Solution().leastOpsExpressTarget(5, 501)) # 8: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5
print(Solution().leastOpsExpressTarget(100, 10**8)) # 3 100 * 100 * 100 * 100