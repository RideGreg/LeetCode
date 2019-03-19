# Time:  O(n^2*logn), n is the # of words, Each call to solve is O(N^2), and the # of calls is bounded by O(logN),
#                     between each 2 calls, we reduce the size of possible candidates.
# Space: O(n^2), H (2D array)

# This problem is an interactive problem new to the LeetCode platform.
#
# We are given a word list of unique words, each word is 6 letters long,
# and one word in this list is chosen as secret.
#
# You may call master.guess(word) to guess a word.
# The guessed word should have type string and must be from the original
# list with 6 lowercase letters.
#
# This function returns an integer type,
# representing the number of exact matches (value and position)
# of your guess to the secret word.
# Also, if your guess is not in the given wordlist, it will return -1 instead.
#
# For each test case, you have 10 guesses to guess the word.
# At the end of any number of calls, if you have made 10 or
# less calls to master.guess
# and at least one of these guesses was the secret, you pass the testcase.
#
# Besides the example test case below,
# there will be 5 additional test cases, each with 100 words in the word list.
# The letters of each word in those testcases were chosen independently at
# random from 'a' to 'z',
# such that every word in the given word lists is unique.
#
# Example 1:
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
#
# Explanation:
#
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret
# and has all 6 matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
#
# We made 5 calls to master.guess and one of them was the secret,
# so we pass the test case.
# Note:  Any solutions that attempt to circumvent the judge will result
# in disqualification.
#
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master(object):
    def __init__(self, wordlist, secret):
        self.wordlist = wordlist
        self.secret = secret

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        if word not in self.wordlist:
            return -1
        return sum(a == b for a, b in zip(word, self.secret))



# Solution: Minimax with Heuristic
# We can guess that having less words in the word list is generally better. Use this strategy of making the guess
# that minimizes the maximum possible size of the resulting word list. If we started with N words in our word list,
# we can iterate through all possibilities for what the secret could be.
#
# Store H[i][j] as the # of matches of wordlist[i] and wordlist[j]. For each guess that hasn't been guessed before,
# do a minimax as described above, taking the guess that gives us the smallest group that might occur.

import collections
import itertools

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

class Solution(object):
    def findSecretWord(self, wordlist, master):  # USE THIS: use Counter instead of append and calculate list len
        def solve(possible):
            if len(possible) < 2: return possible[0]

            bestMaxGroupLen, bestGuess = len(possible), None
            for guess in possible:
                groups = collections.Counter(H[guess][j] for j in possible if j!= guess)
                maxGroupLen = max(groups.values())
                if maxGroupLen < bestMaxGroupLen:
                    bestMaxGroupLen, bestGuess = maxGroupLen, guess
            return bestGuess

        n = len(wordlist)
        H = [[sum(a == b for a, b in itertools.izip(wordlist[i], wordlist[j]))
                  for j in xrange(n)]
                  for i in xrange(n)]
        possible = range(n)  # init
        while possible:
            best = solve(possible)
            matches = master.guess(wordlist[best])  # KENG: write as master.guess(best)
            if matches == len(wordlist[0]): return

            possible = [j for j in possible if H[best][j] == matches] # reduce scope. KENG: easy to write for j in xrange(n)


class Solution1(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def solve(possible):
            if len(possible) < 2: return possible[0]

            min_max_group, best_guess = possible, None
            for guess in possible:
                groups = [[] for _ in xrange(7)] # the matchness between guess and secret (one in possible) is a number between 0 to 6
                for j in possible:
                    if j != guess:
                        groups[H[guess][j]].append(j)
                max_group = max(groups, key=len)
                if len(max_group) < len(min_max_group):
                    min_max_group, best_guess = max_group, guess
            return best_guess

        n = len(wordlist)
        H = [[sum(a == b for a, b in itertools.izip(wordlist[i], wordlist[j]))
                  for j in xrange(n)]
                  for i in xrange(n)]
        possible = range(n)
        while possible:
            guess = solve(possible)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return

            possible = [j for j in possible if H[guess][j] == matches] # KENG: easy to write for j in xrange(n)

# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def solve(possible):
            if len(possible) < 2: return possible[0]

            min_max_group, best_guess = possible, None
            for guess in possible:
                groups = [[] for _ in xrange(7)]
                for j in possible:
                    if j != guess:
                        groups[H[guess][j]].append(j)
                max_group = groups[0] # this is the only difference with Solution 1, choose best guess as it has least # of 0-matchness.
                            # this effectively reduces the size of possible candidates thus works, not as good as Solution 1 though.
                if len(max_group) < len(min_max_group):
                    min_max_group, best_guess = max_group, guess
            return best_guess

        n = len(wordlist)
        H = [[sum(a == b for a, b in itertools.izip(wordlist[i], wordlist[j]))
                  for j in xrange(n)]
                  for i in xrange(n)]
        possible = range(n)
        while possible:
            guess = solve(possible)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return

            possible = [j for j in possible if H[guess][j] == matches]

wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
master = Master(wordlist, wordlist[0])
print(Solution().findSecretWord(wordlist, master))
# H is
# 6 3 2 4
# 3 6 2 2
# 2 2 6 2
# 4 2 2 6

# wordlist is already known.
# If we use wordlist[0] to guess, master.guess will return one of [6,3,2,4], so one guess can find the secret.
# If we use wordlist[1] to guess, master.guess will return one of [3,6,2,2], in case of 2, we need another guess,
# so two guesses are needed to find the secret...
# so iterate all possibilities and determine the best guess (in this case it's wordlist[0]).
