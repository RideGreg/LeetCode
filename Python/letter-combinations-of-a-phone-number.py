# Time:  O(4^n)
# Space: O(n)

# 17
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#

# Iterative Solution
class Solution:
    # Recursive Solution
    def letterCombinations(self, digits):
        def backtrack(i, path):
            if i == len(digits):
                # https://stackoverflow.com/questions/3055477/how-slow-is-pythons-string-concatenation-vs-str-join
                ans.append(''.join(path)) # better string concatenate
                return

            if digits[i] < '2' or digits[i] > '9':
                return
            
            for c in lookup[int(digits[i])]:
                path.append(c)
                backtrack(i+1, path)
                path.pop()

        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"], []
        # filter edge case empty input: should return [] not ['']
        if digits:
            backtrack(0, [])
        return result


    # itenative
    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        total = 1
        for digit in digits:
            total *= len(lookup[int(digit)])
        result = []
        for i in xrange(total):
            base, curr = total, [""]
            for digit in digits:
                choices = lookup[int(digit)]
                base //= len(choices)
                curr.append(choices[(i//base)%len(choices)])
            result.append("".join(curr))
        return result


    # another itenative
    def letterCombinations3(self, digits):
        if not digits:
            return []

        result = [""]
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result.extend([result[i % n] for i in range(n, m * n)])
            for i in range(m * n):
                result[i] = choices[i // n] + result[i]
        return result


if __name__ == "__main__":
    print Solution().letterCombinations("23")
