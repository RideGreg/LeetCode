# Time:  O(4^n / n^(1/2)) ~= Catalan numbers
# Space: O(4^n / n^(1/2)), total O(4^n / n^(3/2)) candidates each needs O(n) space to store the sequence.

# 22
# complexity analysis rests on understanding how many elements there are in generateParenthesis(n).
# It turns out this is the n-th Catalan number 1/(n+1)*(2n,n),
# which is bounded asymptotically by 4^n/(n*sqrt(n)). And multiply by n (each valid number needs n steps to produce).
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result

    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(result, current + ")", left, right - 1)

if __name__ == "__main__":
    print Solution().generateParenthesis(3)
