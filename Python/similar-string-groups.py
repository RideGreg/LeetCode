# Time:  min(O(n^2 * l), O(n * l^3)), where n is # of words, l is the length of each word.
# Space: O(n) if n < l^2 (union find storage); or O(n * l^3) if n >= l^2, for each of nl^2
#        neighbors we store a word of length l.

# 839
# Two strings X and Y are similar if we can swap two letters
# (in different positions) of X, so that it equals Y.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to
# "tars", "rats", or "arts".
#
# Together, these form two connected groups by similarity:
# {"tars", "rats", "arts"} and {"star"}.
# Notice that "tars" and "arts" are in the same group
# even though they are not similar.
# Formally, each group is such that a word is in the group
# if and only if it is similar
# to at least one other word in the group.
#
# We are given a list A of unique strings.
# Every string in A is an anagram of every other string in A.
# How many groups are there?
#
# Example 1:
#
# Input: ["tars","rats","arts","star"]
# Output: 2
#
# Note:
# - A.length <= 2000
# - A[i].length <= 1000
# - A.length * A[i].length <= 20000
# - All words in A consist of lowercase letters only.
# - All words in A have the same length and are anagrams of each other.
# - The judging time limit has been increased for this question.


# Solution: Union-Find, but piecewise union strategy
#
# Let W = A[0].length. We can determine in O(W) time, whether two words from A are similar.
#
# One attempt is brute force: for each pair of words, draw an edge between the words if they are similar.
# We can do this in O(N^2 W) time. After, finding the # of connected components can be done in O(N^2) time
# naively (each node has up to N-1 edges), (or O(N) w/ a union-find structure.) Total complexity is O(N^2 W).
#
# Another attempt is to enumerate all neighbors of a word. A word has up to 2CW neighbors, and if a
# neighbor is a given word, that word and neighbor are connected by an edge. In this way, we can build
# the graph in O(N W^3) time, and again take O(N^2) or O(N) time to analyze the # of connected components.
#
# One insight is that between these two approaches, we can choose which approach works better. If we have
# very few words, we want to use the first approach; if we have very short words, we want to use the second
# approach. We'll piecewise add these two approaches (with complexity O(N^2 W) and O(N W^3)), to create
# an approach with O(NW min(N,W^2)) complexity.
#
# There are a few challenges involved in this problem, but each challenge is relatively straightforward.
#
# - Use a helper function similar(word1, word2) that is true if and only if two given words are similar.
# - Enumerate all neighbors of a word, and discover when it is equal to a given word.
# - Use either a union-find structure or a depth-first search, to calculate the # of connected components
# of the underlying graph.

import collections
import itertools

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.__size = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.__size -= 1
        return True

    def size(self):
        return self.__size


class Solution(object):
    def numSimilarGroups(self, A):
        def isSimilar(a, b):
            diff = 0
            for x, y in itertools.izip(a, b):
                if x != y:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 2

        N, L = len(A), len(A[0])
        union_find = UnionFind(N)
        if N < L*L:
            for (i1, word1), (i2, word2) in \
                    itertools.combinations(enumerate(A), 2):
                if isSimilar(word1, word2):
                    union_find.union_set(i1, i2)
        else:
            buckets = collections.defaultdict(set)
            for i in xrange(len(A)):
                word = list(A[i])
                for j1, j2 in itertools.combinations(xrange(L), 2):
                    word[j1], word[j2] = word[j2], word[j1]
                    buckets["".join(word)].add(i)
                    word[j1], word[j2] = word[j2], word[j1]

            for i, word in enumerate(A):
                for j in buckets[word]:
                    union_find.union_set(i, j)
        return union_find.size()
