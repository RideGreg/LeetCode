# Time:  O(10! * n * l)
# Space: O(n * l)


# 1307 Verbal Arithmetic Puzzle

# Given an equation, represented by words on left side and the result on right side.
#
# You need to check if the equation is solvable under the following rules:
#
#     Each character is decoded as one digit (0 - 9).
#     Every pair of different characters they must map to different digits.
#     Each words[i] and result are decoded as one number without leading zeros.
#     Sum of numbers on left side (words) will equal to the number on right side (result).
#
# Return True if the equation is solvable otherwise return False.

# Constraints:
#
#     2 <= words.length <= 5
#     1 <= words[i].length, results.length <= 7
#     words[i], result contains only upper case English letters.
#     Number of different characters used on the expression is at most 10.

import collections


class Solution(object):
    def isSolvable(self, words, result):
        """
        :type words: List[str]
        :type result: str
        :rtype: bool
        """
        # i: index of word on left side
        # j: index of char in the word on right side
        def backtracking(words, result, i, j, carry, lookup, used):
            if j == len(result):
                return carry == 0

            if i != len(words): # i == len(words) means for position j, all words on left side have been assigned a value
                if j >= len(words[i]) or words[i][j] in lookup:
                    return backtracking(words, result, i+1, j, carry, lookup, used)     
                for val in range(10):
                    if val in used or (val == 0 and j == len(words[i])-1):
                        continue
                    lookup[words[i][j]] = val
                    used.add(val)
                    if backtracking(words, result, i+1, j, carry, lookup, used):
                        return True
                    used.remove(val)
                    del lookup[words[i][j]]
                return False

            carry, val = divmod(carry + sum(lookup[w[j]] for w in words if j < len(w)), 10)
            if result[j] in lookup:
                return val == lookup[result[j]] and \
                       backtracking(words, result, 0, j+1, carry, lookup, used)
            if val in used or (val == 0 and j == len(result)-1):
                return False
            lookup[result[j]] = val
            used.add(val)
            if backtracking(words, result, 0, j+1, carry, lookup, used):
                return True
            used.remove(val)
            del lookup[result[j]]
            return False
        
        return backtracking([w[::-1] for w in words], result[::-1], 0, 0, 0, {}, set())

    # much slow than above solution
    def isSolvable_ming(self, words, result):
        cmap = {}
        leading = set()
        for w in words+[result]:
            for i,c in enumerate(w):
                cmap[c] = -1
                if i == 0:
                    leading.add(c)
        lead = list(leading)
        follow = [c for c in cmap.keys() if c not in leading]

        def replace(s):
            ans = 0
            for c in s:
                ans = ans*10 + cmap[c]
            return ans

        def dfs(cur, mask):
            if cur == len(lead):
                lmin, lmax = 0, 0
                for w in words:
                    l = len(w) - 1
                    lmin += int(cmap[w[0]])*(10**l)
                    lmax += int(cmap[w[0]]+1)*(10**l) - 1
                l = len(result) - 1
                rmin = int(cmap[result[0]])*(10**l)
                rmax = int(cmap[result[0]] + 1) * (10**l) - 1
                if rmin > lmax or lmin > rmax:
                    return False

            if cur == len(clist):
                return sum(replace(w) for w in words) == replace(result)

            for i in range(int(clist[cur] in leading), 10):
                if mask & (1<<i) == 0:
                    cmap[clist[cur]] = i
                    if dfs(cur+1, mask | (1<<i)): return True
            return False

        clist = lead + follow
        mask = 0
        return dfs(0, mask)

print(Solution().isSolvable(["SEND","MORE"], "MONEY"))
# True 9567 + 1085 = 10652
print(Solution().isSolvable(["SIX","SEVEN","SEVEN"], "TWENTY"))
# True 650 + 68782 + 68782 = 138214
print(Solution().isSolvable(["THIS","IS","TOO"], "FUNNY"))
# True
print(Solution().isSolvable(["LEET","CODE"], "POINT"))
# False