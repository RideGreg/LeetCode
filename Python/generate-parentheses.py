# Time:  O(4^n / n^(1/2)) ~= Catalan numbers; brute force O(4^n * n) building all 2^(2n) combinations, each take O(n)
# Space: O(n), recursion 2n depth.

# 22
# complexity analysis rests on understanding how many elements there are in generateParenthesis(n).
# It turns out this is the n-th Catalan number 1/(n+1)*(2n,n),
# which is bounded asymptotically by 4^n/(n*sqrt(n*pi)). And multiply by n (each valid number needs n steps to produce).
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#

import math
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        def backtrack(cur, left, right):
            if left == 0 and right == 0:
                result.append(cur)
            if left > 0:
                backtrack(cur + "(", left - 1, right)
            if left < right:
                backtrack(cur + ")", left, right - 1)

        result = []
        backtrack("", n, n)
        return result

    # https://math.stackexchange.com/questions/1986247/asymptotic-approximation-of-catalan-numbers
    # 4**n // ((n+1/3)*pi)**0.5 <= C(2n,n) <= 4**n // ((n+1/4)*pi)**0.5
    # thus Catalan_n = 4**n // (n**1.5 * pi**0.5)
    def catalan_upperbound(self, n):
        return 4**n // (n**1.5 * math.pi**0.5)

if __name__ == "__main__":
    print(Solution().generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]

for i in range(1, 9):
    print(Solution().catalan_upperbound(i)) # start from C_1: 1,2,5,14,42,132,429,1430
'''
2.0
3.0
6.0
18.0
51.0
157.0
499.0
1634.0
'''